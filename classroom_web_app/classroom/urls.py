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
    # path('<int:classroom_id>/edit/', views.edit_classroom, name='edit_classroom'),  # Edit classroom
    # path('<int:classroom_id>/delete/', views.delete_classroom, name='delete_classroom'),  # Delete class
    # path('submission/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),  # Submit assignment
    # path('comment/<int:announcement_id>/', views.add_comment, name='add_comment'),  #Add comment
]
