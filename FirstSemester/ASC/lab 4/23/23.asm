;Se da octetul A si cuvantul B. Sa se formeze dublucuvantul C:
    ;bitii 24-31 ai lui C sunt bitii lui A
    ;bitii 16-23 ai lui C sunt inversul bitilor din octetul cel mai putin semnificativ al lui B
    ;bitii 10-15 ai lui C sunt 1
    ;bitii 2-9 ai lui C sunt bitii din octetul cel mai semnificativ al lui B
    ;bitii 0-1 se completeaza cu valoarea bitului de semn al lui A

bits 32 ;assembling for the 32 bits architecture
global start

; we ask the assembler to give global visibility to the symbol called start 
;(the start label will be the entry point in the program) 
extern exit ; we inform the assembler that the exit symbol is foreign; it exists even if we won't be defining it
import exit msvcrt.dll  ; we specify the external library that defines the symbol
		; msvcrt.dll contains exit, printf and all the other important C-runtime functions

; our variables are declared here (the segment is called data) 
segment data use32 class=data
    a db 10011001b
    b dw 1101100001100110b
    c dd 0
; the program code will be part of a segment called code
segment code use32 class=code
start:
    ;initializam registrii cu 0
    mov ebx,0 ; in registrul ebx vom calcula rezultatul
    mov dx,0

    mov eax,0
    mov al,[a] ; izolam bitul 7 al lui a
    and al,10000000b
    mov cl,1
    sar al,cl ; shiftare 1 pozitie spre dreapta
    mov cl,2
    rol al,cl ; rotim 2 pozitii spre stanga

    or ebx,eax ; punem bitii in ebx

    mov eax,0
    mov ax,[b] ; izolam bitii 9-15 ai lui b 
    and ax,1111111100000000b
    mov cl,10
    rol ax,cl ; rotim 10 pozitii spre stanga

    or ebx,eax ; punem bitii in ebx

    or bx,1111110000000000b ; facem biti 10-15 din rezultat sa aiba valoarea 1
 
    mov ax,[b] ;negam bitii 0-14 ai lui b 
    not ax
    and ax,0000000011111111b ; izolam bitii 0-14 ai lui b 
    or dx,ax ; punem bitii in dx

    mov ax,[a] 
    mov cl,8 
    shl ax,cl ; mutam bitii lui a de pe pozitiile 0-7 pe 8-15

    or dx,ax ; punem bitii in dx

    push dx
    push bx
    pop ebx ; ebx = dx:bx

    mov [c],ebx ; punem valoarea din registru in variabila rezultat

	; call exit(0) ), 0 represents status code: SUCCESS
	push dword 0 ; saves on stack the parameter of the function exit
	call [exit] ; function exit is called in order to end the execution of the program