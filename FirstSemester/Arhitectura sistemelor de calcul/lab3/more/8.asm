;inmultiri, impartiri - interpretare cu semn
;a,c - byte, b - word, d - doubleword, x - qword
;24. a - (7+x)/(b*b-c/d+2)
; ;))) ai luat gresit tipurile
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
    c db 50
    d dd 100
    x dq 1000

; our code starts here
segment code use32 class=code
    start:
        mov ax,[b]
        imul word[b] ; dx:ax = b*b
        
        push dx
        push ax
        pop ecx ; ecx = b*b
        
        mov al,[c]
        cbw
        cwde ; eax = c
        cdq  ; edx:eax = c
        
        mov ebx,[d]
        idiv ebx ; eax = c/d iar edx = c%d
        
        mov edx,2
        
        sub ecx,eax ; ecx = b*b-c/d
        sub ecx,edx ; ecx = b*b-c/d-2
        
        push ecx
        
        mov eax,dword[x]
        mov edx,dword[x+4] ; edx:eax = x
        
        mov ebx,7
        mov ecx,0
        add eax,ebx ; edx:eax = 7+x
        adc edx,ecx ; ???
        
        pop ecx
        
        idiv ecx ; eax = (7+x)/(b*b-c/d+2)
                 ; edx = (7+x)%(b*b-c/d+2)
                
        mov ebx,eax
        
        mov al,[a]
        cbw
        cwde ; ebx = a
        
        sub eax,ebx ; eax = a-(7+x)/(b*b-c/d+2)
    
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
