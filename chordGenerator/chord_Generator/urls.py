from django.urls import include, path

from chord_Generator.views import ChordView, KeyView

urlpatterns = [
    path('', ChordView.as_view(), name='chords'),
    path('A/', KeyView.as_view(), name='A')
]
