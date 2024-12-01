;aici se realizeaza permutarile
bits 32
global permutare
extern printf
segment data use32 class=data
    format_permutare db "Permutare circulara: %X",10,0

segment code use32 public class=code
    permutare:
        ; Permutare circulara la dreapta a cifrelor
        mov eax, dword [esp + 4]
        ror eax, 8 ; O rotație circulară la dreapta
        mov dword [esp + 4], eax

        ; Afisare reprezentare dupa permutare
        push dword [esp + 4]
        push dword format_permutare
        call [printf]
        add esp, 4*2  ; Curățare argumente din stiva

        ret