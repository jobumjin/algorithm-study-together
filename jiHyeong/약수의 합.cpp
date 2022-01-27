/*
포인트
1. 약수 구하기: 나눴을 때 나머지가 0
2. 반복문
*/

#include <string>
#include <iostream>
using namespace std;

int solution(int n) {
	
	int i = 1; // n을 나눌 숫자
	int answer = 0;

	for (i = 1; i <= n; i++)
	{
		if (n % i == 0)
		{
		answer = answer + i;
		}			
	}

	return answer;
}

int main()
{
	int n;

		std::cout << "n의 값 입력:" << std::endl;
		std::cin >> n;
		std::cout << "약수의 합: " << solution(n) << std::endl;

	return 0;
}