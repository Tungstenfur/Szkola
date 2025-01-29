#include <iostream>
#include <string>
using namespace std;
int main()
{
    string oc;
    int dec, iloraz=-1, reszta;
    cin >> dec;
    while (iloraz != 0) 
    {
        iloraz = dec / 8;
        reszta = dec % 8;
        oc = to_string(reszta) + oc;
        dec = iloraz;
    }
    cout << oc;
}