;de calculat: 256*1
;a - word
;a = 256 , b = 1 rez: 256 * 1 = 256

bits 32 ;asamblare si compilare pentru arhitectura de 32 biti
; definim punctul de intrare in programul principal
global  start 

extern  exit ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import  exit msvcrt.dll; exit este o functie care incheie procesul, este definita in msvcrt.dll
        ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante
segment  data use32 class=data ; segmentul de date in care se vor defini variabilele 
    a dw 256
    b db 1
    
segment  code use32 class=code ; segmentul de cod
start: 
    mov ax,[b]  ; ax = b           1 = 1h
    mul word[a] ; dx:ax = ax * a   256 = 100h
    
    push   dword 0 ;se pune pe stiva codul de retur al functiei exit
	call   [exit] ;apelul functiei sistem exit pentru terminarea executiei programului	
   