#include <iostream>
using namespace std;

bool willBark(int t, int s, int x) {
  // multiplier
  int n = 1; 

  // time t
  int time0 = t;

  // iterates to repeatedly multiply the s with the multiplier
  while (true) {

    // time t + s
    int time1 = t + n*s; // time at t + n*s

    // time t + s + 1
    int time2 = t + n*s + 1; // time at t + n*s + 1

    // check whether x is the bark-time or not
    if (x == time0 || x == time1 || x ==time2) {
      return true;
      break;
    }
    else {
      ++n; // increment the multiplier
      if (time1 > x || time2 > x) { // if time1 and time2 exceed the x, then break
        return false;
        break;
      }
    }
  }
}

int main() {
  int t, s, x;
  cin >> t >> s >> x;

  bool answer = willBark(t, s, x);

  if(answer == 1) {
    cout << "YES";
  }
  else {
    cout << "NO";
  }
}

