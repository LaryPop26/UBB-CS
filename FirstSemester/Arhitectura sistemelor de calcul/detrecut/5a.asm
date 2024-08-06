bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dd 1
    b dd 2
    c dd 3
    message1 db "Media este: %d ",0
    
; our code starts here
segment code use32 class=code
    start:
        mov eax,[a]
        add eax,[b]
        add eax,[c]
        
        cdq
        mov ebx,3
        idiv ebx
        
        push dword eax
        push dword message1  
        call [printf]       ; apelam functia printf pentru afisare
        add esp, 4*2        ; eliberam parametrii de pe stiva
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
