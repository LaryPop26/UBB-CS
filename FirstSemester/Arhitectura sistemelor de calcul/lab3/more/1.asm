;adunari, scaderi - interpretare fara semn
;a - byte, b - word, c - double word, d - qword
;10. (a+d+d)-c+(b+b)

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
    b dw 300
    c dd 500
    d dq 1000

; our code starts here
segment code use32 class=code
    start:
        ;calculam a + d+ d
        ;convertim byte ul a la qword
        mov al,[a]  ;
        mov ah, 0   ;conversie fara semn de la al la ax
        mov bx, 0   ;conversie fara semn de la ax la bx:ax
                    ;bx:ax = a

        push bx
        push ax
        pop eax     ;conversie de la bx:ax la eax
                    ;eax = a

        mov ebx, 0
        mov ecx, dword[d]   ;salvam partea inferioara din qwordul d in ecx
        mov edx, dword[d+4] ;salvam partea superioara din qwordul d in edx

        add eax, ecx    ;adunam a+d
        adc ebx, edx    ;rezultatul final va fi stocat in ebx:eax

        add eax, ecx    ;adunam a+d+d
        adc ebx, edx    ;rezultatul final va fi stocat in ebx:eax

        ;calculam (a+d+d)-c
        ;convertim doublewordul c la qword
        mov ecx, [c]
        mov edx, 0 ;la final in edx:ecx = c

        sub eax,ecx     ;scadere (a+d+d)-c
        sbb ebx,edx     ;rezultatul final stocat in ebx:eax 

        ;calculam b + b
        mov cx,[b]
        add cx,[b]      ;cx = b+b

        ;convertim wordul cx la qword
        mov dx,0
        push dx
        push cx
        pop ecx

        mov edx,0       ;acum edx:ecx = b+b

        ;calculam (a+d+d)-c+(b+b)
        add eax,ecx
        adc ebx,edx

        ;rezultatul final stocat in ebx:eax      
            
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
