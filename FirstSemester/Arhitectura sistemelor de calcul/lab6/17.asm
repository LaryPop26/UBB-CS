bits 32 ; assembling for the 32 bits architecture
; Se da un sir de dublucuvinte. Sa se ordoneze descrescator sirul cuvintelor inferioare ale acestor dublucuvinte. 
; Cuvintele superioare raman neschimbate.
; exeplu
; dandu-se: sir DD 12345678h 1256ABCDh, 12AB4344h
; rezultatul va fi 1234ABCDh, 12565678h, 12AB4344h.
; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s dd 12345678h, 1256ABCDh, 12AB4344h
    len equ ($-s)/4
    r times len dw 0
    rez times len dd 0

; our code starts here
segment code use32 class=code
  
start:
        mov ecx, len      
        mov esi, s        
        mov edi, rez   
        jecxz final
        
        cld
        
        ; extrag partea high a dublucuvintelor si le salvez pe pozitiile corecte
        higher:
            lodsd
            and eax,0FFFF0000H
            stosd
            loop higher
        ; rez va arata astfel: 12340000h, 12560000h, 12AB0000h
        
        mov ecx, len      
        mov esi, s        
        mov edi, r        
        
        ; extrag partea low a dublucuvintelor pentru a le sorta
        ; vor fi salvate in sirul intermediar r
        lower:
            lodsd                 ; load dword from [esi] into eax
            stosw                 ; store ax into [edi]
            loop lower      ; repeat for all elements
        ; pt exemplu, r arata astfel:
        ; r: 5678H, ABCDH, 4344H         
        
        ;sortare bubble sort
        mov edx,len
        oloop:
            mov ecx, len
            dec ecx
            mov esi,r
            mov edi,r
            
            iloop:
                lodsw
                mov bx,[esi]
               
                cmp ax,bx
                jb skip
                xchg ax,bx
                              
                skip:
                    shl eax,16
                    mov ax,bx
                    stosd
                    dec edi
                    dec edi
                    loop iloop
        dec edx
        jnz oloop
                  
        ; aici r este sortat descrescator
        ; r: ABCDh, 5678h, 4344h
        
        ; construim sirul final
        mov ecx,len
        mov esi,r
        mov edi,rez
        
        rezultat:
            movsw
            add edi,2
            loop rezultat
        ; acum in rez va fi sirul: 1234ABCDh, 12565678h, 12AB4344h
        
        final:
        
        ; Exit the program
        push dword 0          ; push exit code
        call [exit]           ; call the exit function to terminate the program
