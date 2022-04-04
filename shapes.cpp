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

bool Point::equals(Point p)
{
	return x == p.getx() && y == p.gety();
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
HalfEdge::HalfEdge()
{
	ps.set(0, 0);
	pe.set(0, 0);
}

HalfEdge::HalfEdge(double x1, double y1, double x2, double y2)
{
	ps.set(x1, y1);
	pe.set(x2, y2);
}

void HalfEdge::set(Point pstart, Point pend)
{
	ps.set(pstart.getx(), pstart.gety());
	pe.set(pend.getx(), pend.gety());
}

void HalfEdge::setDeep(const Point & pstart, const Point & pend)
{
	ps = pstart;
	pe = pend;
}

Point HalfEdge::getps()
{
	return ps;
}

Point HalfEdge::getpe()
{
	return pe;
}

bool HalfEdge::equals(HalfEdge line)
{
	return (ps.equals(line.getps()) && pe.equals(line.getpe())
	|| (ps.equals(line.getpe()) && pe.equals(line.getps())));
}

void HalfEdge::print()
{
	cout << "(" << ps.getx() << ", " << ps.gety() << ")"
		<< "(" << pe.getx() << ", " << pe.gety() << ")";
}

//Trapezoid
Trapezoid::Trapezoid()
{
	top = HalfEdge();
	bot = HalfEdge();
	left = HalfEdge();
	right = HalfEdge();
}

//upper left corner, are named counterclockwise as p1, p2, p3, p4.

Trapezoid::Trapezoid(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4)
{
}

Trapezoid::Trapezoid(Point p1, Point p2, Point p3, Point p4)
{
}

Trapezoid::Trapezoid(HalfEdge topp, HalfEdge botp, HalfEdge leftp, HalfEdge rightp)
{
	top.set(topp.getps(), topp.getpe());
	bot.set(botp.getps(), botp.getpe());
	left.set(leftp.getps(), leftp.getpe());
	right.set(rightp.getps(), rightp.getpe());
}

void Trapezoid::set(const HalfEdge & topp, const HalfEdge & botp, const HalfEdge & leftp, const HalfEdge & rightp)
{
	top = topp;
	bot = botp;
	left = leftp;
	right = rightp;
}
