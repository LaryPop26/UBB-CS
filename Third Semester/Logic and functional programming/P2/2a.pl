% insert(Element, ListaSortata, ListaNoua) - predicat care inserează un element în lista sortată.
insert(X, [], [X]):-!.  % Inserăm în lista goală.
insert(X, [Y|T], [X,Y|T]) :-
    X =< Y,!.  % Dacă X este mai mic sau egal decât Y, X devine capul listei.
insert(X, [Y|T], [Y|Sorted]) :-
    X > Y,  % Dacă X este mai mare decât Y, continuăm inserția în restul listei.
    insert(X, T, Sorted).

% sortare(Lista, ListaSortata) - predicat care sortează o listă păstrând dublurile.
sortare([], []).  % Caz de bază: lista goală este deja sortată.
sortare([H|T], Sorted) :-
    sortare(T, SortedT),  % Sortăm restul listei.
    insert(H, SortedT, Sorted).  % Inserăm elementul în lista sortată.
