#include <stdio.h>
#include <stdlib.h>
int v[50];
int N[50];
int P[50];
int afisareASM(int n,int v[]); //initializare subprogram
int main() 
{
 FILE* f=fopen("numere.txt","r"); // se deschide fisierul in mod citire
 
 int x;
 int ln=0;
 while(fscanf(f,"%d",&x)!=EOF){
    v[++ln]=x;
 } //citire elemente pana la finalul fisierului
 int n=0,p=0;
 for(int i=1; i<=ln; ++i)
    {
        if(v[i]<0){
        N[++n]=v[i]; // se pun elem negative in vectorul N, resp se det cate sunt
    } 
    else 
    {
    P[++p]=v[i]; // se pun elem pozitive in vectorul P, resp se det cate sunt
    }
    }
 printf("Numere negative: ");
 afisareASM(n,N); // se apeleaza subprogramul pt a afisa nr negative
 printf("\n");
 printf("Numere pozitive: ");
 afisareASM(p,P); // se apeleaza subprogramul pt a afisa nr pozitive
 return 0;
}