#include<stdio.h>
long fn(long n) {
  long temp=0;
  int i,flag=1;
  if(n<=0) {
      printf("error: n must > 0");
      exit(1);
    }
  for(i=1;i<=n;i++) {
      temp=temp+flag*i;
      flag=(-1)*flag;
    }
  return temp;
}
int main()
{
	long result = 0;
	long n=99999999;
	result = fn(n);
	printf("the result is : %d\n",result);
	return 0;

}
