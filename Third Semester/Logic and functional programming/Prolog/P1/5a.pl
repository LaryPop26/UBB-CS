/*
 *
 */

eliminaElement([],_,[]):-!.
eliminaElement([H|T],E,[H|R]):-
    H\=E,!,
    eliminaElement(T,E,R).
eliminaElement([_|T],E,R):-
    eliminaElement(T,E,R).
