;de calculat: (8-ab100+c)/d+x
;a,b,d-byte; c-doubleword; x-qword
;(8-1020100+2655674)/30 + 1073741456 = (8 - 20000 + 2655674) / 30 + 1073741456 = 
;2653682 / 30 + 1073741456 = 87856 + 1073741456 = 1073829312

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
    b db 20
    c dd 2655674
    d db 30
    x dq 1073741456

; our code starts here
segment code use32 class=code
    start:
        
        mov al,100              ;al=100
        mul byte[a]             ;ax=al*a=100*a
        mov bl,byte[b]
        mov bh,0                ;bx=b
        mul bx                  ;dx:ax=ax*bx=100*a*b
        
        push dx
        push ax
        pop eax                 ;eax=100*a*b
        mov ebx,eax             ;ebx=100*a*b

        mov eax,8               ;eax=8
        sub eax,ebx             ;eax=eax-ebx=8-100*a*b
        add eax,dword[c]        ;eax=8-100*a*b+c
        mov edx,0               ;edx:eax=8-100*a*b+c

        mov bl,byte[d]
        mov bh,0                ;bx=d
        mov cx,0                ;cx:bx=d
        push cx
        push bx 
        pop ebx                 ;ebx=d
        div ebx                 ;eax=edx:eax / ebx = (8-100*a*b+c)/d
                                ;edx=edx:eax % ebx = (8-100*a*b+c)%d
        mov edx,0
        add eax,dword[x]
        adc edx,dword[x+4]      ;edx:eax = (8-100*a*b+c)/d + x
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program