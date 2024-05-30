%option noyywrap
%{
    #include <stdio.h>
    int ids = 0;
    int assign = 0;
    int rel = 0;
    int keywords = 0;
    int number = 0;
    int operators = 0;
%}
TYPE int|char|bool|float|void|for|do|while|if|else|return|void|break|continue|double|case|sizeof|struct|switch|long
%%
{TYPE} {printf("%s is keyword\n",yytext);keywords++;}
(<|>|<=|>=|==) {printf("%s is relational operator\n",yytext);rel++;}
= {printf("%s is assignment operator\n",yytext);assign++;}
(\+|-|\*|\/|%) {printf("%s is operator\n",yytext);operators++;}
[_a-zA-Z]+[a-zA-Z0-9]* {printf("%s is identifier\n",yytext);ids++;}
[0-9]+ {printf("%s is number\n",yytext);number++;}
[0-9]+.[0-9]+ {printf("%s is number\n",yytext);number++;}
(\+\+) {printf("%s is increment operator\n",yytext);operators++;}
(--) {printf("%s is decrement operator\n",yytext);operators++;}
. {;}
%%

/*** C Code section ***/
int main(void)
{
    // printf("\n");
    // yyin=fopen("testfile.txt","r+");
    yylex();
    // printf("identifiers = %d\nassignment operator = %d\nrelational operator = %d\nkeywords = %d\nNumber = %d\noperators = %d\n",ids,assign,rel,keywords,number,operators);
    return 0;
}