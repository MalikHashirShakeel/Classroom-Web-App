from django.urls import path
from . import views

urlpatterns = [
    path('', views.classroom_list, name='classroom_list'),  # View all classrooms
    # path('create/', views.create_classroom, name='create_classroom'),  # Create a new class
    # path('<int:classroom_id>/', views.classroom_detail, name='classroom_detail'),  # View class details
    # path('<int:classroom_id>/edit/', views.edit_classroom, name='edit_classroom'),  # Edit classroom
    # path('<int:classroom_id>/delete/', views.delete_classroom, name='delete_classroom'),  # Delete class
    # path('<int:classroom_id>/join/', views.join_classroom, name='join_classroom'),  # Join a class
    # path('<int:classroom_id>/announcement/', views.add_announcement, name='add_announcement'),  # Add announcement
    # path('<int:classroom_id>/assignment/', views.add_assignment, name='add_assignment'),  # Add assignment
    # path('submission/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),  # Submit assignment
    # path('comment/<int:announcement_id>/', views.add_comment, name='add_comment'),  #Add comment
]
