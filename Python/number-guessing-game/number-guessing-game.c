#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
    int number,guess,nguesses=1;
    srand(time(0));
    number=rand()%100+1;//Generate a random number betwwen 1 to 100
    // printf("the number is %d\n",number);
    //keep running the loop untill the number is guessed
    do
    {
        printf("Guess the number between 1 to 100\n");
        scanf("%d",&guess);
        if (guess<number)
        {
            printf("higher number plzz\n");
        }
        else if (guess>number)
        {
            printf("lower number plzz\n");
        }
        else
        {
            printf("you guessed it in %d attempt\n",nguesses);
        }
        nguesses++;
        
        
        
    } while (guess!=number);
    
    return 0;
}
