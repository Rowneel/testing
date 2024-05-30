/*** Definition section ***/
%option noyywrap
%{
    #include <stdio.h>
%}

%%

[\n] {
	printf("Hello World\n");	
}

%%

/*** C Code section ***/
int main(void)
{
    yylex();
    return 0;
}