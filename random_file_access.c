#include <stdio.h>

struct student
{
    int roll;
    char name[50];
};

int main()
{
    struct student s;
    FILE *fp;
    int i, n, index;
    char choice;

    printf("Enter No of Students: ");
    scanf("%d", &n);

    fp = fopen("students.txt", "w");

    printf("\nEnter Roll and Name of %d Student:\n", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d%s", &s.roll, s.name);
        fwrite(&s, sizeof(s), 1, fp);
    }
    fclose(fp);
    fp = fopen("students.txt", "r");
    do
    {
        printf("\nEnter index: ");
        scanf("%d", &index);

        fseek(fp, index * sizeof(s), SEEK_SET);
        fread(&s, sizeof(s), 1, fp);
        printf("Record at index %d:\n", index);
        printf("Roll: %d\n", s.roll);
        printf("Name: %s\n", s.name);
        printf("\nFind another student?(y/n): ");
        scanf(" %c", &choice);
    }while (choice != 'n');
    fclose(fp);

    return 0;
}