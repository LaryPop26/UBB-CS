/*
 * Sa se calculeze cel mai mare divizor comun al elementelor unei liste.
 */

/*
 * cmmdc(x: element, y: element)
 * model de flux: (i,i,i) -
 * cmmdc(X, Y) = X , Y = 0 sau X = Y
 *               Y , X = 0
 *               cmmdc(X, Y-X), X < Y
 *               cmmdc(X-Y, Y), Y < X
 */

cmmdc(0, Y, Y) :- !.
cmmdc(X, 0, X) :- !.
cmmdc(X, Y, Div) :- X = Y, !, Div = X.
cmmdc(X, Y, Div) :- X < Y, !, Y1 is Y - X, cmmdc(X, Y1, Div).
cmmdc(X, Y, Div) :- X > Y, X1 is X - Y, cmmdc(X1, Y, Div).


/*
 * cmmdc_lista(List:list)
 * model de flux: (i,i) -
 *                (i,o) -
 * cmmdc_lista(l1...ln) = false, n = 0
 *                        l1 , n = 1
 *                        cmmdc_lista(el l3 ... ln), n > 1 ,
 *                        iar e = cmmdc(l1,l2)
 */
cmmdc_lista([H], H) :- !.
% Caz 1: lista are un el
cmmdc_lista([H1, H2 | T], Rez) :-
    cmmdc(H1, H2, RezIntermediar),
    % Calc CMMDC dintre primele două elemente
    cmmdc_lista([RezIntermediar | T], Rez).
    % Apel recursiv pe restul listei cu CMMDC-ul calculat
