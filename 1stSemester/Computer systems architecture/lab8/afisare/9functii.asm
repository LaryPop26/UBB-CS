bits 32 ; assembling for the 32 bits architecture
;Sa se citeasca de la tastatura doua numere a si b (in baza 10) si sa se calculeze: (a+b) / (a-b). 
;Catul impartirii se va salva in memorie in variabila "rezultat" (definita in segmentul de date). Valorile se considera cu semn.

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import scanf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dd 0
    b dd 0
    rezultat dd 0
    msg db "Primul numar este: ", 0
    msg2 db "Al doilea numar este: ", 0
    msg3 db "Rezultatul operatiei este: %d",0
    msgerror db "Eroare, numere egale!",0
    format db "%d", 0
; our code starts here
segment code use32 class=code
    start:
        ; citire primul nr
        push dword msg 
        call [printf]      
        add esp, 4 * 1      
         
        push dword a       
        push dword format
        call [scanf]        
        add esp, 4 * 2     
                 
        ; citire al 2 lea nr      
        push dword msg2 
        call [printf]     
        add esp, 4 * 1      
        
        push dword b       
        push dword format
        call [scanf]       
        add esp, 4 * 2     
        
        ; salvare nr in registrii pt calcule
        mov ebx,[a]
        mov eax,[b]
        
        add eax,ebx ; eax = a+b
        cdq
        
        sub ebx,[b] ; ebx = a-b
        
        ; comparare rez din ebx cu 0 , in caz ca nr sunt egale sa se afiseze mesaj de eroare
        mov ecx,0
        cmp ebx,ecx
        jz aici
        
        idiv ebx    ; eax = edx:eax / ebx , edx = edx:eax % ebx
        
        mov [rezultat],eax
        ; afisare rezultat      
        push dword [rezultat]       
        push dword msg3
        call [printf]       
        add esp, 4 * 2     
        jmp final
                      
        aici:
        push dword msgerror
        call [printf]
        add esp, 4           
        
        final:
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
