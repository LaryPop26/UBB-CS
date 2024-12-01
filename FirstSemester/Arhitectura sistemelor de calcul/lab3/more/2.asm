;adunari, scaderi - interpretare fara semn
;a - byte, b - word, c - double word, d - qword
;24. ((a+b)+(a+c)+(b+c))-d

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
        mov al,[a]
        mov ah,0
        
        mov bx,[b]
        add ax, bx ; ax = a + b
        
        mov cx, 0
        
        push cx
        push ax
        pop eax     ; eax = a + b 
        
        push cx
        push bx
        pop ebx     ; ebx = b
        
        mov ecx,[c]
        add ebx,ecx ; ebx = b + c
        
        mov edx,eax ; edx = a + b
        
        mov al,[a]
        mov ah,0
        mov cx,0
        push cx
        push ax
        pop eax ; eax = a
        
        add eax,[c] ; eax = a + c
        
        add eax,edx
        add eax,ebx     ; eax = (a+b)+(a+c)+(b+c)
        
        mov edx,0
        
        sub eax,dword[d]
        sbb edx,dword[d+4]  ; edx:eax = (a+b)+(a+c)+(b+c) - d    
            
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
