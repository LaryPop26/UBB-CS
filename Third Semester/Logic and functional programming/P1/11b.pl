suma([],_,0):-!.
suma([H|T],Poz,R):-
    Poz mod 2=:=0,
    NewPoz is Poz+1,
    suma(T,NewPoz,R1),
    R is R1+H,!.
suma([H|T],Poz,R):-
    Poz mod 2=:=1,
    NewPoz is Poz+1,
    suma(T,NewPoz,R1),
    R is R1-H,!.

sumaAlternanta(L,R):-
    suma(L,0,R).
