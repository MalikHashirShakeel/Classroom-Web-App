from django.urls import path
from . import views

urlpatterns = [
    path('', views.classroom_list, name='classroom_list'),  # View all classrooms
    path('create/', views.create_classroom, name='create_classroom'),  # Create a new class
    path('join/', views.join_classroom, name='join_classroom'),  # Join a classroom
    path('<int:classroom_id>/', views.classroom_detail, name='classroom_detail'),  # View class details
    path('<int:classroom_id>/announcement/add/', views.add_announcement, name='add_announcement'),
    path('<int:classroom_id>/assignment/add/', views.add_assignment, name='add_assignment'),  # Add assignment
    path('announcement/<int:announcement_id>/delete/', views.delete_announcement, name='delete_announcement'),  # Delete announcement
    path('assignment/<int:assignment_id>/delete/', views.delete_assignment, name='delete_assignment'),  # Delete assignment
    path('announcement/<int:announcement_id>/', views.view_announcement, name='view_announcement'),  # View announcement
    path('announcement/<int:announcement_id>/edit/', views.edit_announcement, name='edit_announcement'),  # Edit announcement
    path('assignment/<int:assignment_id>/', views.view_assignment, name='view_assignment'),  # View assignment
    path('assignment/<int:assignment_id>/edit/', views.edit_assignment, name='edit_assignment'),  # Edit assignment
    path('assignment/<int:assignment_id>/submit/', views.submit_assignment, name='submit_assignment'),  # Submit assignmen
    path('submission/<int:submission_id>/edit/', views.edit_submission, name='edit_submission'),  # Edit submission
    path('submission/<int:submission_id>/cancel/', views.cancel_submission, name='cancel_submission'),  # Cancel submission
    path('assignment/<int:assignment_id>/submissions/', views.view_submissions, name='view_submissions'),
    path('<str:object_type>/<int:object_id>/comments/', views.view_comments, name='view_comments'),  # View comments
    path('comment/<int:comment_id>/reply/', views.add_reply, name='add_reply'),  # Add reply
    path('<int:classroom_id>/students/', views.view_students, name='view_students'),  # View all students
    path('<int:classroom_id>/students/<int:student_id>/delete/', views.delete_student, name='delete_student'),  # Delete student
    path('<int:classroom_id>/add-student/', views.add_student, name='add_student'),  # Add student by email
]
