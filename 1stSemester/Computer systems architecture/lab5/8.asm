bits 32 ; assembling for the 32 bits architecture
;Se da un sir de caractere S. 
;Sa se construiasca sirul D care sa contina toate literele mari din sirul S
;ex
;S: 'a', 'A', 'b', 'B', '2', '%', 'x', 'M'
;D: 'A', 'B', 'M'
; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data   
    s db 'a', 'A', 'b', 'B', '2', '%', 'x', 'M'
    len equ $-s
    d resb len

; our code starts here
segment code use32 class=code
    start:
        mov ecx,len
        mov esi,0
        mov edi,0
        jecxz final
        repeta:
            mov al,[s+esi] ; el curent
            
            ; verifica daca e litera mica sau mare
            cmp al,'A' 
            jnae final_repeta
            
            cmp al,'Z'
            jnbe final_repeta
            
            mov [d+edi],al
            inc edi
                        
            final_repeta:
            inc esi
            
        loop repeta
        
        final:
    
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
        
        
        ; cu instr lab 6
        ; mov ecx,len
        ; mov esi,0
        ; mov edi,0
        ; jecxz final
        ; repeta:
            ; lodsb ; el curent
            
            ; ; verifica daca e litera mica sau mare
            ; cmp al,'A' 
            ; jnae final_repeta
            
            ; cmp al,'Z'
            ; jnbe final_repeta
            
            ; stosb
                                    
            ; final_repeta:
            
            
        ; loop repeta
        
        ; final:
    
        ; ; exit(0)
        ; push dword 0      ; push the parameter for exit onto the stack
        ; call [exit]       ; call exit to terminate the program

