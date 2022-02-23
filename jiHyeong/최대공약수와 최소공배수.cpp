// [포인트]
// for문으로 계속 나누는 방법의 시간복잡도는 O(N)이지만
// 유클리드 호제법을 사용하면 O(logN)
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> solution(int n, int m) {
    vector<int> answer;

    int a = 0;
    int b = 0;
    int r = 0; // 나머지

    a = n;
    b = m;
    // 유클리드 호제법
    while (b !=0)
    {
        r = a % b;
        a = b;
        b = r;
    }

    // 최소공배수
    answer.push_back(a);
    // 최대공약수
    answer.push_back(n * m /a);

    return answer;
}

int main() 
{    
    int input = 0;
    int n = 0;
    int m = 0;

    cout << "n 입력:" << endl;
    cin >> input;
    n = input;     

    cout << "m 입력:" << endl;
    cin >> input;
    m = input;

    cout << "[결과] " << endl;
    for (int i = 0; i < solution(n, m).size(); i++)
    {
        cout << solution(n, m)[i] << " ";
    }

    return 0;
}