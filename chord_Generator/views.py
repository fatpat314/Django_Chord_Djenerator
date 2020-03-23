from django.shortcuts import render
from django.views.generic.list import ListView
from chord_Generator.sample import sample_by_frequency
from chord_Generator.markov_chord import MarkovChord

from chord_Generator.models import Chords
from chord_Generator.app import generate_chords


amount = 8
# Create your views here.
class ChordAmountView(ListView):
    model = Chords

    def get(self,request):
        key = "chord_Generator/keys/chord_list.txt"

        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'splash.html',{'chords' : chords})

class KeyView_A(ListView):
    model = Chords
    def get(self,request):

        key = "chord_Generator/keys/A.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})

class KeyView_Bb(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/A#Bb.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})

class KeyView_B(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/B.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})

class KeyView_C(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/C.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})

class KeyView_Db(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/C#Db.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})

class KeyView_D(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/D.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})

class KeyView_Eb(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/D#Eb.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})

class KeyView_E(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/E.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})

class KeyView_F(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/F.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})

class KeyView_Gb(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/F#Gb.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})

class KeyView_G(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/G.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})

class KeyView_Ab(ListView):
    model = Chords
    def get(self,request):
        key = "chord_Generator/keys/G#Ab.txt"
        chord = generate_chords(key, amount)
        chords = chord
        return render(request, 'home.html',{'chords' : chords})
