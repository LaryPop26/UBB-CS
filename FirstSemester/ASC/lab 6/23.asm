;Dandu-se un sir de octeti sa se obtina un sir de cuvinte care sa contina in octetii inferiori 
;multimea caracterelor din sirul de octeti, iar octetul superior al unui cuvant sa contina numarul de aparitii al 
;octetului inferior din acel cuvant in sirul de octeti dat.
;Exemplu:   
    ;daca avem sirul:
        ;sir DB 2, 4, 2, 5, 2, 2, 4, 4 
    ;se va obtine sirul
        ;rez DW 0402h, 0304h, 0105h.
bits 32 ;assembling for the 32 bits architecture
global start
; we ask the assembler to give global visibility to the symbol called start 
;(the start label will be the entry point in the program) 
extern exit ; we inform the assembler that the exit symbol is foreign; it exists even if we won't be defining it
import exit msvcrt.dll  ; we specify the external library that defines the symbol
        ; msvcrt.dll contains exit, printf and all the other important C-runtime functions
import printf msvcrt.dll
; our variables are declared here (the segment is called data) 
segment data use32 class=data
    sir db 2, 4, 2, 5, 2, 2, 4, 4
    len equ $-sir
    rez times len dw 0

; the program code will be part of a segment called code
segment code use32 class=code
    start:
    
    cld
    mov esi, sir      ; Adresa de început a șirului
    mov edi, rez      ; Adresa de început a rezultatului
    xor ecx, ecx      ; Resetăm contorul

    ; Procesăm șirul
    procesare:
        lodsb          ; Încarcă valoarea din [esi] în AL și avansează ESI
        test al, al    ; Verificăm dacă am ajuns la sfârșitul sirului
        jz sfarsit     ; Dacă da, terminăm procesarea

        mov ebx, edi   ; Adresa de început a rezultatului
        mov edx, 0     ; Resetăm cuvântul temporar

    ; Căutăm octetul în șirul rezultat
        cautare:
            cmp al, [ebx]  ; Comparăm octetul cu cel din rezultat
            jne nu_este     ; Dacă nu e același, continuăm căutarea
            inc edx          ; Creștem numărul de apariții
            jmp gata_cautare
        nu_este:
            add ebx, 4      ; Trecem la următorul cuvânt din rezultat

            cmp ebx, edi    ; Am ajuns la finalul rezultatului?
            jl cautare      ; Dacă nu, continuăm căutarea

        ; Adăugăm octetul și numărul de apariții la șirul rezultat
        mov al, dl         ; Mutăm valoarea lui dl în al pentru a o putea folosi cu stosb
        stosw              ; Adăugăm cuvântul la rezultat

        gata_cautare:
        
        jmp procesare

    sfarsit:
    ; Aici poți utiliza rezultatul sau face alte operații

    ; Aici poți adăuga cod pentru a termina programul
    push dword 0
    call [exit]
