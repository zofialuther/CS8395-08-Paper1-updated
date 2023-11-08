colors([red, green, blue, black, white]) :-
    foreach(member(Color, [red, green, blue, black, white]), 
        (writeln(Color), true)
    ).