#include <iostream>
#include <string>
using namespace std;
int main()
{
    string hex;
    int dec, iloraz = -1, reszta;
    cin >> dec;
    while (iloraz != 0)
    {
        iloraz = dec / 16;
        reszta = dec % 16;
        if (reszta == 15)
            hex = "F" + hex;
        else if (reszta == 14)
            hex = "E" + hex;
        else if (reszta == 13)
            hex = "D" + hex;
        else if (reszta == 12)
            hex = "C" + hex;
        else if (reszta == 11)
            hex = "B" + hex;
        else if (reszta == 10)
            hex = "A" + hex;
        else
            hex = to_string(reszta) + hex;
        dec = iloraz;
    }
    cout << hex;
}