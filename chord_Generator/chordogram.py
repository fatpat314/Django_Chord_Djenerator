from random import randint

class Chordogram:

    def __init__(self, chord_list):

        self.chord_list = chord_list

        self.dictionary_chordogram = self.build_chordogram()
        print(self.dictionary_chordogram)

        self.tokens = sum(self.dictionary_chordogram.values())

    def build_chordogram(self):
        #Make an empty dictionary
        chordogram = {}

        #loop for each chord in the chord_list
        for chord in self.chord_list:
            #add chord into dictionary
            chordogram[chord] = chordogram.get(chord, 0) + 1

        return chordogram

    def sample(self):
        random_index = randint(0,sum(self.dictionary_chordogram.values())-1)

        start = 0

        for chord, count in self.dictionary_chordogram.items():
            end = start + count

            if random_index >= start and random_index < end:
                return chord

            start = end
