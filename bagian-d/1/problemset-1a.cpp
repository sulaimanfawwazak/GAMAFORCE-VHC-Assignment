#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double numTiles(double n, double m, double a) {

  // min tiles to cover up the width
  double num_tiles_width = ceil(n/a);

  // min tiles to cover up the height
  double num_tiles_height = ceil(m/a);

  // multiply min number of tiles for width and height
  double num_tiles = num_tiles_width * num_tiles_height;

  return num_tiles;
}

int main() {
  double n, m, a;
  cin >> n >> m >> a;

  double answer = numTiles(n, m, a);

  // to make sure the output is integer
  cout << fixed << setprecision(0) << answer;
}