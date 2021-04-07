from notes.serializers import NoteSerializer
from notes.models import Note
from django.shortcuts import render
from rest_framework import generics
from datetime import datetime


# Create your views here.
class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_update(self, serializer):
        serializer.save(date_updated = datetime.now())