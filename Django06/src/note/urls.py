from django.urls import path
from .views import NoteListView, NoteCreateView, NoteDeleteView, SharedNoteListView, ShareNoteView, UnShareNoteView


app_name = 'note'

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('delete/<int:pk>', NoteDeleteView.as_view(), name='note-delete'),
    path('shared-note-list/', SharedNoteListView.as_view(), name='shared-note-list'),
    path('share-note/<int:pk>', ShareNoteView.as_view(), name='share-note'),
    path('unshare-note/<int:pk>', UnShareNoteView.as_view(), name='unshare-note'),
]
