sublista([],_,_,_,[]):-!.
sublista([H|T],PozI,PozF,PozC,[H|R]):-
    PozI=<PozC,
    PozC=<PozF,
    NewPozC is PozC+1,
    sublista(T,PozI,PozF,NewPozC,R),!.
sublista([_|T],PozI,PozF,PozC,R):-
    (PozC < PozI ; PozC > PozF),
    NewPozC is PozC+1,
    sublista(T,PozI,PozF,NewPozC,R),!.


sublistaMain(L,PozI,PozF,R):-
    sublista(L,PozI,PozF,0,R).