#include <string>
#include <iostream>

using namespace std;

bool isPalindrom(string s)
{
    bool answer= false;   
    int i = 0;
    int j = s.length() - 1; // 배열의 인덱스 끝부분
    
        for (i = 0; i < s.length()/2; i++)
        {
            if (s[i] != s[j - i]) {
                answer = false;
                return answer;
            }                                                            
        }
        answer = true;   
    return answer;
}

int main() {
    string input;

    while (true) {
        cout << "문자 입력: " << endl;
        cin >> input;
        cout << isPalindrom(input) << endl;
    }    
}