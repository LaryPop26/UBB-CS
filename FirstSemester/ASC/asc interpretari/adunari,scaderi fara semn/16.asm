;de calculat: c-a-(b+a)+c
;a - byte, b - word, c - double word, d - qword - Interpretare fara semn
;2655674 - 10 - (2510 + 10) + 2655674 = 2655674 - 10 - 2520 + 2655674 = 5308818

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
    b dw 2510
    c dd 2655674

; our code starts here
segment code use32 class=code
    start:
        mov al,byte[a]      ;al = a                                 10
        mov ah,0            ;conversie fara semn de la al la ax
        add ax,word[b]      ;ax=a+b                                 2520
 
        mov bx,ax           ;bx=b+a                                 2520
        mov cx,0            ;conversie fara semn de la bx la cx:bx 
                            ;cx:bx=b+a                              2520
        push cx
        push bx
        pop ebx             ;conversie prin stiva de la word la dword
                            ;ebx=b+a                                2520
        
        mov al,byte[a]      ;al = a                                 10
        mov ah,0            ;conversie fara semn de la al la ax
        mov cx,ax           ;cx = a 
        mov dx,0            ;dx:cx = a                 
        
        push dx
        push cx
        pop ecx             ;conversie prin stiva de la word la dword
                            ;ecx = a                                10
         
        mov eax,dword[c]    ;eax = c                                2655674 
        sub eax,ecx         ;eax = c - a                            2655664
        sub eax,ebx         ;eax = c - a - (b + a)                  2653144
        add eax,dword[c]    ;eax = c - a - (b + a) + c              5308818
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
        