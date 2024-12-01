divizibil(N,D):-
    D*D<N,!,
    D1 is D+2,
    divizibil(N,D1).


divizibil(N,D):-
    D*D<N,
    N mod D =:=0,!.

prim_m(2):-!.
prim_m(N):-
    N>2,
    N mod 2 =\=0,
    not(divizibil(N,3)).

duplic_prim([],[]):-!.
duplic_prim([H|T],[H,H|Rez]):-
    prim_m(H),!,
    duplic_prim(T,Rez).
duplic_prim([H|T],[H|Rez]):-
    \+ prim_m(H),
    duplic_prim(T,Rez).
