/*
 *
 */

nrAparitii([],_,0).
nrAparitii([H|T],E,R):-
    E=H,!,nrAparitii(T,E,R1),R is R1+1.
nrAparitii([H|T],E,R):-
    E\=H,!,nrAparitii(T,E,R).

/*
 *
 */
elimina([],_,[]).
elimina([H|T],C,R):-
    nrAparitii(C,H,A),A=<1,!,
    elimina(T,C,R1),R=[H|R1].
elimina([_|T],C,R):-
    elimina(T,C,R).

/*
 *
 */
elim(L,R):-
    elimina(L,L,R).
