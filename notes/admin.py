from django.contrib import admin
from . import models

class NotesAdmin(admin.ModelAdmin):
    # shows the notes in admin panel by their title
    list_display = ('title',)

admin.site.register(models.Notes, NotesAdmin)

'''
Shell commands:
from notes.models import Notes
first_note = Notes.objects.get(pk='1')
new_note = Notes.objects.create(title='Second Note', text='Second note description')
filtering: Notes.objects.filter(title__icontains('note'))
excluding: Notes.objects.exclude(text__icontains('note'))
Chaining: Notes.objects.filter(title__icontains('not')).exlude(text__icontains('Django'))
'''
