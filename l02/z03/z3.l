%{
#include <stdio.h>
#include <stdbool.h>

int yywrap();
int yylex();

bool print_doc = false;
%}

/* states*/
%x INSTRING
%x ININCLUDE
%x SINGLELINE_COMMENT
%x MULTILINE_COMMENT

%%

\"                          { ECHO; BEGIN(INSTRING); }
<INSTRING>{
\"                          { ECHO; BEGIN(INITIAL); }
.                           ECHO;
}

#include[[:blank:]]*\<      { ECHO; BEGIN(ININCLUDE); }
<ININCLUDE>{
>                           { ECHO; BEGIN(INITIAL); }
.|\n                        ECHO; 
}

\n?\/(\\\n)*\/              BEGIN(SINGLELINE_COMMENT);
<SINGLELINE_COMMENT>{
.*\\\n                      ;
.                           ;
[^\\]\n                     { printf("\n"); BEGIN(INITIAL); }
}

\n?\/(\\\n)*\*              BEGIN(MULTILINE_COMMENT);
<MULTILINE_COMMENT>{
.|\n                        ;
\*(\\\n)*\/                 { printf("\n"); BEGIN(INITIAL); }
}

\n?\/(\\\n)*\/(\/|!)        { if (print_doc) ECHO; else BEGIN(SINGLELINE_COMMENT); }
\n?\/(\\\n)*\*(\\\n)*(\*|!) { if (print_doc) ECHO; else BEGIN(MULTILINE_COMMENT); }

%%


int yywrap() {
    return 1;
}

int main() {
    return yylex();
}