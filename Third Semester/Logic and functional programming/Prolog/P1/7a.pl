cauta([H|_],H):-!.
cauta([_|T],E):-
    cauta(T,E).


reuniune([],L2,L2).
reuniune([H|T],L2,R):-
    cauta(L2,H),!,
    reuniune(T,L2,R).
reuniune([H|T],L2,[H|R]):-
    reuniune(T,L2,R).


adauga(E,[],[E]).
adauga(E,[H|T],[E,H|T]):-
    E<H,!.
adauga(E,[H|T],[H|R]):-
    E>H,adauga(E,T,R).
adauga(E,[H|T],[H|T]):-
    E==H,!.

reunion([],L2,R):-
    reunion(L2,[],R).
reunion([H|T],L2,R):-
    reunion(T,L2,RezT),!,
    adauga(H,RezT,R).
