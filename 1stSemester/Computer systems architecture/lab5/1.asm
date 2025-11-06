; Se da un sir de octeti S de lungime l. 
; Sa se construiasca sirul D de lungime l-1 astfel incat elementele din D sa reprezinte 
; produsul dintre fiecare 2 elemente consecutive S(i) si S(i+1) din S.
; Ex. 
; S: 1, 2, 3, 4
; D: 2, 6, 12
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        
; declare external functions needed by our program
extern exit           ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s db 1,2,3,4 ;declarare sir
    len equ $-s ;stabilire lungime sir 
    d times len-1 db 0 ;rezervare spatiu de dimensiune len-1 pt sirul destinatie si initializarea sa 
    ;d resb len-1
; our code starts here
segment code use32 class=code
    start:
        mov ecx,len-1 ;punem (lungimea sirului s)-1 in ecx pt a realiza bucla
        mov esi,0 ; index pt sirul s
        mov edi,0 ; index pt sirul d
        jecxz Sfarsit ; jump in caz ca sirul e initializat gol
        repeat:
                mov al,[s+esi] ; punem prima valoare in al
                mov bl,[s+esi+1] ; punem urmatoarea valoare din sir in bl
                mul bl ; realizam inmultirea elementelor de pe 2 pozitii consecutive
                mov [d+edi],al ; salvam rezultatul in sirul d pe pozitia corecta
                inc esi ; crestem indexul pt s
                inc edi ; crestem indexul pt d
        loop repeat ; bucla pt a parcurge intreg sirul
        Sfarsit: ;terminarea programului
        
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
