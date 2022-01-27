/*
포인트
1. 문자열 s에 들어있는 p/P의 개수와 y/Y의 개수 세기
2. C++ string은 일반 배열처럼 대괄호를 이용해서 string 인자에 접근할 수 있다.
*/

#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
	bool answer = true;
	int count_p = 0; // 개수 저장
	int count_y = 0;
	char find; // pP 나 yY를 찾기 위해 비교할 변수
	int i;

	for (i = 0; i < s.length(); i++)
	{	
		if(s[i] == 'p' || s[i] == 'P') { count_p++; }
		else if (s[i] == 'y' || s[i] == 'Y') { count_y++; }
	}
		
	if (count_p == count_y)
	{
		answer = true;
	}

	else
	{
		answer = false;
	}
	
	return answer;
}

int main()
{
	string s;

		std::cout << "s의 값 입력: " << std::endl;
		std::cin >> s;
		std::cout << "결과: "<< solution(s) << std::endl;

	return 0;
}