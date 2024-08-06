;Se da un fisier text. Sa se citeasca continutul fisierului, sa se determine litera mare (uppercase) 
;cu cea mai mare frecventa si sa se afiseze acea litera, impreuna cu frecventa acesteia.
;Numele fisierului text este definit in segmentul de date.
bits 32 
global start        
 
extern exit, fopen, fclose, fread, printf
import printf msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fclose msvcrt.dll             
import exit msvcrt.dll    
 
segment data use32 class=data

    nume_fisier db "fisier.txt", 0 ;numele fisierului care va fi deschis
    mod_acces db "r", 0 ;modul de deschidere a fisierului
    
    descriptor_f dd -1
    len equ 100    ; numarul maxim de caractere din fisier
    text times 100 db 0 ; sirul in care se va citi textul din fisier
    
    fv times 28 db 0 ; vector de frecventa pentru caractere
    fv_maxima dd 0
    
    afisare_format db "Litera cu cea mai mare frecventa este %c, si apare de %d ori",0
 
    
segment code use32 class=code
    start:
        ;fopen(nume, mod_acces)
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor_f], eax
        
        cmp eax, 0 ; verificam daca fisierul este deschis corect
        je final
        
        ;eax = fread(text, 1,len, descriptor_f)
        push dword [descriptor_f]
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp, 4 * 4
        
        ;eax = numarul de caractere citite
        mov ebx, 0
        mov ecx, eax ;ecx = numarul de caractere citite
        mov esi, text ;
        cld
        jecxz no_caracters
        mov ebx, 0 ; aici salvez caracterul cu fv maxima
        repeta:
            push ecx
            mov eax, 0 ; stocheaza caracterul citit
            mov edx, 0 ; suport 
            ;verificam daca e litera mare
            lodsb      ; AL = caracterul citit 
            cmp al, 65
            jb nu_e_uppercase   
            cmp al, 90
            ja nu_e_uppercase
                sub al, 65
                add byte [fv + eax], 1
                ;calcul fv max
                mov dl, [fv + eax]
                cmp dl, [fv_maxima]
                jb fv_mai_mica
                    mov [fv_maxima], dl ; salvam noua frecventa maxima
                    mov ebx, eax ; salvam caracterul cu noua fv_maxima
                fv_mai_mica:
                ;/////////
            nu_e_uppercase:
            pop ecx
        loop repeta
        
        ;printf(format, caracter, frecventa)
        push dword [fv_maxima] 
        mov dl, 'A'
        add edx, ebx            ; calculam in edx pozitia caracterului cu frecventa maxima
        push dword edx          
        push dword afisare_format 
        call [printf]
        add esp, 4 * 3
        
        no_caracters:
        ;fclose(descriptor_f)
        push dword [descriptor_f]
        call [fclose]
        add esp, 4
        
        final:
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program