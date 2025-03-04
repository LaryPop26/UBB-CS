/*
 * cmmdc(X:integer, Y:integer, D:integer)
 * model de flux:
 * X: primul numar pt calcul cmmdc
 * Y: al 2-lea nr pt calcul cmmdc
 * D: rezultatul cmmdc
 */

cmmdc(0,Y,Y):-!.
cmmdc(X,0,X):-!.
cmmdc(X,Y,D):-
    X = Y,!,D = X.
cmmdc(X,Y,D):-
    X < Y,!,Y1 is Y-X,cmmdc(X,Y1,D).
cmmdc(X,Y,D):-
    X>Y,X1 is X-Y,cmmdc(X1,Y,D).
/*
 * cmmmc(X:integer, Y:integer, M:integer)
 * model de flux:
 * X: primul numar pt calcul cmmmc
 * Y: al 2-lea nr pt calcul cmmmc
 * M: rezultatul cmmmc
 */

cmmmc(X,Y,M):-
    cmmdc(X,Y,D),
    M is (X*Y)//D.

/*
 * cmmmcLista(L: list, Rez: Integer)
 * model de flux
 * L: lista pt care se calculeaza cmmmc
 * Rez: cmmmc al liste
 */
cmmmcLista([],1):-!.
cmmmcLista([H|T],Rez):-
    cmmmcLista(T,R),
    cmmmc(H,R,Rez).

