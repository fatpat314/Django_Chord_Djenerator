Welcome to the Django Jazz Chord Djenerator. Choose the number of chords you want and the key and start writing.



The Django Jazz Chord Djenerator uses a markov-chain to produce a chord progression of any given length in whatever key the user desires.

This is achieved by changing the data that is used in the markov-chain depending on the users choice. The markov-chain then randomly selects a chord in the key the user selected. The markov-chain then determines the next chord depending on the relationship between the current chord and the next chord and repeats this process until the desired number of chords is reached.

See it live: https://chord-generator-pk.herokuapp.com/A/?quantity=
