;programul substituie fiecare litera a sirului s1 cu litera corespunzatoare din alfabetul dat
bits 32    
segment data use32 class=data
    alfabet dd "OPQRSTUVWXYZABCDEFGHIJKLMN"
    
segment code use32 public code
global substituire

substituire:
        mov ecx,0
            parcurgere_s1:
                movzx eax, byte [ebx + ecx] ; se incarca caracterul curent din s1 in eax
                cmp eax,0 ; se verifica daca s-a ajuns la sfarsitul sirului
                je sfarsit ; salt la final daca s-a terminat sirul
            
                sub eax,'a' ; convertire de la litere mici la litere mari
                movzx edx, byte[alfabet+eax] ; inlocuire litere cu cele din alfabet
                mov [edi+ecx],dl ; salvare litere in s2
            
                inc ecx
                jmp parcurgere_s1
        
        sfarsit:
            mov byte [edi + ecx], 0
           
        ret