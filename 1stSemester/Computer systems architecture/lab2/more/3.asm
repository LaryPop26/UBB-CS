;adunari-scaderi a,b,c,d word
;(c+b+a)-(d+d)

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 1000
    b dw 1005
    c dw 2000
    d dw 1010
; our code starts here
segment code use32 class=code
    start:
        mov ax,[c] ;ax => c = 2000 = 07D0(h)
        add ax,[b] ;ax => c + b = 2000 + 1005 = 3005 = 0BBD(h)
        add ax,[a] ;ax => c + b + a = 2000 + 1005 + 1000 = 4005 = 0FA5(h)
        
        mov bx,[d] ;bx => d = 1010 = 03F2(h)
        add bx,[d] ;bx => d + d = 1010 + 1010 = 2020 = 07E4(h)
        
        sub ax,bx ; ax = ax - bx => (c+b+a)-(d+d) = 4005 - 2020 = 1985 = 07C1(h)
    
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
