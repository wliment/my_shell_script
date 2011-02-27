#include<stdio.h>
long fn(long n) {
  if(n<=0) {
      printf("error: n must > 0");
      exit(1);
    }
  if(0==n%2)
    return (n/2)*(-1);
  else
    return (n/2)*(-1)+n;
}
int main()
{
	long result = 0;
	long n=99999999;
	result = fn(n);
	printf("the result is : %d\n",result);
	return 0;

}
