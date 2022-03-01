#include <iostream>
#include <cmath>
using namespace std;

long long solution(long long n) {
    long long answer = 0; 
    long long nSqrt = 0;
    nSqrt = sqrt(n);
    if (nSqrt*nSqrt == n)
    {
        return answer = (nSqrt + 1) * (nSqrt + 1);
    }
    else
    {
        return answer = -1;
    }    
}

int main() 
{    
    long long input = 0;
    while (true) {
        cout << "n 입력:" << endl;
        cin >> input;

        cout << "[결과] " << solution(input) << endl;

    }    
    return 0;
}
