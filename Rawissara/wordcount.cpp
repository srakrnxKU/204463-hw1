#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define MAX 1000000

map<string, int> wordlist;
map<int, vector<string>> sortedlist;

void add_word(string str)
{
	if (str == "=")
	{
		cout << str << "\n";
	}
	auto it = wordlist.find(str);
	if(it == wordlist.end())
	{
		wordlist.insert(pair<string, int>(str, 1));
	}
	else
	{
		it->second += 1;
	}
}

void sort()
{
	for(auto word = wordlist.begin(); word != wordlist.end(); word++)
	{
		auto it = sortedlist.find(word->second);
		if(it == sortedlist.end())
		{
			vector<string> list;
			list.push_back(word->first);
			sortedlist.insert(pair<int, vector<string>>(word->second, list));
		}
		else
		{
			(it->second).push_back(word->first);
		}
	}
}

int main(int argc, char *argv[]) {
	if (argc < 2)
	{
		return 1;
	}
	char* corpus = argv[1];
	string str = "";
	char c;

	ifstream file(corpus);
	while(file.get(c))
	{
		char x = tolower(c);
		if((int(x) < 97 || int(x) > 122) && x != '-' && x != '\'')
		{
			if(str != "")
			{
				add_word(str);
				str = "";
			}
		}
		else
		{
			if(x == '-' && str == "") ;
			else if(x == '\'' && str[0] == '\'')
			{
				str.erase(str.begin());
			}
			else
			{
				str += x;
			}
		}
	}
	file.close();

	sort();

	//Frequency of Word
	for(auto it = sortedlist.rbegin(); it != sortedlist.rend(); it++)
	{
		cout << it->first << "   ";
		for (auto i = (it->second).begin(); i != (it->second).end(); i++)
		{
			if(i != (it->second).begin())
			{
				cout << ",";
			}
			cout << *i;
		}
		cout << "\n";
	}

	//Frequency of Frequency
	/*for(auto it = sortedlist.begin(); it != sortedlist.end(); it++)
	{
		cout << it->first << "   " << (it->second).size() << "\n";
	}*/
}
