from flask import Flask, render_template
from chord_Generator.sample import sample_by_frequency
from chord_Generator.markov_chord import MarkovChord

# app = Flask(__name__)


# @app.route('/')
def generate_chords():
    my_file = open("chord_Generator/chord_list.txt")
    lines = my_file.readlines()

    chord_list = []

    for line in lines:
        for chord in line.split():
            chord_list.append(chord)

    markovchain = MarkovChord(chord_list)

    chords_as_list = markovchain.walk(10).split()

    return chords_as_list
    #chords=markovchain.walk(10)










# if __name__ == '__main__':
    # app.run()
