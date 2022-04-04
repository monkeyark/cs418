#include "shapes.hpp"
#include <iostream>

using std::string;
using std::cout;

void Point::set(double x0, double y0)
{
	x = x0;
	y = y0;
}

double Point::getx()
{
	return x;
}

double Point::gety()
{
	return y;
}

void Point::move(double dx, double dy)
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


//Line Segment
LineSegment::LineSegment()
{
	ps.set(0, 0);
	pe.set(0, 0);
}

LineSegment::LineSegment(double x1, double y1, double x2, double y2)
{
	ps.set(x1, y1);
	pe.set(x2, y2);
}

void LineSegment::set(Point pstart, Point pend)
{
	ps.set(pstart.getx(), pstart.gety());
	pe.set(pend.getx(), pend.gety());
}

void LineSegment::setDeep(const Point & pstart, const Point & pend)
{
	ps = pstart;
	pe = pend;
}


//Trapezoid
Point LineSegment::getps()
{
	return ps;
}

Point LineSegment::getpe()
{
	return pe;
}

void LineSegment::print()
{
	cout << "(" << ps.getx() << ", " << ps.gety() << ")"
		<< "(" << pe.getx() << ", " << pe.gety() << ")";
}

Trapezoid::Trapezoid()
{
	top = LineSegment();
	bot = LineSegment();
	left = LineSegment();
	right = LineSegment();
}

Trapezoid::Trapezoid(LineSegment topp, LineSegment botp, LineSegment leftp, LineSegment rightp)
{
	top.set(topp.getps(), topp.getpe());
	bot.set(botp.getps(), botp.getpe());
	left.set(leftp.getps(), leftp.getpe());
	right.set(rightp.getps(), rightp.getpe());
}

void Trapezoid::set(const LineSegment & topp, const LineSegment & botp, const LineSegment & leftp, const LineSegment & rightp)
{
	top = topp;
	bot = botp;
	left = leftp;
	right = rightp;
}
