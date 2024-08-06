;de calculat: [(a+b)*2]/(a+d)
;a,b,c,d - byte e,f,g,h - word
;ex a=5, b=8, c=9, d=3 rez: [(5+8)*2]/(5+3) = (13 * 2) / 8 = 26 / 8 = 3 r 2
bits 32 ;asamblare si compilare pentru arhitectura de 32 biti
; definim punctul de intrare in programul principal
global  start 

extern  exit ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import  exit msvcrt.dll; exit este o functie care incheie procesul, este definita in msvcrt.dll
        ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante
segment  data use32 class=data ; segmentul de date in care se vor defini variabilele 
    a db 5
    b db 8
    c db 9
    d db 3
    
segment  code use32 class=code ; segmentul de cod
start: 
    mov cl, 2       ; cl = 2         2h
    mov al, byte[a] ; al = a         5 = 5h
    add al, byte[b] ; al = a+b       13 = Dh
    mul cl          ; ax = al * cl   26 = 1Ah
    mov bl, byte[a] ; bl = a         5h
    add bl, byte[d] ; bl = a+d       8 = 8h
    div bl          ; al = ax / bl   26 / 8 = 3 = 3h
                    ; ah = ax % cl   26 % 8 = 2 = 2h
    
    push   dword 0 ;se pune pe stiva codul de retur al functiei exit
	call   [exit] ;apelul functiei sistem exit pentru terminarea executiei programului	