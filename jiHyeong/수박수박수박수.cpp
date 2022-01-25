/* 
[포인트]
1. 2로 나눴을 때 (홀,짝) 
2. string 라이브러리의 편리함
*/

#include <string>
#include <iostream>
using namespace std;

string solution(int n)
{
	string answer = "";
	for (int i = 0; i < n; ++i)
	{
		if (i % 2 == 0) { answer = answer + "수"; }
		else if (i % 2 == 1) { answer = answer + "박"; }
	}

	return answer;
}

int main()
{
	int n;

	std::cout << "n 입력:" << std::endl;
	std::cin >> n;
	std::cout << "결과: " << solution(n) << std::endl;

    return 0;
}
