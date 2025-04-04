/*
 * gasit(E:element,L:list)
 * model de flux: (i,i)
 * gasit(E,L)= true, el e in lista
 *             false, altfel
 *
 */

gasit(E,[H|_]):-
    H=:=E,!.
gasit(E,[_|T]):-
    gasit(E,T).
/*
 *  A = {1,3,4,5,7}
 *  B = {1,7,8}
 *  A \ B = {3,4,5}
 *  diferentaMultimi(a1...an,b1...bm)=
 *      [],n = 0
 *      a1 + diferentaMultimi(a2...an,b1...bm), a1 nu e in B
 *      diferentaMultimi(a2...an,b1...bm), a1 e in B
 */

diferentaMultimi([],_,[]):-!.
diferentaMultimi([H|T],B,[H|R]):-
    \+ gasit(H,B),!,
    diferentaMultimi(T,B,R).
diferentaMultimi([_|T],B,R):-
    diferentaMultimi(T,B,R).
