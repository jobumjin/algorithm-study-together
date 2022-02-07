/*
포인트
몸풀기
*/

#include <string>
#include <vector>
#include <iostream>
using namespace std;

double solution(vector<int> arr) {
    double answer = 0;
    double sum = 0;
    for (int i = 0; i < arr.size(); i++) {
        sum = sum + arr[i];
    }
    answer = sum / arr.size();
    return answer;
}

int main()
{
    int size;
    int input;
    vector<int> arr;

    cout << "arr 크기 입력:" << endl;
    cin >> size;

    for (int i = 0; i < size; i++)
    {
        cout << "[" << i << "] 번째" << "arr 내용 입력:" << endl;
        cin >> input;
        arr.push_back(input);
    }
    cout << solution(arr);
    return 0;
}