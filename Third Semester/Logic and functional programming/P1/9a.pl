/*
 *
 */

cauta([H|_],H):-!.
cauta([_|T],E):-
    cauta(T,E).


intersectie([],_,[]).
intersectie([H|T],L2,R):-
    not(cauta(L2,H)),!,
    intersectie(T,L2,R).
intersectie([H|T],L2,[H|R]):-
    intersectie(T,L2,R).