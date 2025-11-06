;Se citesc din fisierul numere.txt mai multe numere (pozitive si negative). 
;Sa se creeze 2 siruri rezultat N si P astfel: N - doar numere negative si P - doar numere pozitive. 
;Afisati cele 2 siruri rezultate pe ecran.
bits 32
extern _printf
global _afisareASM
segment data public data use32
    format db "%d ",0
    
segment code public code use32
    _afisareASM:
        ;cod de intrare
        push EBP
        mov EBP,ESP
        
        ;se pune nr elem din vector in ecx
        mov ECX,[ESP+8]
        ;se pune adresa vectorului in esi
        mov ESI,[ESP+12]
        ;se incarca primul elem
        lodsd
        et1:
            lodsd ;se ia cate un elem 
            push ECX ;se protejeaza val din ecx
        
            ;printf("%d",EAX)
            push EAX
            push dword format
            call _printf
            add ESP,4*2
            
            pop ECX ;se restaureaza val din ecx
            
            loop et1

        mov EAX,0 ;se goleste eax
        
        ;cod de iesire
        mov ESP,EBP
        pop EBP
        ret