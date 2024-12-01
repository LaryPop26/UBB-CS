;Se dau cuvintele A si B. Se cere dublucuvantul C:
    ;bitii 0-3 ai lui C coincid cu bitii 5-8 ai lui B
    ;bitii 4-10 ai lui C sunt invers fata de bitii 0-6 ai lui B
    ;bitii 11-18 ai lui C sunt 1
    ;bitii 19-31 ai lui C coincid cu bitii 3-15 ai lui B

bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 0011001001101001b
    b dw 1110010010100101b  
    c dd 0

; our code starts here
segment code use32 class=code
    start:
        mov ebx, 0 ; aici vom avea rezultatul
        
        mov eax,0        
        mov ax,[b] ; izolam bitii 5-8 ai lui b
        and ax, 0000000011100000b
        mov cl, 5
        ror ax,cl ; rotim 5 pozitii in dreapta
        or ebx,eax ; punem bitii in rezultat
        
        mov eax,0
        mov ax, [b] ; negam si izolam bitii 0-6 ai lui b
        not ax
        and ax, 0000000001111111b
        mov cl,4
        shl ax,cl ; shift 5 pozitii in stanga 
        
        or ebx,eax ; punem bitii in rezultat
        
        or ebx,00000000000001111111100000000000b ; facem bitii 11-18 din rezultat sa aiba valoarea 1
        
        mov eax,0
        mov ax,[b] ; izolam bitii 3-15 ai lui b
        and ax, 1111111111111000b
        mov cx,0
        
        push ax
        push cx
        pop eax ; transformare din ax in eax pentru a bune bitii pe pozitiile corecte in rezultat
        
        or ebx,eax ; punem bitii ini rezultat
        
        mov [c],ebx ; salvam rez in dublucuvantul c
        ; exit(0)
        push dword 0      ; push the parameter for exit onto the stack
        call [exit]       ; call exit to terminate the program
