class LastLetterFirstLetter:
    maxPathLength = 0
    maxPathLengthCount = 0
    maxPathExample = ""

    names = ["audino", "bagon", "baltoy", "banette",
             "bidoof", "braviary", "bronzor", "carracosta", "charmeleon",
             "cresselia", "croagunk", "darmanitan", "deino", "emboar",
             "emolga", "exeggcute", "gabite", "girafarig", "gulpin",
             "haxorus", "heatmor", "heatran", "ivysaur", "jellicent",
             "jumpluff", "kangaskhan", "kricketune", "landorus", "ledyba",
             "loudred", "lumineon", "lunatone", "machamp", "magnezone",
             "mamoswine", "nosepass", "petilil", "pidgeotto", "pikachu",
             "pinsir", "poliwrath", "poochyena", "porygon2", "porygonz",
             "registeel", "relicanth", "remoraid", "rufflet", "sableye",
             "scolipede", "scrafty", "seaking", "sealeo", "silcoon",
             "simisear", "snivy", "snorlax", "spoink", "starly", "tirtouga",
             "trapinch", "treecko", "tyrogue", "vigoroth", "vulpix",
             "wailord", "wartortle", "whismur", "wingull", "yamask"]

    @staticmethod
    def recursive(part, offset):
        global maxPathLength, maxPathLengthCount, maxPathExample, names
        if offset > maxPathLength:
            maxPathLength = offset
            maxPathLengthCount = 1
        elif offset == maxPathLength:
            maxPathLengthCount += 1
            maxPathExample = ""
            for i in range(offset):
                maxPathExample += ("\n  " if i % 5 == 0 else " ") + part[i]

        lastChar = part[offset - 1][-1]
        for i in range(offset, len(part)):
            if part[i][0] == lastChar:
                tmp = names[offset]
                names[offset] = names[i]
                names[i] = tmp
                LastLetterFirstLetter.recursive(names, offset + 1)
                names[i] = names[offset]
                names[offset] = tmp

    @staticmethod
    def main(args):
        global maxPathLength, maxPathLengthCount, maxPathExample, names
        for i in range(len(names)):
            tmp = names[0]
            names[0] = names[i]
            names[i] = tmp
            LastLetterFirstLetter.recursive(names, 1)
            names[i] = names[0]
            names[0] = tmp
        print("maximum path length        : " + str(maxPathLength))
        print("paths of that length       : " + str(maxPathLengthCount))
        print("example path of that length:" + maxPathExample)


LastLetterFirstLetter.main([])