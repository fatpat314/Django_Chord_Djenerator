from django.shortcuts import render
from django.views.generic.list import ListView
from chord_Generator.sample import sample_by_frequency
from chord_Generator.markov_chord import MarkovChord

from chord_Generator.models import Chords
from chord_Generator.app import generate_chords


# Create your views here.
class ChordView(ListView):
    model = Chords

    def get(self,request):
        key = "chord_Generator/keys/chord_list.txt"
        chord = generate_chords(key)
        chords = chord
        return render(request, '/Users/patrickkelly/Desktop/Projects_2020/spring_intensive/chordGenerator/chord_Generator/templates/home.html',{'chords' : chords})

class KeyView_A(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/F.txt"
        chord = generate_chords(key)
        chords = chord
        return render(request, '/Users/patrickkelly/Desktop/Projects_2020/spring_intensive/chordGenerator/chord_Generator/templates/home.html',{'chords' : chords})

class KeyView_Bb(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/A#Bb.txt"
        chord = generate_chords(key)
        chords = chord
        return render(request, '/Users/patrickkelly/Desktop/Projects_2020/spring_intensive/chordGenerator/chord_Generator/templates/home.html',{'chords' : chords})
