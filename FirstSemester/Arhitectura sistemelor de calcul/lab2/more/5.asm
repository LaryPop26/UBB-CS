;inmultiri-impartiri a,b,c,d-byte, e,f,g,h-word
;((a-b)*4)/c

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 10
    b db 6
    c db 5

; our code starts here
segment code use32 class=code
    start:
        mov al,[a] ; al => a = 10 = A(h)
        sub al,[b] ; al => a - b = 10 - 6 = 4 = 4(h)
        
        mov bl,4 ; bl => 4 = 4(h)
        mul bl    ; ax = al*bl => 4 * 4 = 16 = 10(h)
        
        mov bl,[c] ; bl => c = 5 = 5(h)
        div bl ; al = ax / bl => 16 / 5 = 3 = 3(h)
               ; ah = ax % bl => 16 % 5 = 1 = 1(h)
    
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
