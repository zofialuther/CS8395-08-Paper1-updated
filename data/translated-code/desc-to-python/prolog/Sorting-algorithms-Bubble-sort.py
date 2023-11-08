def bubble_pass(List, SortedList) :-
    append([A,B|T], SortedList),
    (A =< B -> append([A|T], [B], NewList), bubble_pass(NewList, SortedList) ; SortedList = List).

bubble_sort(List, SortedList) :-
    bubble_pass(List, SortedList), !.

main :-
    List = [3, 2, 5, 1, 4],
    bubble_sort(List, SortedList),
    write(SortedList).