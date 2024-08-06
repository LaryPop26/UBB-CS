;de calculat: (a-c)+(b+b+d)
;a,b,c,d - byte
;ex a=7, b=8, c=5, d=9 rez: (7-5)+(8+8+9)= 2+25 = 27
bits 32 ;asamblare si compilare pentru arhitectura de 32 biti
; definim punctul de intrare in programul principal
global  start 

extern  exit ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import  exit msvcrt.dll; exit este o functie care incheie procesul, este definita in msvcrt.dll
        ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante
segment  data use32 class=data ; segmentul de date in care se vor defini variabilele 
    a db 7
    b db 8
    c db 5
    d db 9
    
segment  code use32 class=code ; segmentul de cod
start: 
    mov al,byte[a] ; al = a             7
    sub al,byte[c] ; al = a-c           2
    mov ah,byte[b] ; ah = b             8 
    add ah,byte[b] ; ah = b+b           16
    add ah,byte[d] ; ah = b+b+d         25
    add al,ah      ; al = (a-c)+(b+b+d) 27
    
    push   dword 0 ;se pune pe stiva codul de retur al functiei exit
	call   [exit] ;apelul functiei sistem exit pentru terminarea executiei programului	
   