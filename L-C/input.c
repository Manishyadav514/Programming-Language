
/*Structure in C*/
#include<stdio.h>

/* To define our own Laptop*/
struct student
{
    int id;
    char name;
    int standard;
};

void main()
{
    struct student good, bad;   /* struct: to show it is our own type student*/

    printf("Enter 1st student details\n");
    printf("Enter id\n");
    scanf("%d", &good.id);
    printf("Enter name:");
    scanf("%s", &good.name);
    printf("Enter class:");
    scanf("%d", &good.standard);
    printf("Good Student Details=%d,%s,%d", &good.id, &good.name, &good.standard);
}
