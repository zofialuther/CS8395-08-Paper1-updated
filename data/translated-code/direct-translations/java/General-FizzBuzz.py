class FizzBuzz:
    def main(self):
        sounds = [Sound(3, "Fizz"), Sound(5, "Buzz"), Sound(7, "Baxx")]
        for i in range(1, 21):
            sb = ""
            for sound in sounds:
                sb += sound.generate(i)
            print(i if len(sb) == 0 else sb)

class Sound:
    def __init__(self, trigger, onomatopoeia):
        self.trigger = trigger
        self.onomatopoeia = onomatopoeia

    def generate(self, i):
        return self.onomatopoeia if i % self.trigger == 0 else ""

fizz_buzz = FizzBuzz()
fizz_buzz.main()