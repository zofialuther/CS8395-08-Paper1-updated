lyrics(1, 'a partridge in a pear tree').
lyrics(2, 'two turtle doves').
lyrics(3, 'three french hens').
lyrics(4, 'four calling birds').
lyrics(5, 'five golden rings').
lyrics(6, 'six geese a-laying').
lyrics(7, 'seven swans a-swimming').
lyrics(8, 'eight maids a-milking').
lyrics(9, 'nine ladies dancing').
lyrics(10, 'ten lords a-leaping').
lyrics(11, 'eleven pipers piping').
lyrics(12, 'twelve drummers drumming').

gifts(1, 'a partridge in a pear tree').
gifts(2, 'two turtle doves').
gifts(3, 'three french hens').
gifts(4, 'four calling birds').
gifts(5, 'five golden rings').
gifts(6, 'six geese a-laying').
gifts(7, 'seven swans a-swimming').
gifts(8, 'eight maids a-milking').
gifts(9, 'nine ladies dancing').
gifts(10, 'ten lords a-leaping').
gifts(11, 'eleven pipers piping').
gifts(12, 'twelve drummers drumming').

writeLyrics(N) :-
    lyrics(N, L),
    write('On the '), write(N), write(' day of Christmas, my true love gave to me '), write(L), nl.

writeLoop(0).
writeLoop(N) :-
    N > 0,
    writeLyrics(N),
    M is N-1,
    writeLoop(M).

main :-
    writeLoop(12),
    halt.