/*
 *
 */

eliminare([],_,[],0):-!.
eliminare([H|T],E,R,Nr):-
    H=:=E,
    eliminare(T,E,R,Nr1),!,
    Nr is Nr1+1.
eliminare([H|T],E,[H|R],Nr):-
    eliminare(T,E,R,Nr).

/*
 *
 */
listaPerechi([],[]).
listaPerechi([H|T],[RezP|Rez]):-
    eliminare([H|T],H,Rez1,Nr),
    RezP=[H,Nr],
    listaPerechi(Rez1,Rez).

/*
 *
 */
numar(L,R):-
    listaPerechi(L,R).
