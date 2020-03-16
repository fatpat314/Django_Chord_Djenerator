from chordogram import Chordogram

class MarkovChord:

    def __init__ (self, chord_list):

        self.markov_chain = self.build_markov(chord_list)
        self.first_chord = list(self.markov_chain.keys())[0]

    def build_markov(self, chord_list):
        markov_chain = {}

        for i in range(len(chord_list)-1):
            current_chord = chord_list[i]
            next_chord = chord_list[i+1]

            if current_chord in markov_chain.keys():
                chordogram = markov_chain[current_chord]

                chordogram.dictionary_chordogram[next_chord] = chordogram.dictionary_chordogram.get(next_chord, 0) +1
            else:
                markov_chain[current_chord] = Chordogram([next_chord])

        return markov_chain

    def walk(self, num_chords):

        chord = self.first_chord

        chord_chart = ""

        for i in range(num_chords):
            chord_chart += chord + " "
            chordogram = self.markov_chain[chord]

            chord = chordogram.sample()

        return chord_chart

    def print_chain(self):
        for chord, chordogram in self.markov_chain.items():
            print(chord, chordogram.dictionary_chordogram)

markov_chain = MarkovChord(["C", "G", "Am", "G", "Dm", "G"])
markov_chain.print_chain()
print(markov_chain.walk(20))
