#include <iostream>
#include "shapes.hpp"
#include "trapezoidal.hpp"

using std::cout;
using std::cin;
using std::cerr;
using std::endl;

int main(int argc, char* argv[])
{
	// Point p1;
	// int nx, ny;
	// cout << "Enter p1: ";
	// cin >> nx >> ny;
	// p1.set(nx, ny);
	// p1.print();
	// Point p2;
	// int dx, dy;
	// cout << "Enter p2: ";
	// cin >> nx >> ny;
	// p2.set(nx, ny);
	// p1.print();
	// cout << ", ";
	// p2.print();
	// cout << endl;

	// cout << "Enter p2 changes: ";
	// cin >> dx >> dy;
	// while(!cin.eof())
	// {
	// 	p2.move(dx, dy);
	// 	p2.print();
	// 	cout << endl;
	// 	cin >> dx >> dy;
	// }

	Point p = Point(0,0,0);
	Point p1, p2, p3;
	p1.set(0,0,0);
	p2.set(1,0,0);
	p3.set(0,1,0);

	HalfEdge l1, l2, l3;
	l1.set(p1, p2);
	l2.set(p2, p3);
	l3.set(p3, p1);

	return EXIT_SUCCESS;
}