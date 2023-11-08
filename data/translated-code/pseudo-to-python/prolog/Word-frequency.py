import re

def print_top_words(File, N):
    String = open(File, 'r', encoding='utf-8').read()
    Words = re.split("\\w+", String)
    Lower = lower_case(Words)
    Sorted = sorted(Lower)
    Counted = merge_words(Sorted)
    Top_words = sorted(Counted, key=lambda x: x[1], reverse=True)
    print(f"Top {N} words:\nRank\tCount\tWord")
    print_top_words(Top_words, N, 1)

def lower_case(Words):
    if len(Words) == 0:
        return []
    else:
        return [(word.lower(), 1) for word in Words]

def merge_words(Words):
    if len(Words) == 0:
        return []
    elif len(Words) == 1:
        return Words
    else:
        Word1, Count1 = Words[0]
        Word2, Count2 = Words[1]
        NewCount = Count1 + Count2
        NewWord = Word1
        return merge_words([(NewWord, NewCount)] + Words[2:])

def print_top_words(Words, N, R):
    if len(Words) == 0 or N == 0:
        return
    else:
        Word, Count = Words[0]
        print(f"{R}\t{Count}\t{Word}")
        print_top_words(Words[1:], N-1, R+1)

print_top_words("135-0.txt", 10)