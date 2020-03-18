from django.urls import include, path

from chord_Generator.views import ChordView

urlpatterns = [
    path('', ChordView.as_view(), name='chords')
]
