/*
 *
 */

elimina([],_,[],_).
elimina([H|T],E,R,Nr):-
    H=:=E, Nr<3,!,
    Nr1 is Nr+1,
    elimina(T,H,R,Nr1).
elimina([H|T],E,[H|R],Nr):-
    H=:=E, Nr>3,!,
    Nr1 is Nr+1,
    elimina(T,H,R,Nr1).
elimina([H|T],E,[H|R],Nr):-
    elimina(T,E,R,Nr).

/*
 *
 */
elim(L,E,R):-
    elimina(L,E,R,0).
