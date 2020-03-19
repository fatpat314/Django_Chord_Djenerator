from django.urls import include, path

from chord_Generator.views import ChordAmountView, KeyView_A, KeyView_Bb, KeyView_B, KeyView_C, KeyView_Db, KeyView_D, KeyView_Eb, KeyView_E, KeyView_F, KeyView_Gb, KeyView_G, KeyView_Ab

urlpatterns = [
    path('', ChordAmountView.as_view(), name='chords'),
    path('A/', KeyView_A.as_view(), name='/A'),
    path('Bb/', KeyView_Bb.as_view(), name='A#Bb'),
    path('B/', KeyView_B.as_view(), name='B'),
    path('C/', KeyView_C.as_view(), name='C'),
    path('Db/', KeyView_Db.as_view(), name='C#Db'),
    path('D/', KeyView_D.as_view(), name='D'),
    path('Eb/', KeyView_Eb.as_view(), name='D#Eb'),
    path('E/', KeyView_E.as_view(), name='E'),
    path('F/', KeyView_F.as_view(), name='F'),
    path('Gb/', KeyView_Gb.as_view(), name='F#Gb'),
    path('G/', KeyView_G.as_view(), name='G'),
    path('Ab/', KeyView_Ab.as_view(), name='G#Ab'),

]
"""And so on, there must be a better way"""
