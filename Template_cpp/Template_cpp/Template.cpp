// copy all of below into Google KickStart solution

#include <iostream>     // includes cin to read from stdin and cout to write to stdout
using namespace std;    // since cin and cout are both in namespace std, this saves some text

int main() {
    int T, N, N_out;
    cin >> T;           // read N. cin knows that T is an int, so it reads it as such.
    for (int i = 1; i <= T; ++i) {
        cin >> N;           // read N
        N_out = pow(N,3);   // perform some operation
        cout << "Case #" << i << ": " << N_out << endl;
        // cout knows that N_out is an int, and prints it accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }
    return 0;
}