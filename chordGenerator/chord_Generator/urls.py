from django.urls import include, path

from chord_Generator.views import ChordView, KeyView_A, KeyView_Bb

urlpatterns = [
    path('', ChordView.as_view(), name='chords'),
    path('A/', KeyView_A.as_view(), name='A'),
    path('Bb/', KeyView_Bb.as_view(), name='A#Bb'),
    # path('B/', KeyView_B.as_view(), name='B'),

]
"""And so on, there must be a better way"""
