/*
포인트
1. char to_string 불가능. 아스키코드 숫자를 뱉어버린다.
2. 그래서 'answer += 넣을 char;' 로 작성 (insert 연산과 동일함)
3. string을 배열 인덱스로 접근하는 방법
*/
#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string s)
{
	string answer = "";
	
	if (s.length() % 2 == 0) // 짝수
	{
		answer = answer + s[s.length() / 2 - 1] + s[s.length() / 2];
		;
	}
	else if (s.length() % 2 == 1) // 홀수
	{
		answer = s[s.length() / 2];
	}
	return answer;
}

int main()
{
	string s;
	string q; // 종료용

	while (q != "q")
	{
		std::cout << "s의 string 값 입력:" << std::endl;
		std::cin >> s;

		std::cout << "가운데 글자:" << solution(s) << std::endl;

		std::cout << "종료하려면 q입력\n계속하려면 아무키나 입력" << std::endl;
		std::cin >> q;
	}

	return 0;
}