%precedent(List:List,Rest:Int,List:List)
%List-> lista de prelucrat
%Rest-> avand scaderi avem situatii cand trebuie  sa retinem un rest pentru al scade din op
%Result-> lista rezultata . precedentul listei
%daca am ajuns la sf de lista ret lista vida
%model de flux: (i,o,o) , (i,i,i)
precedent([],_,[]):-!.
%daca sunt la sf listei si ultima cifra este 0
%aici setam restul la 1 si ultima cifra va fi 9
precedent([0],1,[9]):-!.
%altfel ultima cifra devine ultima cifra-1
precedent([H],0,[NewH]):-
    NewH is H-1,!.
%daca avem restul 1 si cifra curenta este 0 continuam cu
%restul 1 si la result adaug la inceput 9
precedent([0|T],1,[9|Result]):-
    precedent(T,1,Result),
    !.
%altfel noua cifra de adaugat e l1-Rest
precedent([H|T],0,[NewH|Result]):-
    precedent(T,NewR,Result),
    !,
    NewH is H-NewR.
