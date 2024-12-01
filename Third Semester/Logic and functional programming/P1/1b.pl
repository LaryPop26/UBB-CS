/*
 * adaugaDupaPar(L:list,R:list)
 * model de flux: (i,o),(i,i)
 * L: lista in care se adauga val 1
 * R: lista rezultat
 * adaugaDupaPar(l1...ln)= [],n=0
 *                         l1 + 1 + adaugaDupaPar(l2...ln), l1 e par
 *                         l1 + adaugaDupaPar(l2...ln), altfel
 */
adaugaDupaPar([],[]):-!.
adaugaDupaPar([H|T],[H,1|R]):-
    H mod 2=:=0,!,
    adaugaDupaPar(T,R).
adaugaDupaPar([H|T],[H|R]):-
    adaugaDupaPar(T,R).

