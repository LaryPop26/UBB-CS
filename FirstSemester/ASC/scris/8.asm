bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    x dw -129,10+100h+1000b
    y dw 1001h>>1001b, 128h & 128
    z dw z,$$-z
    w dd x+y-z,w-y+x
    h dw 101b,11h-11b
    a db $$-$
    b dd h-b+0ah-0bh
    ;c db 3-b, z-w
    d dw -513, 128^(~128)
    e dd 'abcdefh'
    f dw w-1;, [w-1]
    g times 3 dw 'db'
    ;k dw 1+2b+3h+a, c+0ch
    m dd a+0ah;, a+ah
   ; s dd a-start,start-start1

; our code starts here
segment code use32 class=code
    start:
        xor eax,eax
        lea ebx,[esi]
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
