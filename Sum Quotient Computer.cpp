#include<iostream>
#include<conio.h>
int main(void)
{
int x, y, sum, pro, dif, rem, quot;
cout<<"Enter First Number:";
cin>>x;
cout<<"Enter Second Number:";
cin>>y;
sum=x+y;
pro=x*y;
dif=x-y;
rem=x%y;
quot=x/y;
cout<<"nThe Sum is:"<<sum<<"nThe Product is:"
<<pro<<"nThe Difference is:"
<<dif<<"nThe Reminder is:"<<rem<<"nThe Quotient"<<quot;
cout<<"nThank you...";
cout<<"nPress any key to continue...";
getch();
}
