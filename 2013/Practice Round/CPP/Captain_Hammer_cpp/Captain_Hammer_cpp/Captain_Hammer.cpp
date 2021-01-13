// https://blog.csdn.net/weixin_44833351/article/details/112154546

#define _USE_MATH_DEFINES
#include <iostream>     // includes cin to read from stdin and cout to write to stdout
#include <cmath>
#include <iomanip>      // std::setprecision
using namespace std;    // since cin and cout are both in namespace std, this saves some text

// used later to perform accuracy correction and to stop asin from going out of bounds
#define Equ(a,b) ((fabs((a) - (b)))<(eps))
const double eps = 1e-6;

double solve(int v, int d) {
    // first use time = distance / horizontal speed
    // then use SUVAT eqn for vertical motion v = u + at
    // eliminate t and rearrange for theta(use sine double angle formula)
    double sin2theta = (9.8 * d) / pow((double)v, 2);
    if (Equ(sin2theta, 1.000000)) sin2theta = 1.000000;
    return asin(sin2theta) * 180 / (M_PI * 2);
}

int main() {
    int T, V, D;
    double theta;

    // get number of test cases
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        // get launch speed and distance travelled for each test
        cin >> V >> D;

        // output answer in desired format
        cout << fixed << setprecision(7);
        cout << "Case #" << i << ": " << solve(V, D) << endl;
    }
    return 0;
}