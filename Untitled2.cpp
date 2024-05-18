#include <iostream>
using namespace std;
int main()
{
	float sum=0 , Grade1 ,Grade2 ,Grade3 ,Grade4 ,Grade5 , average=0;
	
	cout<<"\nInput grade in Math :";cin>>Grade1;
	cout<<"\nInput grade in Science :";cin>>Grade2;
	cout<<"\nInput grade in Filipino :";cin>>Grade3;
	cout<<"\nInput grade in History :";cin>>Grade4;
	cout<<"\nInput grade in PE :";cin>>Grade5;
	
	
	sum=Grade1+Grade2+Grade3+Grade4+Grade5;
	average=sum/5;
	
	cout<<"\nThe sum is" <<sum;
	cout<<"\nThe average is" <<average;
	
	return 0;
}
