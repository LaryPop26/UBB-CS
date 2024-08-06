;Se da dublucuvantul A. Sa se obtina numarul intreg n reprezentat de bitii 14-17 ai lui A. 
;Sa se obtina apoi in B dublucuvantul rezultat prin rotirea spre stanga a lui A cu n pozitii. Sa se obtina apoi octet C astfel:
    ;bitii 0-5 ai lui C coincid cu bitii 1-6 ai lui B
    ;bitii 6-7 ai lui C coincid cu bitii 17-18 ai lui B
bits 32 ;assembling for the 32 bits architecture
global start

; we ask the assembler to give global visibility to the symbol called start 
;(the start label will be the entry point in the program) 
extern exit ; we inform the assembler that the exit symbol is foreign; it exists even if we won't be defining it
import exit msvcrt.dll  ; we specify the external library that defines the symbol
		; msvcrt.dll contains exit, printf and all the other important C-runtime functions

; our variables are declared here (the segment is called data) 
segment data use32 class=data
    a dd 11110111111010001001110110100011b
    n db 0
    b dd 0
    c db 0
; the program code will be part of a segment called code
segment code use32 class=code
start:
    ;initializam registrii cu 0
    mov ebx,0
    mov dx,0

    mov eax,[a] ; izolam bitii 14-17 ai lui a
    and eax,00000000000000111100000000000000b
    mov cl,14
    ror eax,cl ; rotim 14 pozitii spre dreapta

    or dl,al
    mov [n],dl ; punem valoarea in variabila n

    mov eax,[a]
    mov cl,[n]
    rol eax,cl ; rotim n pozitii spre stanga
    or ebx,eax ; punem rezultatul in ebx

    mov [b],ebx ; punem valoarea in variabila b
 
    mov eax,[b] ; izolam bitii 1-6 ai lui b
    and eax,00000000000000000000000001111110b
    mov cl,1
    ror eax,cl ; rotim 1 pozitie spre dreapta 

    mov ebx,0 ; in registrul bx vom calcula rezultatul(c)
    or ebx,eax ; punem bitii in rezultat

    mov eax,[b] ; izolam bitii 17-18 ai lui b
    and eax,00000000000001100000000000000000b
    mov cl,11
    ror eax,cl ; rotim 11 pozitii spre dreapta
    or ebx,eax ; punem bitii in rezultat

    mov [c],bx ; punem valoarea in variabila c
 
	; call exit(0) ), 0 represents status code: SUCCESS
	push dword 0 ; saves on stack the parameter of the function exit
	call [exit] ; function exit is called in order to end the execution of the program