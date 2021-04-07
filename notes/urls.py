from django.urls import path, include
from . import views 

urlpatterns = [
    path('notes/', views.NoteList.as_view(), name='note_list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='note_detail'),
]
