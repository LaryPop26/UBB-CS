/*
 * Sa se scrie un predicat care transforma o lista intr-o multime,
 * in ordinea ultimei aparitii.
 * Exemplu: [1,2,3,1,2] e transformat in [3,1,2].
 */

 /*
 * gasit(e:element, List:list)
 * model de flux: (i,i) -
 * gasit(e,l1 ... ln) = True, l1 e elem cautat
 *                      False, l e vida
 *                      gasit(e, l2 ... ln), altfel
 */
gasit(E,[H|_]):-
    H=E,!.
gasit(E,[_|T]):-
    gasit(E,T).
/*
 * cauta(List:list, Rez: list)
 * model de flux:(i,o) -
 *               (i,i) -
 * cauta(l1...ln) = [], n = 0
 *                  l1 + cauta(l2...ln), l1 nu mai e in lista mai
 *                  departe
 *                  cauta(l2 ... ln), altfel
 */
cauta([],[]):-!.
% caz 1: lista e goala
cauta([H|T],[H|Rez]):-
    cauta(T,Rez),
    not(gasit(H,Rez)),!.
% caz 2: H - el curent, T restul listei
%        daca se reapeleaza recursiv, iar daca el nu s-a mai
%        gasit in lista, este adaugat in Rez
cauta([_|T],Rez):-
    cauta(T,Rez).
%caz 3: altfel

/*
 * multime(Lisr:list, RezP: list)
 * model de flux: (i,o) -
 *                (i,i) -
 * multime(list) = [], lista e goala
 *                 cauta(list), altfel
 */
multime([],[]):-!.
%caz 1: lista e goala
multime(List,RezP):-
     cauta(List,RezP).
% caz 2: se apeleaza recursiv cauta(l,r)
