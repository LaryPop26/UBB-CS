interclasare([],[],[]):-!.
interclasare([H|T1],[],[H|R]):-!,
    interclasare(T1,[],R).
interclasare([],[H|T2],[H|R]):-!,
    interclasare([],T2,R).
interclasare([H1|T1],[H2|T2],[H1|R]):-
    H1<H2,!,
    interclasare(T1,[H2|T2],R).
interclasare([H1|T1],[H2|T2],[H2|R]):-
    H2<H1,!,
    interclasare([H1|T1],T2,R).
interclasare([H|T1],[H|T2],[H|R]):-
    interclasare(T1,T2,R).

% fuck taietura