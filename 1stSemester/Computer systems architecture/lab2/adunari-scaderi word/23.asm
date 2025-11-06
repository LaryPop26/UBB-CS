;de calculat: (a+b+c)-(d+d)
;a,b,c,d - word
;ex a=260, b=320, c=935, d=567 rez: (260+320+935)-(567+567)= 1515 - 1134 = 381 = 17Dh
bits 32 ;asamblare si compilare pentru arhitectura de 32 biti
; definim punctul de intrare in programul principal
global  start 

extern  exit ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import  exit msvcrt.dll; exit este o functie care incheie procesul, este definita in msvcrt.dll
        ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante
segment  data use32 class=data ; segmentul de date in care se vor defini variabilele 
    a dw 260
    b dw 320
    c dw 935
    d dw 567
    
segment  code use32 class=code ; segmentul de cod
start: 
    mov ax,word[a] ; ax = a             260 = 104h
    add ax,word[b] ; ax = a+b           580 = 244h
    add ax,word[c] ; ax = a+b+c         1515 = 5EBh
    mov bx,word[d] ; bx = d             567 = 237h
    add bx,word[d] ; bx = d+d           1134 = 46Eh
    sub ax,bx      ; a = (a+b+c)-(d+d)  381 = 17Dh
    
    push   dword 0 ;se pune pe stiva codul de retur al functiei exit
	call   [exit] ;apelul functiei sistem exit pentru terminarea executiei programului	
    