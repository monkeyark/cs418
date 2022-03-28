#include <iostream>
#include "shapes.h"
#include "trapezoidal.h"

using std::cout;
using std::cin;
using std::endl;

int main()
{
	Point p1;
	Point p2;
	int nx, ny;
	int dx, dy;
	cout << "Enter p1: ";
	cin >> nx >> ny;
	p1.set(nx, ny);

	cout << "Enter p2: ";
	cin >> nx >> ny;
	p2.set(nx, ny);
	p1.print();
	cout << ", ";
	p2.print();
	cout << endl;

	cout << "Enter p2 changes: ";
	cin >> dx >> dy;
	while(!cin.eof())
	{
		p2.move(dx, dy);
		p2.print();
		cout << endl;
		cin >> dx >> dy;
	}

	return 0;
}