/*    
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA

*/

#include<iostream>
using namespace std;

int main(){
    int x;
    cin>>x;

    
    int spaces = (x-1);
    int noChars = 1;
    char charStart = 'A';


    for(int j=0;j<x;j++){

        for(int i=0;i<spaces;i++)cout<<" ";
        for(int i=0;i<(noChars-1)/2;i++)cout<<charStart++;
        cout<<charStart;
        for(int i=0;i<(noChars-1)/2;i++)cout<<--charStart;
        for(int i=0;i<spaces;i++)cout<<" ";
        cout<<endl;
        spaces--;
        noChars+=2;
        
    } 
}