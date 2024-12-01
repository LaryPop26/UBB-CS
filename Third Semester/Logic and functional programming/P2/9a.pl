/*
 * elimina(L:lista,F:intreg,R:Lista)
 * model de flux: (i,i,o) - det,(i,i,i)
 * L: lista in care se elimina elemente consecutive
 * F: flag ce indica daca suntem intr-o secventa de el consecutive
 * R: lista rezultat
 */

elimina([],_,[]).
elimina([_],1,[]).
elimina([H],0,[H]).
elimina([H1,H2|T],_,R):-
    H1=:=H2-1,
    elimina([H2|T],1,R).
elimina([H1,H2|T],1,R):-
    H1=\=H2-1,
    elimina([H2|T],0,R).
elimina([H1,H2|T],0,R):-
    H1=\=H2-1,
    elimina([H2|T],0,R1),
    R=[H1|R1].

/*
 * eliminaConsecutive(L:lista,R:lista)
 * model de flux: (i,o) - det,(i,i)
 * L: lista in care se cauta elemente consecutive
 * R: lista rezultat
 */
eliminaConsecutive(L,R):-elimina(L,0,R).
