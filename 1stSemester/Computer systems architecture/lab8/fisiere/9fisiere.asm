bits 32 ; assembling for the 32 bits architecture

;Se da un fisier text. Sa se citeasca continutul fisierului, sa se determine caracterul special 
;(diferit de litera) cu cea mai mare frecventa si sa se afiseze acel caracter, impreuna cu frecventa acestuia. 
;Numele fisierului text este definit in segmentul de date.

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fread, fclose, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    nume_fisier db "specialchar.txt", 0
    mod_acces db "r",0
    
    len equ 100
    text times (len+1) db 0
    descriptor dd -1
    frequency times 256 dd 0
    format db "Caracterul special este: '%c', intalnit de %d ori.", 0 

; our code starts here
segment code use32 class=code
    start:
        ; deschdere fisier pentru citire
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        
        cmp eax,0
        je final
        
        ; citire din fisier
        push dword [descriptor]
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp,4 * 4 
        
        mov esi, text    ; esi -> text

        xor ebx, ebx     ; contor pt frecventa
        xor ecx, ecx     ; contor pt ascii cu frecventa maxima

        count_loop:
            mov al, byte [esi]
            cmp al, 0        ; verificare daca s-a ajuns la final
            je find_max
            inc esi

            ; verificare caracter special
            cmp al, 'a'
            jl increment_frequency
            cmp al, 'z'
            jle count_loop
            cmp al, 'A'
            jl increment_frequency
            cmp al, 'Z'
            jle count_loop

        increment_frequency:
            movzx edi, al    ; Zero extend the ASCII value to edi
            inc dword [frequency + edi * 4]
            jmp count_loop

        find_max:
            mov edi, frequency
            xor eax, eax
            xor edx, edx

        max_loop:
            cmp eax, 256     ; Check if we've gone through all ASCII values
            je display_result
            mov ebx, [frequency + eax * 4]
            cmp ebx, edx
            jle next_char
            mov edx, ebx    ; Update max frequency
            mov ecx, eax    ; Update character with max frequency
        next_char:
            inc eax
            jmp max_loop
    
        display_result:
            push dword edx
            push dword ecx
            push dword format
            call [printf]
            add esp, 4*3
            
            ; inchidere fisier
            push dword [descriptor]
            call [fclose]
            add esp, 4
        
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
