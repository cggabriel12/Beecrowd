#include <iostream>
#include <iomanip> // necessário para setprecision

using namespace std;

double r = 0;
double pi = 3.14159;

int main() {
    cin >> r;

    cout << fixed << setprecision(4); // 4 casas decimais
    cout << "A=" << (r * r) * pi << "\n";

    return 0;
}

