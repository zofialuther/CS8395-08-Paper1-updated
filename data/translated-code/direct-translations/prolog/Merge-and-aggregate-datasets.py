from aggregs import bagMax, bagCount, bagSum, bagReduce
from iso8601 import julian_date, date_string
from proc_files import load_csv, add_cvt_type_hook

add_cvt_type_hook('date', 'date_converter(_,_)')

def date_converter(Atom, Date):
    return date_string('YYYY-MM-DD', Date, Atom)

load_csv('visit.csv', 'visit(integer,date,float)')
load_csv('patient.csv', 'patient(integer,atom)')

def is_nan(Number):
    X = Number
    return X != Number

def summaryDates(Id, Lastname, LastDate):
    LastDateNumber = bagMax(date_number(Id))
    Lastname = patient(Id, Lastname)
    Y, M, D, _, _, _ = julian_date(LastDateNumber)
    LastDate = date_converter(LastDate, date(Y, M, D))

def summaryScores(Id, Lastname, Sum, Mean):
    Sum = bagSum(scores(Id))
    Count = bagCount(scores(Id))
    Mean = Sum / Count
    Lastname = patient(Id, Lastname)

def test():
    summaryDates(Id, Lastname, LastDate)
    print(f'summaryDates({Id}, {Lastname}, {LastDate})')

def test2():
    summaryScores(Id, Lastname, ScoreSum, ScoreMean)
    print(f'summaryScores({Id}, {Lastname}, {ScoreSum}, {ScoreMean})')

def date_number(Id, Number):
    Y, M, D = visit(Id)
    return julian_date(Number, Y, M, D, _, _, _)

def scores(Id, Score):
    _, Score = visit(Id)
    return not is_nan(Score)

def maximum(X, Y, Z):
    if X > Y:
        return Z == X
    else:
        return Z == Y

def sum(X, Y, Z):
    return Z == X + Y

def successor(X, Y, Z):
    return Z == X + 1