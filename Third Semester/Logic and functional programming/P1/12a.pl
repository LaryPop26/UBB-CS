/*
 *
 */
substituie([],_,_,[]):-!.
substituie([H|T],E1,E2,[E2|R]):-
    E1==H,!,
    substituie(T,E1,E2,R).
substituie([H|T],E1,E2,[H|R]):-
    E1\=H,!,
    substituie(T,E1,E2,R).

