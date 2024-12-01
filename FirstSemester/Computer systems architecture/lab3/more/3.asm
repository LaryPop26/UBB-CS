;adunari, scaderi - interpretare cu semn
;a - byte, b - word, c - double word, d - qword
;10. b+c+d+a-(d+c)

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
        ;convert cu semn de la wordul b la qword
        mov ax,[b]
        cwde
        cdq     ;edx:eax = b
        
        mov ebx,eax
        mov ecx,edx ;ecx:ebx = b
        ;convert cu semn de la dwordul c la qword
        mov eax,[c]
        cdq     ;edx:eax = c
        ;adunam b+c
        add ebx,eax
        adc ecx,edx ;ecx:ebx = b+c
        ;salvam qword d in registrii
        mov eax,dword[d]
        mov edx,dword[d+4];edx:eax = d
        ;calc b+c+d
        add ebx,eax
        adc ecx,edx ;ecx:ebx = b+c+d
        ;convert cu semn de la byteul a la qword
        mov al,[a]
        cbw
        cwde
        cdq ;edx:eax = a
        
        add ebx,eax
        adc ecx,edx ;ecx:ebx = b+c+d+a
        ;calc d+c
        ;;convert cu semn de la dwordul c la qword
        mov eax,[c]
        cdq ;edx:eax = c
        
        add eax,dword[d]
        adc edx,dword[d+4] ; edx:eax = c+d
        ;rez final
        sub ebx,eax
        sbb ecx,edx ;ecx:ebx = b+c+d+a-(d+c)
                    
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
