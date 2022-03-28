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
		Point p1;
		Point p2;
	public:
		LineSegment(int x1, int y1, int x2, int y2);
		LineSegment(const Point & p1, const Point & p2 ) : p1(p1), p2(p2) {}

		void setPoints( const Point & ap1, const Point & ap2)
		{
			p1 = ap1;
			p2 = ap2;
		}
};

class Trapezoid
{
	private:
		LineSegment l1, l2, l3, l4;
	public:
		Trapezoid();
		Trapezoid(LineSegment l1, LineSegment l2, LineSegment l3, LineSegment l4);
};