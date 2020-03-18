from random import randint


chord_counts = {'one':1, 'fish':4, 'two':1, 'red':1, 'blue':1}
def sample_by_frequency(chordogram):
    random_index = randint(0, sum(chordogram.values())-1)

    start = 0

    for chord, count in chordogram.items():
        end = start + count

        if random_index >= start and random_index < end:
            return chord

        start = end

print(sample_by_frequency(chord_counts))
