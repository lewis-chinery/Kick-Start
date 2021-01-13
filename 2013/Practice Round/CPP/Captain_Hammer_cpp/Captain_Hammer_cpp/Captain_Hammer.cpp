#define _USE_MATH_DEFINES
#include <iostream>     // includes cin to read from stdin and cout to write to stdout
#include <cmath>
#include <iomanip>      // std::setprecision
using namespace std;    // since cin and cout are both in namespace std, this saves some text

int main() {
    int T, V, D;
    double theta;

    // get number of test cases
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        // get launch speed and distance travelled for each test
        cin >> V >> D;

        // calculate theta(degrees between 0 and 90)
        theta = 180 / M_PI * abs(0.5 * asin(-9.8 * D / (pow(V, 2))));

        cout << fixed << setprecision(7);
        cout << "Case #" << i << ": " << theta << endl;
    }
    return 0;
}