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
		void print();
		string toString();
};

class LineSegment
{
	private:
		Point ps;
		Point pe;
	public:
		LineSegment();
		LineSegment(double x1, double y1, double x2, double y2);
		LineSegment(const Point & ps, const Point & pe ) : ps(ps), pe(pe) {}
		void set(Point pstart, Point pend);
		void setDeep(const Point & pstart, const Point & pend);
		Point getps();
		Point getpe();
		// void move(Point x, Point y);
		void print();
};

class Trapezoid
{
	private:
		LineSegment top, bot, left, right;
	public:
		Trapezoid();
		Trapezoid(LineSegment topp, LineSegment botp, LineSegment leftp, LineSegment rightp);
		// Trapezoid(LineSegment(const LineSegment & top, const LineSegment & bot, const LineSegment & left, const LineSegment & right)) : top(top), bot(bot), left(left), right(right) {}
		void set(const LineSegment & topp, const LineSegment & botp, const LineSegment & leftp, const LineSegment & rightp);
};