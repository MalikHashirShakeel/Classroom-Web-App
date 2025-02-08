from django.contrib import admin
from .models import Classroom, Enrollment, Announcement, Assignment, Submission, Comment

# Classroom Admin
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_code', 'created_by', 'created_at')
    search_fields = ('name', 'class_code', 'created_by__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

# Enrollment Admin
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'student', 'enrolled_at')
    search_fields = ('classroom__name', 'student__username')
    list_filter = ('enrolled_at',)

# Announcement Admin
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'created_by', 'created_at', 'file')
    search_fields = ('title', 'content', 'classroom__name', 'created_by__username')
    list_filter = ('created_at',)

# Assignment Admin
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'created_by', 'due_date', 'created_at', 'file')
    search_fields = ('title', 'classroom__name', 'created_by__username')
    list_filter = ('due_date', 'created_at')

# Submission Admin
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'submitted_at', 'file', 'grade')
    search_fields = ('assignment__title', 'student__username')
    list_filter = ('submitted_at',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_by', 'assignment', 'announcement', 'is_private', 'created_at')
    search_fields = ('content', 'created_by__username', 'assignment__title', 'announcement__title')
    list_filter = ('created_at', 'is_private')
    ordering = ('-created_at',)
    list_display_links = ('content',)

# Register Models
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Comment, CommentAdmin)
