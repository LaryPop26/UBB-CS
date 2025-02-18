succesor_aux([9],[0],1):-!.
succesor_aux([H],[Nr],0):-
    Nr is H+1,!.
succesor_aux([H|T],[C|R],Rest):-
    succesor_aux(T,R,R1),
    C is (H+R1) mod 10,
    Rest is (H+R1)//10.

add(0,R,R):-!.
add(N,R,[N|R]).

succesor(L,R):-
    succesor_aux(L,RP,Rest),
    add(Rest,RP,R).
