;Se dau doua siruri de caractere S1 si S2. 
;Sa se construiasca sirul D prin concatenarea elementelor sirului S2 
;in ordine inversa cu elementele de pe pozitiile pare din sirul S1.
;S1: '+', '2', '2', 'b', '8', '6', 'X', '8'
;S2: 'a', '4', '5'
;D: '5', '4', 'a', '2','b', '6', '8'
bits 32 ;assembling for the 32 bits architecture
global start

; we ask the assembler to give global visibility to the symbol called start 
;(the start label will be the entry point in the program) 
extern exit ; we inform the assembler that the exit symbol is foreign; it exists even if we won't be defining it
import exit msvcrt.dll  ; we specify the external library that defines the symbol
		; msvcrt.dll contains exit, printf and all the other important C-runtime functions

; our variables are declared here (the segment is called data) 
segment data use32 class=data
    s1 db '+', '2', '2', 'b', '8', '6', 'X', '8'
	len1 equ $-s1
    s2 db 'a', '4', '5'
	len2 equ $-s2
	lend equ $-s1
	d times lend db 0

; the program code will be part of a segment called code
segment code use32 class=code
start:
	mov ecx,len2 ;pregatim registrul pt parcurgere
	mov esi,len2 ;initializam registrul indice cu lungimea S2
	dec esi ;decrementam indicele la care ne aflam
	mov edi,len2
	jecxz pozitii_pare ;tratam cazul in care ecx e 0
	repeta:
		mov al,[s2+esi] ;punem in al elementul curent
		mov [d+edi],al ;punem elementul in sirul rezultat
		dec esi ;decrementam indicele la care ne aflam
		inc edi ;incrementam indicele din sirul rezultat
	loop repeta
	
pozitii_pare:
	mov ecx,len1 ;pregatim registrul pt parcurgere
	mov esi,0 ;initializam registrul indice cu 0
	inc esi ;incrementam registrul indice pt a parcurge pozitiile pare din sir
	jecxz final
	repeta2:
		mov al,[s1+esi] ;punem in al elementul curent de pe pozitia para
		mov [d+edi],al ;punem elementul in sirul rezultat
		inc esi
		inc esi ;incrementam de 2 ori registrul indice pt a ramane pe pozitii pare
		inc edi ;incrementam indicele din sirul rezultat
	loop repeta2

final:

	; call exit(0) ), 0 represents status code: SUCCESS
	push dword 0 ; saves on stack the parameter of the function exit
	call [exit] ; function exit is called in order to end the execution of the program