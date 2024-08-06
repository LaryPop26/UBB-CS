bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a1 db 0,1,2,'xyz'
    db 300,"F"+3
    a2 times 3 db 44h
    a3 times 11 db 5,1,3
    a4 dw a2+1,'bc'
    
    a44 dw 2009h
    a5 dd a2+1,'bcd'
    a6 times 4 db '13'
    a61 times 4 dw '13'
    ;a7 db a2
    a8 dw a2
    a9 dd a2
    a10 dq a2
    ; a11 db [a2]
    ; a12 dw [a2]
    ; a13 dd dword[a2]
    ; a14 dq [a2]
    ; a15 dd eax
    ; a20 dd [eax]
    
    
; our code starts here
segment code use32 class=code
    start:
        
        MOV al,-5
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
