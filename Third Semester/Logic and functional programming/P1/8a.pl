/*
 *
 */

nrAparitii([],_,0).
nrAparitii([H|T],E,R):-
    E=H,!,nrAparitii(T,E,R1),R is R1+1.
nrAparitii([H|T],E,R):-
    E\=H,nrAparitii(T,E,R).

multime([]).
multime([H|T]):-
    nrAparitii([H|T],H,Nr), Nr = 1, multime(T).

