//Factorial
#include<stdio.h>
 int main()
 {
     int i=5;
     int *p;
     p=&i;
     printf("%d\n",p);        // Gives address of 5
     printf("%d\n",  bbb&i);
     printf("%d\n",*p);       // Fetches the value of 5
     printf("%d\n",i);
    /* Pointer should be the same as value*/
     char a="A";
     char *q;
     printf("%s\n",q);        // Gives address of 5
     printf("%s\n",&a);
     printf("%s\n",*q);       // Fetches the value of 5
     printf("%s\n",a);




     //int value[]={1,3,4};
    // printf("%d",&value[]);

 }

