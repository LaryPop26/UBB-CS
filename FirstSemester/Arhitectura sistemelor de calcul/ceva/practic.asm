bits 32

global start        

extern exit, fopen, fclose, printf, fwrite, fseek
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
import fseek msvcrt.dll
import fwrite msvcrt.dll

segment data use32 class=data
    nume_fisier db "fisier.txt", 0    ; Numele fișierului care va fi creat sau deschis
    mod_acces db "r+", 0              ; Modul de acces pentru fopen (read and write)
    descriptor_f dd -1                ; Descriptorul fișierului
    len equ 100                        ; Lungimea buffer-ului textului
    text times 100 db 0               ; Buffer pentru text
    afisare_format db "Descriptorul este %x", 0  ; Format pentru afișarea descriptorului în hexazecimal
    format db "%d", 0                 ; Format pentru afișarea în decimal

segment code use32 class=code
start:
    ; fopen(nume, mod_acces)
    push dword mod_acces
    push dword nume_fisier
    call [fopen]
    add esp, 4 * 2

    mov [descriptor_f], eax          ; Salvare descriptor fișier

    cmp eax, 0                         ; Verificare dacă fopen a avut succes
    je final                          ; Dacă nu, iesire din program

    ; Printeaza descriptorul in baza 16
    push dword [descriptor_f]
    push afisare_format
    call [printf]
    add esp, 8

    ; Pozitionare la inceputul fisierului
    push dword [descriptor_f]         ; Descriptor fisier
    push dword 0                      ; Offset
    push dword 0                      ; Origin (SEEK_SET - de la inceput)
    call [fseek]
    add esp, 12

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