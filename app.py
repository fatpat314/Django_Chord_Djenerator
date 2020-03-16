from flask import Flask
from sample import sample_by_frequency
from markov_chord import MarkovChord

app = Flask(__name__)

@app.route('/')
def generate_words():
    my_file = open("./chord_list.txt")
    lines = my_file.readlines()

    chord_list = []

    for line in lines:
        for chord in line.split():
            chord_list.append(chord)

    markovchain = MarkovChord(chord_list)

    return markovchain.walk(10)


if __name__ == '__main__':
    app.run()
