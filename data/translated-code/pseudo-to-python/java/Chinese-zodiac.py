animals = ["Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Goat","Monkey","Rooster","Dog","Pig"]
elements = ["Wood","Fire","Earth","Metal","Water"]
animalChars = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
elementChars = [["甲","丙","戊","庚","壬"],["乙","丁","己","辛","癸"]]

def getYY(year):
    if year % 2 == 0:
        return "yang"
    else:
        return "yin"

def main():
    years = [1935,1938,1968,1972,1976,1984,1985,2017]
    for i in range(len(years)):
        print(str(years[i])+" is the year of the "+elements[(years[i]-4)%10//2]+" "+animals[(years[i]-4)%12]+" ("+getYY(years[i])+"). "+elementChars[years[i]%2][(years[i]-4)%10//2]+animalChars[(years[i]-4)%12])

main()