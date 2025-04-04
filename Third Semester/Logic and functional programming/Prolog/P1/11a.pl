creste([_]).
creste([H1,H2|T]):-
    H1<H2,
    creste([H2|T]).

scadere([_]).
scadere([H1,H2|T]):-
    H1>H2,
    scadere([H2|T]).


scade([_]).
scade([H1,H2|T]):-
    H1>H2,
    scade([H2|T]).
scade([H1,H2|T]):-
    H1=<H2,
    creste([H2|T]).

vale(L):-
    not(creste(L)),
    not(scadere(L)),
    scade(L),!.
