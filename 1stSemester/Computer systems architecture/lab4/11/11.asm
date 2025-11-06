;Se dau un octet A si un cuvant B. 
;Sa se obtina un octet C care are pe bitii 0-3 bitii 2-5 ai lui A, iar pe bitii 4-7 bitii 6-9 ai lui B.
bits 32 ;assembling for the 32 bits architecture
global start

; we ask the assembler to give global visibility to the symbol called start 
;(the start label will be the entry point in the program) 
extern exit ; we inform the assembler that the exit symbol is foreign; it exists even if we won't be defining it
import exit msvcrt.dll  ; we specify the external library that defines the symbol
		; msvcrt.dll contains exit, printf and all the other important C-runtime functions

; our variables are declared here (the segment is called data) 
segment data use32 class=data
    a dw 01001110b
    b dw 1110010110001100b
    c db 0
; the program code will be part of a segment called code
segment code use32 class=code
start:
    ;facem registrii 0 
    mov ebx,0

    mov al,[a] ; izolam bitii 2-5 ai lui a
    and al,00111100b
    mov cl,2
    ror al,cl ; rotim 2 pozitii spre dreapta

    mov dl,al ; punem rezultatul in dl 

    mov ax,[b] ; izolam bitii 6-9 ai lui b
    and ax,0000001111000000b
    mov cl,2
    ror ax,cl ; rotim 2 pozitii spre dreapta

    or bl,dl ; punem bitii pt pozitiile 0-3 in rezultat
    or bl,al ; punem bitii pt pozitiile 4-7 in rezultat

    mov [c],bl ; punem rezultatul in variabila c

	; call exit(0) ), 0 represents status code: SUCCESS
	push dword 0 ; saves on stack the parameter of the function exit
	call [exit] ; function exit is called in order to end the execution of the program