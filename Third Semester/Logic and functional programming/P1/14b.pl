elementulN([],_,_,0):-!.
elementulN([_|T],Poz,PozC,R):-
    Poz\=PozC,!,
    NewPozC is PozC+1,
    elementulN(T,Poz,NewPozC,R).
elementulN([H|_],Poz,PozC,H):-
    Poz==PozC,!.

element(L,P,R):-
    elementulN(L,P,1,R).

% unde trebuie taieturaaaaaaa