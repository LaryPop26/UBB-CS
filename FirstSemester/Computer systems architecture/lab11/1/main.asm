;Se da un numar a reprezentat pe 32 biti fara semn. Se cere sa se afiseze reprezentarea in baza 16 a lui a, precum si rezultatul permutarilor circulare ale cifrelor sale.
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,printf             ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
extern permutare
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    numar dd 1234567890
    format db "Numarul in hex: %X",10, 0
    
; our code starts here
segment code use32 class=code
   start:
    ; Afisare reprezentare initiala    
    push dword [numar]
    push dword format
    call [printf]
    add esp, 4*2 ; Curățare argumente din stivă
   
    push dword [numar]
    call permutare
    call permutare
    call permutare    

    ; exit(0)
    push dword 0      ; push the parameter for exit onto the stack
    call [exit]       ; call exit to terminate the program