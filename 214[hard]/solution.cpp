#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <iterator>

namespace {
	double dist(double x0, double y0, double x1, double y1) {
		// no need to std::sqrt the thing since sqrt(x) is a monotonically increasing function
		return std::pow((x0 - x1), 2) + std::pow((y0 - y1), 2);
	}
} //namespace anon

int main() {
	typedef std::pair<double, double> Point;
	std::vector<Point> Points;
	Point initpos(0.5, 0.5);
	double totalDist = 0;

	std::ifstream file("100.txt");
	file.ignore ( std::numeric_limits<std::streamsize>::max(), '\n' );
	std::string line;
	double x, y;
	while (file >> x >> y) {
		Points.push_back(std::make_pair(x, y));
	}

	double temp;
	while(!Points.empty()) {
		double min = 1000;
		std::vector<Point>::iterator ind = Points.begin();
		std::vector<Point>::iterator nn = Points.begin();
		while (ind != Points.end()) {
			temp = dist(std::get<0>(initpos), std::get<1>(initpos), std::get<0>(*ind), std::get<1>(*ind));
			if (temp < min) {
				min = temp;				   
				nn = ind;
			}
			++ind;
		}	
		totalDist += std::sqrt(min);
		std::swap(initpos, *nn);
		Points.erase(nn);
	}

	std::cout << totalDist << std::endl;
	return 0;
}
