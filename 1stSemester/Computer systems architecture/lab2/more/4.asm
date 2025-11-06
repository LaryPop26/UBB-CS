;inmultiri-impartiri a,b,c - byte, d - word
;((a+b-c)*2 + d-5)*d

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 5
    b db 20
    c db 15
    d dw 300

; our code starts here
segment code use32 class=code
    start:
        mov al,[a] ; al => a = 5 = 5(h)
        add al,[b] ; al => a + b = 5 + 20 = 25 = 19(h)
        sub al,[c] ; al => a + b - c = 5 + 20 - 15 = 10 = A(h)
        
        mov bl,2 ; bl => 2 = 2(h)
        mul bl   ; ax = al * bl => (a+b-c)*2 = 10 * 2 = 20 = 0014(h)
        
        add ax,[d] ; ax => (a+b-c)*2+d = 20 + 300 = 320 = 0140(h)
        
        mov bx,5  ; bx => 5 = 5(h)
        sub ax,bx ; ax = ax - bx => (a+b-c)*2+d-5 = 320 - 5 = 315 = 013B(h)
        
        mov bx,[d] ; bx => d = 300 = 012C(h)
        mul bx ; dx:ax = ax * bx => ((a+b-c)*2 + d-5)*d = 315 * 300 = 
        
        push dx ; salvam rezultatul pe stiva
        push ax
        pop eax ; eax = ((a+b-c)*2 + d-5)*d = 94500 = 00017124(h)
    
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
