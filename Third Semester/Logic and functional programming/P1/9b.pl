/*
 *
 */
lista(M,N,[]):-M>N,!.
lista(M,N,[M|R]):-
    M=<N,NewM is M+1,
    lista(NewM,N,R),!.