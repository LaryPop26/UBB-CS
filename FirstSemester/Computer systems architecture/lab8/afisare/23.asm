;Sa se citeasca de la tastatura un numar hexazecimal format din 2 cifre. 
;Sa se afiseze pe ecran acest numar in baza 10, interpretat atat ca numar fara semn cat si ca numar cu semn (pe 8 biti).
bits 32
global start

extern exit, printf, scanf
import exit msvcrt.dll
import printf msvcrt.dll    
import scanf msvcrt.dll

segment data use32 class=data
    n dd 0
    message db "Introduceti un numar n: ", 0                            ;n =  FF
    format db "%x", 0
    format2 db "Numarul in reprezentarea cu semn este: %d",10, 0        ;=> -1
   
    format3 db "Numarul in reprezentarea fara semn este: %u",10, 0      ;=> 255
    

segment code use32 class=code
start:
    push dword message  ; ! pe stiva se pune adresa string-ului, nu valoarea
    call [printf]       ; apelam functia printf pentru afisare
    add esp, 4*1        ; eliberam parametrii de pe stiva ; 4 = dimensiunea unui dword; 1 = nr de parametri
                                                   
    ; vom apela scanf(format, n) => se va citi un numar in variabila n
    ; punem parametrii pe stiva de la dreapta la stanga
    push dword n        ; ! adresa lui n, nu valoarea
    push dword format
    call [scanf]        ; apelam functia scanf pentru citire
    add esp, 4 * 2      ; eliberam parametrii de pe stiva
                       
    mov eax,[n]         ; punem valoarea citita in eax
    
    pushad              ; salvam valorile din registrii
    
    
    or eax,11111111111111111111111100000000b ; facem complementul pt reprezentarea cu semn
    
    aici:
    push dword eax
    push dword format2
    call [printf]
    add esp, 4*2        ; afisare nr cu semn
    popad               ; revenim la valorile de dinaintea printf
    
    pushad              ; salvam valorile din registrii
    push dword eax
    push dword format3
    call [printf]
    add esp, 4*2        ; afisare nr fara semn
    popad               ; revenim la valorile de dinaintea printf
    
    push dword 0 
	call [exit]         ; se incheie programul