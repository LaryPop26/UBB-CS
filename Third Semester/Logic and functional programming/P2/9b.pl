/*
 * elimina(L:lista,F:intreg,R:Lista)
 * model de flux: (i,i,o) - det,(i,i,i)
 * L: lista in care se cauta elemente consecutive
 * F: flag ce indica daca elementul curent si urmatorul sunt consecutive
 * R: lista rezultat
 */

elimina([],_,[]).
elimina([_],1,[]).
elimina([H],0,[H]).
elimina([H1,H2|T],_,R):-
    H1=:=H2-1,elimina([H2|T],1,R).
elimina([H1,H2|T],1,R):-
    H1=\=H2-1,elimina([H2|T],0,R).
elimina([H1,H2|T],0,R):-
    H1=\=H2-1,elimina([H2|T],0,R1),R=[H1|R1].

/*
 * eliminaSublista(L:lista,R:lista)
 * model de flux: (i,o) - det, (i,i)
 * L: lista in care se cauta subliste cu el elemente consecutive
 * R: lista rezultat
 */

eliminaConsecutiveSublista([],[]).
eliminaConsecutiveSublista([H|T],R):-
                is_list(H),elimina(H,0,RH),eliminaConsecutiveSublista(T,RT),R=[RH|RT].
eliminaConsecutiveSublista([H|T],R):-
                \+ is_list(H),eliminaConsecutiveSublista(T,RT),R=[H|RT].
