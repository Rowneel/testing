/*** Definition section ***/
%option noyywrap
%{
    #include <stdio.h>
    int flag=0;
    int ln=1;
%}

%%

[(] {flag++;}

[)] {flag--;}

\n {
	if(flag==0)
		printf("The statemnet at line no = %d has no missing paranthesis\n",ln);
	else
		printf("Error at line no = %d\n",ln);
	if(flag>0)
		printf("The statemnet has either extra ( paranthesis or a missing ) paranthesis\n");
	else if(flag<0)
		printf("The statemnet has either extra ) paranthesis or a missing ( paranthesis\n");	
	flag=0;
	ln++;
}

. {;}
%%

int main(void)
{	
	char fname[100];
	printf("\nEnter the name of file\n");
	scanf("%s",fname);
	yyin=fopen(fname,"r+");
	yylex();
    return 0;
}
