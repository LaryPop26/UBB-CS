/*
secventa([],[],[]):-!.
secventa([H],[H],[H]):-!.
secventa([L1,L2],[L1,L2],[]):-
    L1=<L2,!.
secventa([L1,L2|T],[L1],[L2|T]):-
    L1>=L2,!.

secventa([L1,L2,L3|T],[L1|R],Rest):-
    L1<L2,
    L2<L3,!,
    secventa([L2,L3|T],R,Rest).
secventa([L1,L2,L3|T],[L1,L2],[L3|T]):-
    L1<L2,
    L2>=L3,!.

determin([],[]):-!.
determin(List,[S|Rez]):-
    secventa(List,S,Rest),
    determin(Rest,Rez).

len([],0):-!.
len([H|T],Nr):-
    len(T,Nr1),
    Nr is Nr1+1.


max([],M,M,L,L):-!.
max([H|T],M,Rez,L,RL):-
    len(H,LH),
    LH>L,!,
    max(T,H,Rez,LH,RL).
max([_|T],M,Rez,L,RL):-
    max(T,M,Rez,L,RL).

det_max([H|T],Rez):-
    determin([H|T],Liste),
    max(Liste,[],Rez,0,_).
*/

% Verificăm dacă un număr este par
par(X) :-
    X mod 2 =:= 0.

% Găsim secvența de numere pare consecutive din listă
secventa_pare([H|T], [H|Secventa]) :-
    par(H),
    secventa_pare(T, Secventa).
secventa_pare([H|T], Secventa) :-
    \+ par(H),
    secventa_pare(T, Secventa).
secventa_pare([], []).

% Determinăm lungimea unei secvențe
lungime([], 0).
lungime([_|T], L) :-
    lungime(T, L1),
    L is L1 + 1.

% Comparăm lungimea secvențelor
cea_mai_lunga_secventa([Secventa|T], CeaMaiLungaSecventa) :-
    cea_mai_lunga_secventa(T, Secventa, CeaMaiLungaSecventa).
cea_mai_lunga_secventa([], CeaMaiLungaSecventa, CeaMaiLungaSecventa).
cea_mai_lunga_secventa([Secventa|T], SecventaCurenta, CeaMaiLungaSecventa) :-
    lungime(Secventa, L1),
    lungime(SecventaCurenta, L2),
    L1 > L2,
    cea_mai_lunga_secventa(T, Secventa, CeaMaiLungaSecventa).
cea_mai_lunga_secventa([Secventa|T], SecventaCurenta, CeaMaiLungaSecventa) :-
    lungime(Secventa, L1),
    lungime(SecventaCurenta, L2),
    L1 =< L2,
    cea_mai_lunga_secventa(T, SecventaCurenta, CeaMaiLungaSecventa).

% Găsim toate secvențele de numere pare consecutive
toate_secventele_pare([], []).
toate_secventele_pare([H|T], [Secventa|Secvente]) :-
    par(H),
    secventa_pare([H|T], Secventa),
    toate_secventele_pare(T, Secvente).
toate_secventele_pare([H|T], Secvente) :-
    \+ par(H),
    toate_secventele_pare(T, Secvente).

% Rezolvare finală: găsim cea mai lungă secvență de numere pare
cea_mai_lunga_secventa_pare(Lista, CeaMaiLungaSecventa) :-
    toate_secventele_pare(Lista, Secventele),
    cea_mai_lunga_secventa(Secventele, CeaMaiLungaSecventa).
