/*
포인트
1. 고정된 증가량(x)을 더해줄 변수 increment
*/
#include <string>
#include <vector>
using namespace std;

vector<long long> solution(int x, int n)
{
	vector<long long> answer;
	int increment = x; // 증가량
	for (int i = 1 ; i <= n ; i++) {
		x = increment * i;
		answer.push_back(x);
	}
	return answer;
}