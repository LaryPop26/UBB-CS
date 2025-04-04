/*
 * elimina(E:integer,L:list, Rez:list)
 * model de flux:
 * E : el curent
 * L lista de transformat
 * R lista rezultat
 */
elimina(_,[],[]):-!.
elimina(E,[H|T],Rez):-
    E=:=H,!,
    elimina(E,T,Rez).
elimina(E,[H|T],[H|Rez]):-
    E=\=H,
    elimina(E,T,Rez).

/*
 * multime(L:list,R:list)
 * model de flux:
 * L: lista data
 * R: lista rezultat
 */
multime([],[]):-!.
multime([H|T],[H|R]):-
    elimina(H,T,R1),
    multime(R1,R).
