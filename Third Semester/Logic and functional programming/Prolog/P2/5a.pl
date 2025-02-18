% Predicatul principal pentru a găsi toate pozițiile elementului maxim.
poz(L, P) :-
    maxim(L, Max),
    find_positions(L, Max, 1, P).

% Predicatul pentru a găsi elementul maxim într-o listă.
maxim([X], X).
maxim([H|T], Max) :-
    maxim(T, MaxTail),            % Recursively find the maximum of the tail.
    (H > MaxTail -> Max = H;    % If the head is greater than the tail maximum, H is the new maximum.
     Max = MaxTail),!.
% Predicatul auxiliar care găsește toate pozițiile unui element Max într-o listă.
find_positions([], _, _, []):-!.
find_positions([H|T], Max, Pos, [Pos|P]) :-
    H =:= Max,
    NextPos is Pos + 1, !,
    find_positions(T, Max, NextPos, P).
find_positions([_|T], Max, Pos, P) :-
    NextPos is Pos + 1,
    find_positions(T, Max, NextPos, P).
