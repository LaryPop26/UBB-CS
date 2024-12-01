;adunari-scaderi a,b,c,d word
; c-(a+d)+(b+d)

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
    b db 5
    c db 15
    d db 20

; our code starts here
segment code use32 class=code
    start:
        mov bl,[a]  ;bl => a = 10 = A(h)
        add bl,[d]  ;bl => a+d = 10 + 20 = 30 = 1E(h) 
        
        mov cl,[b]  ;cl => b = 5 = 5(h)
        add cl,[d]  ;cl => b+d = 5 + 20 = 25 = 19(h)
        
        mov al,[c]  ;al => c = 15 = F(h)
        sub al,bl   ;al => c - (a+d) = 15 - 30 = -15  = F1(h)
        add al,cl   ;al => c-(a+d)+(b+d) = -15 + 25 = 10 = A(h)
    
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
