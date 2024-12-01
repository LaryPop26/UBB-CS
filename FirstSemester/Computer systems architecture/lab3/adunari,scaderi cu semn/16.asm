;de calculat: (d-a)-(a-c)-d
;a - byte, b - word, c - double word, d - qword - Interpretare cu semn
;(d-a)-(a-c)-d = (1073741456- 10) - (10- 2655674) - 1073741456 = 1073741446 - (-2655664) - 1073741456 = 2655654

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 10
    c dd 2655674
    d dq 1073741456

; our code starts here
segment code use32 class=code
    start:
        ;convertim byte-ul a la qword EDX:EAX
        mov al,byte[a]
        cbw
        cwde
        cdq
        
        ;mutam qword-ul a in ECX:EBX
        mov ecx,edx  
        mov ebx,eax         ;ecx:ebx = a
        
        ;mutam qword-ul d in EDX:EAX
        mov eax,dword[d]
        mov edx,dword[d+4] ; edx:eax = d
        
        ;scadem qword-ul a din qword-ul d in EDX:EAX
        sub eax,ebx
        sbb edx,ecx         ;edx:eax = d - a
        
        ;mutam qword-ul (d-a0 in ECX:EBX
        mov ecx,edx
        mov ebx,eax         ;ecx:ebx = d - a
        
        ;convertim byte-ul a la dword EAX
        mov al,byte[a]
        cbw
        cwde                ;eax = a
        ;scadem in EAX dword-ul c
        sub eax,dword[c]    ;eax = a - c
        cdq                 ;eax -> edx:eax
        
        ;scadem qword-ul (a-c) din qword-ul (d-a) in ECX:EBX
        sub ebx,eax         ;ebx=ebx-eax
        sbb ecx,edx         ;ecx:ebx=(d-a) - (a-c)
        
        ;mutam qword-ul d in EDX:EAX
        mov eax,dword[d]
        mov edx,dword[d+4] ; edx:eax = d
        
        ;scadem qword-ul D din qword-ul (d-a) - (a-c)  in ECX:EBX
        sub ebx,eax         ;ebx=ebx-eax
        sbb ecx,edx         ;ecx:ebx=(d-a) - (a-c) - d
        ;rezultat in ecx:ebx
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
