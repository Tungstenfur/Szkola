#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int tablica[50];
void wypelnij(int tab[],int rozmiar)
{
    for (int i = 0;i < rozmiar;i++) 
    {  
        tab[i] = rand() % 1001;
    }
}
void wyswietl(int tab[], int rozmiar) {
    for (int i = 0;i < rozmiar;i++)
    {
        if (i % 10 == 0)cout << "\n";
        cout << i<<":" << tab[i] << " "; 
    }
    cout << "\n";
}
int znajdz(int tab[], int rozmiar, int szukana) {
    for (int i = 0;i < rozmiar;i++) {
        if (tab[i] == szukana) return i;
    }
    return -1;
}
int znajdzNieparzyste(int tab[], int rozmiar) {
    int toReturn;
    for (int i = 0;i < rozmiar;i++)
    {
        if (i%2==1)
        {
            cout << tab[i] << " ";
            toReturn += tab[i];
        }
    }
    return toReturn;
}
int main()
{
    int x = size(tablica);
    srand(time(0));
    wypelnij(tablica, x);
    wyswietl(tablica, x);
    cout << znajdz(tablica, x, tablica[0])<<endl;
    cout << znajdz(tablica, x, 500) << endl;
 
}
