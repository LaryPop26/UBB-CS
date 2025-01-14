/*
 diff(a, b) =
	b - a, a < b
	a - b, a > b

 diff(A:nr, B:nr, R:nr)
 model de flux (i, i, o)
 A: primul nr din lista
 B: al 2-lea nr din lista
 R: diferenta dintre cele 2 numere
*/

diff(A, B, R) :-
    A < B, R is B - A.
diff(A, B, R) :-
    A > B, R is A - B.

/*
 check(l1...ln, m) =
	true, diff(l1, l2) >= m and n = 2
	check(l2...ln, m), diff(l1, l2) >= m and n > 2
	false, altfel

 check(L:list, M:integer)
 model de flux: (i, i)
 L: lista de verificat
 M: diferenta minima intre numerele generate
*/
check([H1, H2], M):-
    diff(H1, H2, RD),
    RD >= M, !.
check([H1, H2|T], M) :-
    diff(H1, H2, RD),
    RD >= M,
    check([H2|T], M).

/*
 sequences(n, i) =
	1. [], i = n + 1
	2. i + sequences(n, i + 1), i <= n
	3. sequences(n, i + 1), i <= n

 sequences(N:integer, I:integer, R:list)
 model de flux: (i, i, o) - nedet
 N: numarul maxim pana la care se genereaza lista
 I: nr de la care incepe secventa
 R: lista generata
*/
sequences(N, I, []) :-
    I =:= N + 1, !.
sequences(N, I, [I|R]) :-
    I =< N,
    NI is I + 1,
    sequences(N, NI, R).
sequences(N, I, R) :-
    I =< N,
    NI is I + 1,
    sequences(N, NI, R).

/*
 onesolution(n,m,r)=
             sequences(N,1,R), check(R,M).
 onesolution(N:number, M:number, R:list)
 model de flux: (i, i, o) - nedeterminist
 N: numarul maxim pana la care se genereaza lista
 M: diferenta minima dintre 2 numere din lista
 R: lista generata
*/
onesolution(N, M, R) :-
    sequences(N, 1, R),
    check(R, M).

/*
 allsolutions(N:number, M:number, R:list)
 model de flux: (i, i, o)
 N: numarul maxim pana la care se genereaza lista
 M: diferenta minima dintre 2 numere din lista
 R: lista generata

*/
allsolutions(N, M, R) :-
    findall(RPartial, onesolution(N, M, RPartial), R).
% permutari etc
