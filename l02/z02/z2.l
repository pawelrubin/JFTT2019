%{
#include<stdio.h>
int yylex();
int yywrap();
%}

/* states */
%x COMMENT
%x CDATA
%x INSTRING

%%

\<!--           BEGIN(COMMENT);
<COMMENT>{
.|\n            ;
-->             BEGIN(INITIAL);
}

\<!--.*--.*-->  ECHO;

\<!\[CDATA\[    { ECHO; BEGIN(CDATA); }
<CDATA>{
.|\n            ECHO;
]]>             { ECHO; BEGIN(INITIAL); }
}

\"              { ECHO; BEGIN(INSTRING); }
<INSTRING>{
\"              { ECHO; BEGIN(INITIAL); }
.               ECHO;
}

%%

int yywrap() {
    return 1;
}

int main() {
    return yylex();
}
