/*

Sample:

Inputs
5
2
1

Outputs:
-16
(-2 + 4i)/10 
(-2 – 4i)/10


*/

#include <bits/stdc++.h>
using namespace std;

int main(){
    double a,b,c;
    cin>>a>>b>>c;

    ////converting a,b,c into complex numbers a+0i, b+0i, c+0i;
    complex<double> a_complex (a,0);
    complex<double> b_complex (b,0);
    complex<double> c_complex (c,0);

    ////calculating delta
    double delta = b*b - 4*a*c;

    ////converting delta into complex number
    complex<double> delta_complex (delta,0);


    ////finding solutions by formula solution = (-b (+ or -) sqrt(delta))/2a 

    complex<double> sol1 = (-b_complex + sqrt(delta_complex))/(complex<double>(2,0)*a_complex);
    complex<double> sol2 = (-b_complex - sqrt(delta_complex))/(complex<double>(2,0)*a_complex);


    cout<<delta<<endl;

    ///if delta >= 0 real solutions else complex solutions
    if(delta>=0){
        cout<<real(sol1)<<endl;
        cout<<real(sol2)<<endl;
    }
    else{
        cout<<real(sol1)<<"+ "<<imag(sol1)<<"i"<<endl;
        cout<<real(sol2)<<"+ "<<imag(sol2)<<"i"<<endl;
    }
    
    return 0;

}