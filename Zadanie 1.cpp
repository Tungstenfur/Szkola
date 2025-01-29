#include <iostream>
#include <string>
using namespace std;
int main()
{
    string bin;
    int dec, iloraz=-1, reszta;
    cin >> dec;
    while (iloraz != 0)
    {
        iloraz = dec / 2;
        reszta = dec % 2;
        bin = to_string(reszta)+bin;
        dec = iloraz;
    }
    cout << bin;
}

