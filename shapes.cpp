#include "shapes.h"
#include <iostream>

using std::string;
using std::cout;

void Point::set(int x0, int y0)
{
	x = x0;
	y = y0;
}

int Point::getx()
{
	return x;
}

int Point::gety()
{
	return y;
}

void Point::move(int dx, int dy)
{
	x += dx;
	y += dy;
}

void Point::print()
{
	cout << "(" << x << ", " << y << ")";
}

// string Point::toString()
// {
// 	return "(" + x + ", " + y + ")";
// }