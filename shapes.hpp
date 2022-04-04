#include <string>

using std::string;

class Point
{
	private:
		double x, y;
	public:
		Point() : x(0), y(0) {}
		Point(double x, double y) : x(x), y(y) {}
		void set(double x, double y);
		double getx();
		double gety();
		void move(double x, double y);
		bool equals(Point p);
		void print();
		string toString();
};

class HalfEdge
{
	private:
		Point ps;
		Point pe;
	public:
		HalfEdge();
		HalfEdge(double x1, double y1, double x2, double y2);
		HalfEdge(const Point & ps, const Point & pe ) : ps(ps), pe(pe) {}
		void set(Point pstart, Point pend);
		void setDeep(const Point & pstart, const Point & pend);
		Point getps();
		Point getpe();
		bool equals(HalfEdge line);
		// void move(Point x, Point y);
		void print();
};

class Trapezoid
{
	private:
		Point p1, p2, p3, p4;
		HalfEdge top, bot, left, right;
	public:
		Trapezoid();
		Trapezoid(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4);
		Trapezoid(Point p1, Point p2, Point p3, Point p4);
		Trapezoid(HalfEdge topp, HalfEdge botp, HalfEdge leftp, HalfEdge rightp);
		// Trapezoid(HalfEdge(const HalfEdge & top, const HalfEdge & bot, const HalfEdge & left, const HalfEdge & right)) : top(top), bot(bot), left(left), right(right) {}
		void set(const HalfEdge & topp, const HalfEdge & botp, const HalfEdge & leftp, const HalfEdge & rightp);
};