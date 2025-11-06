bits 32 ; assembling for the 32 bits architecture
; Se da un sir de cuvinte. Sa se obtina din acesta un sir de dublucuvinte, in care fiecare dublucuvant 
; va contine nibble-urile despachetate pe octet (fiecare cifra hexa va fi precedata de un 0), 
; aranjate crescator in interiorul dublucuvantului.
; exemplu
; pentru sirul initial: 1432h, 8675h, 0ADBCh, ...
; Se va obtine: 01020304h,  05060708h, 0A0B0C0Dh, ... 
; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s dw 1432h, 8675h, 0ADBCh
    len equ ($-s)/2
    r times len dd 0

; our code starts here
segment code use32 class=code
    start:
        mov ecx,len
        mov esi,s
        mov edi,r
        jecxz final
        
        repeta:
            lodsw   ;stocam primul cuvant din sir in ax
            
            ; facem in eax forma finala a dublucuvintelor ( eax = 0x0y0z0t ,unde x,y,z,t - cifre hexa)
            mov bx,ax   ;stocam cuvantul si in bx pentru zerorizari 
            
            and al,0FH  ; al - primul nibble
            shr bl,4    ; bl - al 2 lea nibble
            and ah,0FH  ; ah - al 3 lea nibble
            shr bh,4    ; bh - al 4 lea nibble
            
            ; sortam nibble-urile crescator
            mov edx,3   ; edx - contor pentru nr repetari bucla sortare
            
            ; bubble sort pt sortarea crescatoare a nibble-urilor
            sortare:
            
                cmp ah, al
                jg swap01
                jmp no_swap01
            swap01:
                xchg ah, al          
            no_swap01:

                cmp al, bh
                jg swap12
                jmp no_swap12
            swap12:
                xchg al, bh          
            no_swap12:

                cmp bh, bl
                jg swap23
                jmp no_swap23
            swap23:
                xchg bh, bl          
            no_swap23:
                
                dec edx
                jnz sortare
           
            
            shl eax,16  ; mutam partea low din eax in partea high
            mov ax,bx   ; punem in partea low a lui eax restul nibble-urilor
                        ; astfel in eax se afla dublucuvantul format si ordonat crescator

            stosd
                
            loop repeta
        
        final:
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
