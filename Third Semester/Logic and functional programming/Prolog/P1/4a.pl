/*
 *
 */

substituie([],_,_,[]).
substituie([H|T],E,L2,[L2|R]):-
    E=:=H,!,
    substituie(T,E,L2,R).
substituie([H|T],E,L2,[H|R]):-
    E=\=H,
    substituie(T,E,L2,R).


