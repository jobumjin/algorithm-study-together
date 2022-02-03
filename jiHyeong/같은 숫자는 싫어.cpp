/*
포인트
1. 배열을 다시 옮겨서 저장하는 과정이 굳이 필요 없다는것
2. 들어있는 배열을 그대로 검사해서 바로 출력하는 과정을 눈에 익히자
3. push_back
*/

#include <vector>
#include <iostream>
 
using namespace std;
 
vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    answer.push_back(arr[0]);
    for(int i = 1; i < arr.size() ; i++){
        if(arr[i-1]!=arr[i]) answer.push_back(arr[i]);
    }
    return answer;
}