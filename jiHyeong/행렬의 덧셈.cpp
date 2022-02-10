/*
포인트
1. 2차원 배열
2. 배열의 자료형이 배열(vector)이다. vector<vector<int>>
*/

#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    int i = 0;
    int j = 0;

    for (i = 0; i < arr1.size(); i++) {
        vector<int> input;
        for (j = 0; j < arr1[i].size(); j++) {
            input.push_back(arr1[i][j] + arr2[i][j]);
        }
        answer.push_back(input);
    }
    return answer;
}