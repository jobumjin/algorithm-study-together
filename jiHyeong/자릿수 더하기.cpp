// 포인트
// 10을 계속 나눈다 -> 자릿수 조정
//
#include <iostream>

using namespace std;

int solution(int n)
{
    int answer = 0;
    int temp = 0;

    while (n != 0) {
        temp = n % 10;
        answer += temp;
        n = n / 10;
    }
    return answer;
}

int main() 
{    
    int input = 0;
    
    cout << "숫자 입력:" << endl;
    cin >> input;

    cout << "각 자릿수 합: " << solution(input) << endl;    

    return 0;
}

