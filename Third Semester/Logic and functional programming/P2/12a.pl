inlocuire([],_,_,[]).
inlocuire([H|T],H,E2,[E2|R]):-
   !,inlocuire(T,H,E2,R).
inlocuire([H|T],E,E2,[H|R]):-
    H\= E,
    inlocuire(T,E,E2,R).