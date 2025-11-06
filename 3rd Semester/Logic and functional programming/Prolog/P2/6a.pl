/*
 *
 */

inloc([],_,_,[]).
inloc([E|T],E,L1,Rez):-
    inloc(T,E,L1,Rest),
    add(L1,Rest,Rez),!.
inloc([H|T],E,L1,[H|R]):-
    inloc(T,E,L1,R).

/*
 *
 */
add([],L,L).
add([H|T],L,[H|R]):-
    add(T,L,R).
