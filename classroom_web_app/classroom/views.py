from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Classroom, Enrollment, Announcement, Assignment, Submission
from .forms import ClassroomForm, AnnouncementForm, AssignmentForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User

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

#-------------------------------------------------------------


@login_required
def classroom_detail(request, classroom_id):
    """View to display classroom details, announcements, and assignments."""
    classroom = get_object_or_404(Classroom, id=classroom_id)
    announcements = Announcement.objects.filter(classroom=classroom).order_by('-created_at')
    assignments = Assignment.objects.filter(classroom=classroom).order_by('-created_at')

    is_creator = classroom.created_by == request.user

    context = {
        'classroom': classroom,
        'announcements': announcements,
        'assignments': assignments,
        'is_creator': is_creator,
    }
    return render(request, 'classroom/classroom_detail.html', context)

#------------------------------------------------------------

@login_required
def add_announcement(request, classroom_id):
    """View to add an announcement to a classroom."""
    classroom = get_object_or_404(Classroom, id=classroom_id)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.classroom = classroom
            announcement.created_by = request.user
            announcement.save()
            return redirect('classroom_detail', classroom_id=classroom.id)
    else:
        form = AnnouncementForm()
    context = {
        'form': form,
        'classroom': classroom,
    }
    return render(request, 'classroom/add_announcement.html', context)

@login_required
def delete_announcement(request, announcement_id):
    """View to delete an announcement."""
    announcement = get_object_or_404(Announcement, id=announcement_id)
    if announcement.created_by == request.user:
        announcement.delete()
    return redirect('classroom_detail', classroom_id=announcement.classroom.id)

@login_required
def add_assignment(request, classroom_id):
    """View to add an assignment to a classroom."""
    classroom = get_object_or_404(Classroom, id=classroom_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.classroom = classroom
            assignment.created_by = request.user
            assignment.save()
            return redirect('classroom_detail', classroom_id=classroom.id)
    else:
        form = AssignmentForm()
    context = {
        'form': form,
        'classroom': classroom,
    }
    return render(request, 'classroom/add_assignment.html', context)

@login_required
def delete_assignment(request, assignment_id):
    """View to delete an assignment."""
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if assignment.created_by == request.user:
        assignment.delete()
    return redirect('classroom_detail', classroom_id=assignment.classroom.id)

#------------------------------------------------------------

@login_required
def view_announcement(request, announcement_id):
    """View to display the full details of an announcement."""
    announcement = get_object_or_404(Announcement, id=announcement_id)
    is_creator = announcement.created_by == request.user

    context = {
        'announcement': announcement,
        'is_creator': is_creator,
    }
    return render(request, 'classroom/view_announcement.html', context)

#------------------------------------------------------------

@login_required
def edit_announcement(request, announcement_id):
    """View to edit an announcement."""
    announcement = get_object_or_404(Announcement, id=announcement_id)
    if announcement.created_by != request.user:
        return redirect('view_announcement', announcement_id=announcement.id)

    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('view_announcement', announcement_id=announcement.id)
    else:
        form = AnnouncementForm(instance=announcement)

    context = {
        'form': form,
        'announcement': announcement,
    }
    return render(request, 'classroom/edit_announcement.html', context)

#------------------------------------------------------------

@login_required
def view_assignment(request, assignment_id):
    """View to display the full details of an assignment."""
    assignment = get_object_or_404(Assignment, id=assignment_id)
    is_creator = assignment.created_by == request.user
    is_due_date_passed = timezone.now() > assignment.due_date
    submission = Submission.objects.filter(assignment=assignment, student=request.user).first()

    context = {
        'assignment': assignment,
        'is_creator': is_creator,
        'is_due_date_passed': is_due_date_passed,
        'submission': submission,
    }
    return render(request, 'classroom/view_assignment.html', context)

#------------------------------------------------------------

@login_required
def edit_assignment(request, assignment_id):
    """View to edit an assignment."""
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if assignment.created_by != request.user:
        return redirect('view_assignment', assignment_id=assignment.id)

    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('view_assignment', assignment_id=assignment.id)
    else:
        form = AssignmentForm(instance=assignment)

    context = {
        'form': form,
        'assignment': assignment,
    }
    return render(request, 'classroom/edit_assignment.html', context)

#------------------------------------------------------------

@login_required
def submit_assignment(request, assignment_id):
    """View to submit an assignment."""
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            Submission.objects.create(
                assignment=assignment,
                student=request.user,
                file=file
            )
            return redirect('view_assignment', assignment_id=assignment.id)
    return render(request, 'classroom/submit_assignment.html', {'assignment': assignment})

#------------------------------------------------------------

@login_required
def edit_submission(request, submission_id):
    """View to edit a submission."""
    submission = get_object_or_404(Submission, id=submission_id)
    if submission.student != request.user:
        return redirect('view_assignment', assignment_id=submission.assignment.id)

    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            submission.file = file
            submission.save()
            return redirect('view_assignment', assignment_id=submission.assignment.id)
    return render(request, 'classroom/edit_submission.html', {'submission': submission})

#------------------------------------------------------------

@login_required
def cancel_submission(request, submission_id):
    """View to cancel a submission."""
    submission = get_object_or_404(Submission, id=submission_id)
    if submission.student != request.user:
        return redirect('view_assignment', assignment_id=submission.assignment.id)

    submission.delete()
    return redirect('view_assignment', assignment_id=submission.assignment.id)

#------------------------------------------------------------

@login_required
def view_submissions(request, assignment_id):
    """View to display all submissions for an assignment and list students who haven't submitted."""
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if assignment.created_by != request.user:
        return redirect('view_assignment', assignment_id=assignment.id)
    
    submissions = Submission.objects.filter(assignment=assignment)

    enrolled_students = User.objects.filter(enrollment__classroom=assignment.classroom)

    submitted_students = submissions.values_list('student', flat=True)
    not_submitted_students = enrolled_students.exclude(id__in=submitted_students)

    context = {
        'assignment': assignment,
        'submissions': submissions,
        'not_submitted_students': not_submitted_students,
    }
    return render(request, 'classroom/view_submissions.html', context)