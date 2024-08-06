bits 32

global start        

extern exit, fopen, fclose, printf, fwrite
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
import fwrite msvcrt.dll

segment data use32 class=data
    nume_fisier db "ana.txt", 0
    mod_acces db "w", 0
    descriptor_f dd -1
    len equ 100
    text times 100 db 0
    afisare_format db "Descriptorul este %x", 0
    format db "%d", 0

segment code use32 class=code
start:
    ; fopen(nume, mod_acces)
    push dword mod_acces
    push dword nume_fisier
    call [fopen]
    add esp, 4 * 2

    mov [descriptor_f], eax

    cmp eax, 0
    je final

    ; Printeaza descriptorul in baza 16
    push afisare_format
    push dword [descriptor_f]
    call [printf]
    add esp, 8

    ; Scrie cifrele impare din descriptor in fisier
    mov eax, [descriptor_f]
    mov ebx, 10
    mov ecx, 0

write_digits:
    mov edx, 0
    div ebx
    test edx, 1
    jz not_odd

    add dl, '0'
    ; fwrite(&dl, 1, 1, file)
    push dword 1
    push dword 1
    push dword edx
    push dword [descriptor_f]
    call [fwrite]
    add esp, 16

not_odd:
    cmp eax, 0
    jnz write_digits

    ; fclose(file)
    push dword [descriptor_f]
    call [fclose]
    add esp, 4

final:
    ; exit(0)
    push dword 0
    call [exit]