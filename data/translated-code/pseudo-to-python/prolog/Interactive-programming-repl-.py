import win_menu
import swi_hooks

print("The graphical front-end will be used for subsequent tracing")

LoadFile("c:/users/joel-seven/appdata/roaming/swi-prolog/pl.ini")

print("XPCE 6.6.66, July 2009 for Win32: NT,2000,XP")
print("Copyright (C) 1993-2009 University of Amsterdam.")
print("XPCE comes with ABSOLUTELY NO WARRANTY. This is free software,")
print("and you are welcome to redistribute it under certain conditions.")
print("The host-language is SWI-Prolog version 5.10.0")

print("For HELP on prolog, please type help. or apropos(topic).")
print("on xpce, please type manpce.")

AssertPredicate(f(A, B, C), format('~w~w~w~w~n', [A, C, C, B]))

QueryPredicate(f('Rosetta', 'Code', ':'))