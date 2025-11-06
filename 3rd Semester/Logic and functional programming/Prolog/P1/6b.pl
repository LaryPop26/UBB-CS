/*
 *
 */
max([],M,M).
max([H|T],M,R):-
    H>M,!,
    max(T,H,R).
max([H|T],M,R):-
    H=<M,
    max(T,M,R).

/*
 *
 */
elimMax([],_,[]).
elimMax([H|T],E,R):-
    H==E,!,elimMax(T,E,R).
elimMax([H|T],E,[H|R]):-
    H \= E, elimMax(T,E,R).

/*
 *
 */
main(L,R):-
    max(L,0,M),
    elimMax(L,M,R).
