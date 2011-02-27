
#include "time.h" 
#include "stdio.h" 
#include "stdlib.h" 
#include "string.h"
int main(void) 
{ 
    time_t c_start,t_start, c_end,t_end;   
    c_start = clock();
       t_start = time(NULL) ; 
    getchar(); 
       c_end = clock();
    t_end = time(NULL) ; 
    printf("The pause used %f ms by time().\n",difftime(c_end,c_start)) ; 
       printf("The pause used %f s by clock().\n",difftime(t_end,t_start)) ;
    return 0; 
}
