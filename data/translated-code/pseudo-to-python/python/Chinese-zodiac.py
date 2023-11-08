def zodiacNames():
    return {
        'tian': list(zip('甲乙丙丁戊己庚辛壬癸', 'jiă yĭ bĭng dīng wù jĭ gēng xīn rén gŭi')),
        'di': list(zip('子丑寅卯辰巳午未申酉戌亥', 'zĭ chŏu yín măo chén sì wŭ wèi shēn yŏu xū hài')),
        'wu': ['木火土金水', 'mù huǒ tǔ jīn shuǐ', 'wood fire earth metal water'],
        'sx': ['鼠牛虎兔龍蛇馬羊猴鸡狗豬', 'shǔ niú hǔ tù lóng shé mǎ yáng hóu jī gǒu zhū', 'rat ox tiger rabbit dragon snake horse goat monkey rooster dog pig'],
        'yy': ['阳阴', 'yáng yīn']
    }

def zodiacYear(zodiacDict):
    def tokens(year):
        iYear = year - 4
        iStem = iYear % 10
        iBranch = iYear % 12
        hStem, pStem = zodiacDict['tian'][iStem]
        hBranch, pBranch = zodiacDict['di'][iBranch]
        yy = iYear % 2
        return [
            [str(year), '', ''],
            [hStem + hBranch, pStem + pBranch, str(iYear % 60 + 1)],
            zodiacDict['wu'][iStem // 2],
            zodiacDict['sx'][iBranch],
            [zodiacDict['yy'][yy], 'dark' if yy == 1 else 'light']
        ]
    return tokens

def main():
    zodiacDict = zodiacNames()
    print(''.join(map(zodiacTable(zodiacDict), [1935, 1938, 1949, 1968, 1972, 1976, 2022])))

def zodiacTable(zodiacDict):
    def zodiacYearTable(year):
        return wikiTable({'class': 'wikitable', 'colwidth': '20'}, transpose(zodiacYear(zodiacDict)(year)))
    return zodiacYearTable

def wikiTable(attrs):
    def colWidth():
        return 'width:' + attrs['colwidth'] + '; ' if 'colwidth' in attrs else ''
    
    def cellStyle():
        return attrs['cell']

    def wikiTableString(data):
        return ('{| ' + ' '.join(f'{key}="{value}"' for key, value in attrs.items() if key != 'colwidth' and key != 'cell') + '\n' +
                '\n|-' + ''.join(f'|style="{colWidth()}{cellStyle()}"|{str(cell)}\n' for row in data for cell in row) +
                '\n|}' + '\n\n')

    return wikiTableString

def transpose(matrix):
    if matrix:
        inner = type(matrix[0])
        z = zip(*matrix)
        return list(map(inner, z)) if inner is tuple else list(z)
    else:
        return matrix

if __name__ == '__main__':
    main()