;Sa se citeasca un sir s1 (care contine doar litere mici). Folosind un alfabet (definit in segmentul de date), determinati si afisati sirul s2 obtinut prin substituirea fiecarei litere a sirului s1 cu litera corespunzatoare din alfabetul dat.
;Exemplu:
;Alfabetul: OPQRSTUVWXYZABCDEFGHIJKLMN
;Sirul s1:  anaaremere
;Sirul s2:  OBOOFSASFS
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,printf, scanf ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll 
import scanf msvcrt.dll

extern substituire
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s1 resb 100
    format dd "%s",0
    
    format1 dd "%s",0
    s2 resb 100
    
; our code starts here
segment code use32 class=code
    start:
        
        mov ebx,s1
        mov edi,s2
        
        push dword ebx
        push dword format
        call [scanf]
        add esp, 4*2
     
        call substituire
        
  
        push dword edi
        push dword format1
        call [printf]
        add esp, 4*2
    
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
