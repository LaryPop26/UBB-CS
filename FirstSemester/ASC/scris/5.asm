bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db -2
    j db 3
    lj db $-j
    l db 5,5,6,7
    k db l-a,'m'-'a','m-a'
    la db $-a
    lg db $-lg
    b db 2
; our code starts here
segment code use32 class=code
    start:
        push edx
        push eax
        pop edx
        xor dh,dh
        shl edx, 16
        clc
        rcr edx,16
        add edx,ebx
        push edx
        pop esi
        lodsb
        pop edx
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
