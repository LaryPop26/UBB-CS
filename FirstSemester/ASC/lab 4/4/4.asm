;Se da octetul A. Sa se obtina numarul intreg n reprezentat de bitii 2-4 ai lui A. 
;Sa se obtina apoi in B octetul rezultat prin rotirea spre dreapta a lui A cu n pozitii. 
;Sa se obtina dublucuvantul C:
    ;bitii 8-15 ai lui C sunt 0
    ;bitii 16-23 ai lui C coincid cu bitii lui B
    ;bitii 24-31 ai lui C coincid cu bitii lui A
    ;bitii 0-7 ai lui C sunt 1

bits 32 ;assembling for the 32 bits architecture
global start

; we ask the assembler to give global visibility to the symbol called start 
;(the start label will be the entry point in the program) 
extern exit ; we inform the assembler that the exit symbol is foreign; it exists even if we won't be defining it
import exit msvcrt.dll  ; we specify the external library that defines the symbol
		; msvcrt.dll contains exit, printf and all the other important C-runtime functions

; our variables are declared here (the segment is called data) 
segment data use32 class=data
    a db 11001101b
    n db 0
    b db 0
    c dd 0

; the program code will be part of a segment called code
segment code use32 class=code
start:
    ;initializam registrii cu 0
    mov ebx,0
    mov dx,0
    
    mov al,[a] ;izolam bitii 2-4 ai lui a
    and al,00011100b 
    mov cl,2
    ror al,cl ; rotim spre dreapta 1 pozitie

    or dl,al
    mov [n],dl ; punem valoarea bitilor 2-4 in n 

    mov al,[a]
    mov cl,[n]
    ror al,cl ; rotim spre dreapta cu n pozitii
    or bl,al ; punem rezultatul in bl

    mov [b],bl ; punem valoarea in variabla b

    or bl,11111111b ; facem bitii 0-7 ai lui c 1
    or bh,00000000b ; facem bitii 8-15 ai lui c 0

    mov cl,[b] ; punem valoarea lui b in cl - pt a forma bitii 16-23 ai lui c
    mov ch,[a] ; punem valoarea lui a in ch - pt a forma bitii 24-31 ai lui c

    push cx
    push bx
    pop ebx ; ebx=dx:bx

    mov [c],ebx ; punem valoarea obtinuta in dublucuvantul c
    
	; call exit(0) ), 0 represents status code: SUCCESS
	push dword 0 ; saves on stack the parameter of the function exit
	call [exit] ; function exit is called in order to end the execution of the program