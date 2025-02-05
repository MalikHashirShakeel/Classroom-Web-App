from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Classroom, Enrollment
from .forms import ClassroomForm
from django.contrib import messages

@login_required
def classroom_list(request):
    """Display classrooms created by the user and classrooms the user is enrolled in."""
    created_classrooms = Classroom.objects.filter(created_by=request.user)
    enrolled_classrooms = Classroom.objects.filter(enrollment__student=request.user)

    context = {
        'created_classrooms': created_classrooms,
        'enrolled_classrooms': enrolled_classrooms,
    }
    return render(request, 'classroom/classroom_list.html', context)

#------------------------------------------------------------

@login_required
def create_classroom(request):
    """View to create a new classroom."""
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.created_by = request.user
            classroom.save()
            return redirect('classroom_list')
    else:
        form = ClassroomForm()

    context = {
        'form': form,
    }
    return render(request, 'classroom/create_classroom.html', context)

#------------------------------------------------------------

@login_required
def join_classroom(request):
    """View to join a classroom using a class code."""
    if request.method == 'POST':
        class_code = request.POST.get('class_code')
        try:
            classroom = Classroom.objects.get(class_code=class_code)
            # Check if the user is already enrolled
            if not Enrollment.objects.filter(classroom=classroom, student=request.user).exists():
                Enrollment.objects.create(classroom=classroom, student=request.user)
                messages.success(request, f'You have successfully joined {classroom.name}!')
            else:
                messages.warning(request, 'You are already enrolled in this classroom.')
            return redirect('classroom_list')
        except Classroom.DoesNotExist:
            messages.error(request, 'Invalid class code. Please try again.')

    return render(request, 'classroom/join_classroom.html')
