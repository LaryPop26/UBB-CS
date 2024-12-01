multimiEgale([],[]):-!.
multimiEgale(L1,L2):-
    incluse(L1,L2),
    incluse(L2,L1).

incluse([],_).
incluse([H|T],L2):-
    cauta(H,L2),
    incluse(T,L2),!.

cauta(E,[E|_]).
cauta(E,[_|T]):-
    cauta(E,T).

% vezi caz cu el repetate.
