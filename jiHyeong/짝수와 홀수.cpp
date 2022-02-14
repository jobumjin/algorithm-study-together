/*
몸풀기
*/

#include <string>
#include <iostream>

using namespace std;

string solution(int num) {
    string answer = "";
    
    if (num % 2 == 0) { // 짝
        answer = "Even";
        return answer;
    }
    else if (num % 2 == 1) { // 홀
        answer = "Odd";
        return answer;
    }    
}

int main() {
    int input;
    cout << "숫자 입력: " << endl;
    cin >> input;
    cout << solution(input);
}