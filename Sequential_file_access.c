#include <stdio.h>
#include <conio.h>
struct std
{
    int roll;
    char name[50];
};
struct std s;

void display(FILE *fp)
{
    rewind(fp);
    printf("\nRoll No.\t Name\n");
    while (fread(&s, sizeof(s), 1, fp))
    {
        printf("%d\t\t%s\n", s.roll, s.name);
    }
}
int search(FILE *fp, int key_roll)
{
    rewind(fp);
    while (fread(&s, sizeof(s), 1, fp))
        if (s.roll == key_roll)
            return 1;
    return 0;
}

int main()
{
    int i, n, key_roll, open;
    FILE *fp;
    printf("Enter Number of Students: ");
    scanf("%d", &n);
    if ((fp = fopen("student.txt", "w")) == NULL)
    {
        printf("\nFile could not be opened!\n");
    }
    else
    {
        for (i = 0; i < n; i++)
        {
            printf("\nEnter Roll No and Name of Student %d: ", i + 1);
            scanf("%d%s", &s.roll, s.name);
            fwrite(&s, sizeof(s), 1, fp);
        }
        fclose(fp);
        printf("\nRecord Added!\n");    
    }
    if ((fp = fopen("student.txt", "r")) == NULL)
    {
        printf("\nFile could not be opened!\n");
    }
    else
    {
        do
        {
            printf("\nPress:\n1.Display\n2.Search\n3.Exit\n>>>");
            scanf("%d", &open);
            switch (open)
            {
            case 1:
                printf("\nStudent Records:\n");
                display(fp);
                break;
            case 2:
                printf("\nEnter roll no of student to be searched:");
                scanf("%d", &key_roll);
                if (search(fp, key_roll))
                {
                    printf("\nRecord Found!");
                    printf("\nName: %s\n", s.name);
                }
                else
                {
                    printf("\nRecord Not Found!");
                }
                break;
            case 3:
                printf("\nExit!Press any key...");
                getch();
                break;
            default:
                printf("\nInvalid Option! Try again!");
                break;
            }
        } while (open != 3);
        fclose(fp);
    }
}
