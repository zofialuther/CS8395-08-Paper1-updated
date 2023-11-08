class Sound:
    def __init__(self, trigger, onomatopoeia):
        self.trigger = trigger
        self.onomatopoeia = onomatopoeia

    def generate(self, i):
        if i % self.trigger == 0:
            return self.onomatopoeia
        else:
            return ""

sounds = [Sound(3, "Fizz"), Sound(5, "Buzz"), Sound(7, "Baxx")]

for i in range(1, 21):
    sb = ""
    for sound in sounds:
        sb += sound.generate(i)
    if len(sb) == 0:
        print(i)
    else:
        print(sb)