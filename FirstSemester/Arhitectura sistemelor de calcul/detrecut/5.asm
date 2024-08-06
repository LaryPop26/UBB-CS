;Se citesc 3 nr de la tastatura, sa se afiseze media aritmetica a celor 3 nr pe ecran.
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf            ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import scanf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dd 0
    b dd 1
    c dd 4
    format db "%d", 0
    message db "Introduceti un numar n: ", 0   
    message1 db "Media este: %d ",0

; our code starts here
segment code use32 class=code
start:
    push dword message  
    call [printf]       ; apelam functia printf pentru afisare
    add esp, 4*1      
    
    push dword a        
    push dword format
    call [scanf]        ; apelam functia scanf pentru citire
    add esp, 4 * 2  
    
    mov eax, [a]
    
    push dword message  
    call [printf]       
    add esp, 4*1        ; eliberam parametrii de pe stiva 
    
    push dword b        ; ! adresa lui n, nu valoarea
    push dword format
    call [scanf]        ; apelam functia scanf pentru citire
    add esp, 4 * 2  
    
    mov ebx,[b]
    
    push dword message  
    call [printf]       ; apelam functia printf pentru afisare
    add esp, 4*1        
    
    push dword c        
    push dword format
    call [scanf]        ; apelam functia scanf pentru citire
    add esp, 4 * 2  
    
    mov ecx,[c]
    
    add eax, ebx
    add eax, ecx
    
    cdq
    mov ebx,3
    idiv ebx
    
    push dword eax
    push dword message1  
    call [printf]       ; apelam functia printf pentru afisare
    add esp, 4*2        
    
    ; exit(0)
    push    dword 0      ; push the parameter for exit onto the stack
    call    [exit]       ; call exit to terminate the program
