from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'short_message', 'created_at')  
    search_fields = ('name', 'email', 'message')  
    list_filter = ('created_at',)  
    ordering = ('-created_at',)  

    def short_message(self, obj):
        return obj.message[:50] + ("..." if len(obj.message) > 50 else "")
    short_message.short_description = "Message"

admin.site.register(Message, MessageAdmin)
