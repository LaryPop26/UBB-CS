bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...

; our code starts here
segment code use32 class=code
    start:
        lea eax,[6+esp]
        ;mov eax,6+esp  invalid operand type
        movsx ax,[6+esp]
        mov ebp,[6+ebp*2]
        ;mov [6+ebp*2],12 operation size not specified
        mov ebp,[ebp+esp]
        ;movsx [6+esp],eax  invalid combinaton of opcode and operands
        ;mov [6+esp*2],eax
        ;mov [6+ebp*2],[6+esp]  invalid combinaton of opcode and operands
        ;movzx eax,[6+ebp*2]  operation size not specified
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
