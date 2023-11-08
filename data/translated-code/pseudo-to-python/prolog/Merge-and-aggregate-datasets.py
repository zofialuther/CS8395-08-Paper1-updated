def Load_CSV(filename, data_type):
    # code to load CSV file

def Is_nan(Number):
    X = Number
    return X != Number

def SummaryDates(Id, Lastname, LastDate):
    LastDateNumber = BagMax(Date_number(Id))
    Lastname = Patient(Id, Lastname)
    Y, M, D, _, _, _ = Julian_date(LastDateNumber)
    LastDate = Date_converter(date(Y, M, D))

def SummaryScores(Id, Lastname, Sum, Mean):
    Sum = BagSum(Scores(Id))
    Count = BagCount(Scores(Id))
    Mean = Sum / Count
    Lastname = Patient(Id, Lastname)

def Test():
    SummaryDates(Id, Lastname, LastDate)
    print("summaryDates(Id,Lastname,LastDate)")
    fail()

def Test():
    SummaryScores(Id, Lastname, ScoreSum, ScoreMean)
    print("summaryScores(Id,Lastname,ScoreSum,ScoreMean)")
    fail()

def Date_number(Id):
    Number = Visit(Id, date(Y, M, D), _)
    Y, M, D, _, _, _ = Julian_date(Number)

def Scores(Id):
    Score = Visit(Id, _, Score)
    return not Is_nan(Score)