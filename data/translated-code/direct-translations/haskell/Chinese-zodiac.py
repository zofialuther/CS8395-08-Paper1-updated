from dataclasses import dataclass
from typing import List, Tuple
import numpy as np

@dataclass
class TraditionalStrings:
    ats: np.array
    ads: np.array
    aws: np.array
    axs: np.array
    ays: np.array

    def __init__(self):
        self.ats = np.array([("甲", "jiă"), ("乙", "yĭ"), ("丙", "bĭng"), ("丁", "dīng"), ("戊", "wù"), 
                             ("己", "jĭ"), ("庚", "gēng"), ("辛", "xīn"), ("壬", "rén"), ("癸", "gŭi")])

        self.ads = np.array([("子", "zĭ"), ("丑", "chŏu"), ("寅", "yín"), ("卯", "măo"), ("辰", "chén"), 
                             ("巳", "sì"), ("午", "wŭ"), ("未", "wèi"), ("申", "shēn"), ("酉", "yŏu"), 
                             ("戌", "xū"), ("亥", "hài")])

        self.aws = np.array([("木", "mù", "wood"), ("火", "huǒ", "fire"), ("土", "tǔ", "earth"), 
                             ("金", "jīn", "metal"), ("水", "shuǐ", "water")])

        self.axs = np.array([("鼠", "shǔ", "rat"), ("牛", "niú", "ox"), ("虎", "hǔ", "tiger"), 
                             ("兔", "tù", "rabbit"), ("龍", "lóng", "dragon"), ("蛇", "shé", "snake"), 
                             ("馬", "mǎ", "horse"), ("羊", "yáng", "goat"), ("猴", "hóu", "monkey"), 
                             ("鸡", "jī", "rooster"), ("狗", "gǒu", "dog"), ("豬", "zhū", "pig")])

        self.ays = np.array([("阳", "yáng"), ("阴", "yīn")])

def chars(s: str) -> List[str]:
    return [c for c in s]

def f生肖五行年份(y: int, traditional_strings: TraditionalStrings) -> List[List[str]]:
    i年份 = y - 4
    i天干 = i年份 % 10
    i地支 = i年份 % 12
    (h天干, p天干) = traditional_strings.ats[i天干]
    (h地支, p地支) = traditional_strings.ads[i地支]
    (h五行, p五行, e五行) = traditional_strings.aws[i天干 // 2]
    (h生肖, p生肖, e生肖) = traditional_strings.axs[i地支]
    (h阴阳, p阴阳) = traditional_strings.ays[i年份 % 2]

    return [[str(y), h天干 + h地支, h五行, h生肖, h阴阳],
            ["", p天干 + p地支, p五行, p生肖, p阴阳],
            ["", str(i年份 % 60 + 1) + "/60", e五行, e生肖, ""]]

def showYear(y: int, traditional_strings: TraditionalStrings) -> str:
    result = f生肖五行年份(y, traditional_strings)
    field_widths = [[6, 10, 7, 8, 3], [6, 11, 8, 8, 4], [6, 11, 8, 8, 4]]

    formatted_result = ""
    for i in range(len(field_widths)):
        formatted_line = ""
        for j in range(len(field_widths[i])):
            formatted_line += result[i][j].ljust(field_widths[i][j])
        formatted_result += formatted_line + "\n"

    return formatted_result

def main():
    traditional_strings = TraditionalStrings()
    years = [1935, 1938, 1968, 1972, 1976, 1984, 2017]
    for year in years:
        print(showYear(year, traditional_strings))

main()