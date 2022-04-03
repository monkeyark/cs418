#include <string>

using std::string;

class Point
{
	private:
		int x, y;
	public:
		Point() : x(0), y(0) {}
		Point(int x, int y) : x(x), y(y) {}
		void set(int x, int y);
		int getx();
		int gety();
		void move(int x, int y);
		void print();
		string toString();
};

class LineSegment
{
	private:
		Point ps;
		Point pe;
	public:
		LineSegment(int x1, int y1, int x2, int y2);
		LineSegment(const Point & ps, const Point & pe ) : ps(ps), pe(pe) {}

		void setPoints(const Point & pstart, const Point & pend)
		{
			ps = pstart;
			pe = pend;
		}
};

class Trapezoid
{
	private:
		LineSegment top, bottom, leftp, rightp;
	public:
		Trapezoid();
		Trapezoid(LineSegment top, LineSegment bottom, LineSegment leftp, LineSegment rightp);
};