/*suma_aux(L1, L2, Carry, Suma)
 *suma(L1,L2,Tr) = [], L1,L2 - goale, Tr = 0
 *                 [Tr], L1,L2 -goale, Tr > 0
 *                 suma(
 */
suma_aux([], [], 0, []):-!.
suma_aux([], [], Carry, [Carry]) :- Carry > 0,!.
suma_aux([], [H2|T2], Carry, [Suma|Rest]) :-
    Suma is H2 + Carry,
    Carry1 is Suma // 10,
    suma_aux([], T2, Carry1, Rest).
suma_aux([H1|T1], [], Carry, [Suma|Rest]) :-
    Suma is H1 + Carry,
    Carry1 is Suma // 10,
    suma_aux(T1, [], Carry1, Rest).
suma_aux([H1|T1], [H2|T2], Carry, [Suma|Rest]) :-
    Suma is H1 + H2 + Carry,
    Carry1 is Suma // 10,
    suma_aux(T1, T2, Carry1, Rest).

/*
 * suma(Lista1, Lista2, Suma)
 */
suma(L1, L2, S) :-
    suma_aux(L1, L2, 0, S).
