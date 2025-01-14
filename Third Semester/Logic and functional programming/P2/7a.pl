/*
produs(Lista, Cifra, Rez) :-
    invers(Lista,Li),
    produs_aux(Li, Cifra, 0, Rezultat),
    invers(Rezultat,Rez).

invers(L,R):-
    invers_aux([],L,R).

invers_aux(Col,[],Col):-!.
invers_aux(Col,[H|T],R):-
    invers_aux([H|Col],T,R).

% Cazul de bază: când lista este goală, dacă există un transport rămas, îl adaugăm la rezultat
produs_aux([], _, 0, []).
produs_aux([], _, Transport, [Transport]) :- Transport > 0.

% Regula principală pentru înmulțire cifra cu cifra, luând în calcul transportul
produs_aux([H|T], Cifra, Transport, [RezC|RezTail]) :-
    Produs is H * Cifra + Transport,
    RezC is Produs mod 10,
    NouTransport is Produs // 10,
    produs_aux(T, Cifra, NouTransport, RezTail).
*/

produs([],[],_,0):-!.
produs([H|T],[C|R],Nr,Rest):-
    produs(T,R,Nr,Rez),
    C is (H*Nr+Rez) mod 10,
    Rest is (H*Nr+Rez) // 10.

add(Rez,R,[R|Rez]):-
    R=\=0,!.
add(Rez,_,Rez).


main(L,Nr,R):-
    produs(L,RP,Nr,Rest),
    add(RP,Rest,R).
