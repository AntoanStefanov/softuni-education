class Guitar:
    def play(self):
        print("playing the guitar")


class Piano:
    def play(self):
        print("playing the piano")


guitar = Guitar()
piano = Piano()

# 15 / 16 for judge


def play_instrument(instrument): # instrument: Instrument
    return instrument.play()


play_instrument(guitar)
play_instrument(piano)
