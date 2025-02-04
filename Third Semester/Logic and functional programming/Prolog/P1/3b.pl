/*
 *
 */

creare([],[[],[]],0,0).
creare([H|T],[[H|LPare],LImp],NrPare1,NrImp):-
    H mod 2=:=0,!,
    creare(T,[LPare,LImp],NrPare,NrImp),
    NrPare1 is NrPare+1.
creare([H|T],[LPare,[H|LImp]],NrPare,NrImp1):-
       H mod 2=:=1,
       creare(T,[LPare,LImp],NrPare,NrImp),
       NrImp1 is NrImp+1.
/*
main(List,[LPare,LImp],NrPare,NrImp):-
    creare(List,LPare,LImp,NrPare,NrImp).
*/
