;inmultiri, impartiri - interpretare fara semn
;a,c - byte, b - word, d - doubleword, x - qword
;10. d-(7-a*b+c)/a-6+x/2
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
    c db 5
    d dd 100
    x dq 1000

; our code starts here
segment code use32 class=code
    start:
        mov al,[a]
        mov ah,0
        
        mul word[b] ; dx:ax = a*b
        
        push dx
        push ax
        pop eax ; eax = a*b
        
        mov ebx,7
        sub ebx,eax ; ebx = 7 - a*b
        
        mov al,[c]
        mov ah,0
        mov dx,0
        
        push dx
        push ax
        pop eax ; eax = c
        
        add ebx,eax ; ebx = 7 - a*b + c
        
        push ebx
        pop ax
        pop dx  ;dx:ax = 7 - a*b + c
        
        mov bl,[a]
        mov bh, 0   ; bx = a
        
        div bx  ; ax = (7 - a*b + c) / a   
                ; dx = (7 - a*b + c) % a 

        mov dx,0
        push dx
        push ax
        pop eax ; eax = (7 - a*b + c)/a   
        
        mov ebx,[d] ; ebx = d 
        mov ecx, 6 ; ecx = 6
        
        sub ebx, eax    ; ebx = d-(7-a*b+c)/a
        sub ebx, ecx ; ebx = d-(7-a*b+c)/a-6
        
        mov eax,dword[x]
        mov edx,dword[x+4] ; edx:eax = x
        
        mov ecx,2
        div ecx ; eax = x/2 + edx = x%2
        
        mov ecx,0
        
        add eax,ebx
        adc edx,ecx ; edx:eax = d-(7-a*b+c)/a-6+x/2
        
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
