% Predicate pentru a verifica dacă un element există în lista curentă
exista(H, [H|_]).
exista(H, [_|T]) :- exista(H, T).

% Predicate pentru a elimina dublurile dintr-o listă
elimina_dubluri([], []):-!.
elimina_dubluri([H|T], [H|Rez]) :-
    \+ exista(H, T),!,  % Verifică dacă H nu este în T
    elimina_dubluri(T, Rez).
elimina_dubluri([H|T], Rez) :-
    exista(H, T),!,      % Dacă H este în T, îl ignorăm
    elimina_dubluri(T, Rez).

% Predicate pentru a sorta o listă
sortare(Lista, Sortata) :-
    elimina_dubluri(Lista, FaraDubluri),
    sort(FaraDubluri, Sortata).
