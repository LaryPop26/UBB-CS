;adunari, scaderi - interpretare cu semn
;a - byte, b - word, c - double word, d - qword
;24. (a+b+c)-d+(b-c)
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 1
    b dw 10
    c dd 100
    d dq 1000

; our code starts here
segment code use32 class=code
    start:
        ;convertim cu semn byte a la dword
        mov al,[a]
        cbw
        cwde
        mov ebx,eax ; ebx = a
        
        ;convertim cu semn wordul b la dword
        mov ax,[b]
        cwde
        add ebx,eax ; ebx = a + b
        
        mov eax,[c]
        add eax,ebx ; eax = a + b + c
        
        ;convert rezultat la qword
        cdq ; edx:eax = a+b+c

        mov ebx,dword[d]
        mov ecx,dword[d+4]
        ;scadere (a+b+c) - d
        sub eax,ebx
        sbb edx,ecx     ;edx:eax = (a+b+c) - d
        
        mov ebx,eax
        mov ecx,edx     ;ecx:ebx = (a+b+c) - d
        ;realizam scaderea b - c
        ;convertim cu semmn wordul b la dword
        mov ax,[b]
        cwde
        sub eax,[c]    ; eax = b - c
        ;convertire cu semn de la dword la qword
        cdq     ;edx:eax = b -c
        
        ;adunare finala
        add ebx, eax
        adc ecx, edx    ; ecx:ebx = (a+b+c) - d + (b - c)        
        
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
