/*
포인트
1. vector 라이브러리: 동적 할당 가능한 편리한 배열
2. to_string 숫자
3. += 연산자와 string
*/


#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(vector<string> seoul)
{
	string answer = "";
	int i = 0;

	answer = answer + "김서방은 ";

	for (i = 0; i < seoul.size(); i++)
	{
		if (seoul[i] == "Kim")
		{
			answer = answer + to_string(i);
		}
	}
	answer = answer + "에 있다";

	return answer;
}

int main()
{
	vector<string> seoul;
	string input;
	string q; // 종료용

	while (q != "q") 
	{
		std::cout << "seoul배열의 string 값 입력:" << std::endl;
		std::cin >> input;
		seoul.push_back(input);
		std::cout << "종료하려면 q입력\n계속하려면 아무키나 입력" << std::endl;
		std::cin >> q;
	}
	std::cout << solution(seoul) << std::endl;

	return 0;
}