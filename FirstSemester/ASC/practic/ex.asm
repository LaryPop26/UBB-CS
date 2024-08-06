bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, fread, fopen, fclose             ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    nume db "a.txt", 0
    mod_f db "r", 0
    
    descriptor_f dd -1
    
    format db "Am citit %d caractere.Textul este: %s", 0
    len db 100
    text times 101 db 0

; our code starts here
segment code use32 class=code
    start:
        push dword mod_f
        push dword nume
        call [fopen]
        add esp, 4* 2
        
        mov [descriptor_f],eax
        
        cmp eax,0
        je final
        
        push dword [descriptor_f]
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp, 4* 4
        
        push dword text
        push dword eax
        push dword format
        call [printf]
        add esp,4*3
        
        push dword [descriptor_f]
        call [fclose]
        add esp,4
        
        final:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
