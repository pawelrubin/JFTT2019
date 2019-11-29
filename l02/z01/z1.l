%{
#include<stdio.h>

int yywrap(); 
int yylex();
int NL=0;
int WC=0;
%} 

%%
^[[:blank:]]+(\n)?  ;
[[:blank:]]+(\n)?$  REJECT;
[[:blank:]]+        printf(" ");
[[:alnum:]]+        { ECHO; WC++; };
\n			        { printf("\n"); NL++;}
%%

int yywrap() {
    printf("NL = %d\n", NL);
    printf("WC = %d\n", WC);
    return 1; 
} 
int main() { 
    return yylex(); 
}
        