#include <iostream>
#include <fstream>
#include "io.hpp"

using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;

string read_file(string read_path)
{
	ifstream file(read_path);
	//TODO
	string text, line;
	while (getline(file, line))
	{
		text = text + line + "\n";
	}
	cout << text << endl;
	file.close();
	return text;
}


void save_file(string save_path)
{
	ofstream file(save_path);
	//TODO

	file.close();
}

void print_file(string file_path)
{
	ifstream file(file_path);
	string text, line;
	while (getline(file, line))
	{
		text = text + line + "\n";
	}
	cout << text << endl;
	file.close();
}