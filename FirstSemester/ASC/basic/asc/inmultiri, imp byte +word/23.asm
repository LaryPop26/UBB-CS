;de calculat: [(a+b)*3-c*2]+d
;a,b,c - byte d - word
;ex a=5, b=8, c=9, d=265 rez: [( 5 + 8 ) * 3 - 9 * 2 ] + 265 = (13 * 3 - 18) + 265 = 39 - 18 + 265 =  21 + 265 = 286 = 11Eh
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
    d dw 265
    
segment  code use32 class=code ; segmentul de cod
start: 
    mov al,byte[a] ; al = a             5 = 5h
    add al,byte[b] ; al = a+b           13 = Dh
    mov dl, 3      ; dl = 3             3 = 3h
    mul dl         ; ax = al * dl       39 = 27h
    mov bx,ax      ; bx = ax            27h
    mov cl, 2      ; cl = 2             2 = 2h
    mov al,byte[c] ; al = c             9 = 9h
    mul cl         ; ax = al * cl       18 = 12h
    mov dx,ax      ; dx = ax            12h
    mov ax, bx     ; ax = bx            27h
    sub ax, dx     ; ax = ax - dx       21 = 15h
    mov dx,word[d] ; dx = d             265 = 109h
    add ax, dx     ; ax = ax + dx       286 = 11Eh
    
    push   dword 0 ;se pune pe stiva codul de retur al functiei exit
	call   [exit] ;apelul functiei sistem exit pentru terminarea executiei programului	