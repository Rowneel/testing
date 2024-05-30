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
%x test tokenize
TYPE int|char|bool|float|void|for|do|while|if|else|return|void|break|continue|double|case|sizeof|struct|switch|long
%%
 BEGIN(test);

<test>[a-zA-Z]+[ ]=[ ]([_a-zA-Z][a-zA-Z0-9]*|[0-9]+.[0-9]+|[0-9]+)([ ][+/*%\-][ ]([_a-zA-Z][a-zA-Z0-9]*|[0-9]+.[0-9]+|[0-9]+))+; {printf("Valid Expression!! Enter your expression again to tokenize.\n"); BEGIN(tokenize);}
<tokenize>= {printf("%s is assignment operator\n",yytext);assign++;}
<tokenize>[0-9]+ {printf("%s is number\n",yytext);number++;}
<tokenize>[0-9]+.[0-9]+ {printf("%s is number\n",yytext);number++;}
<tokenize>(\+|-|\*|\/|%) {printf("%s is operator\n",yytext);operators++;}
<tokenize>[_a-zA-Z][a-zA-Z0-9]* {printf("%s is identifier\n",yytext);ids++;}
<tokenize>; {BEGIN(test);}
<test>.+ {printf("Invalid expression!! Enter Valid Expression!! Example: a = b - c;");BEGIN(test);}
%%

/*** C Code section ***/
int main(void)
{
    // printf("\n");
    // yyin=fopen("testfile.txt","r+");
    yylex();
    // printf("identifiers = %d\nassignment operator = %d\nrelational operator = %d\nkeywords = %d\nintegers = %d\noperators = %d\n",ids,assign,rel,keywords,number,operators);
    return 0;
}