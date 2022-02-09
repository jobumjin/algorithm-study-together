package codingtest;
//프로그래머스 하샤드 수
//자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수
//x의 자릿수의 합으로 x가 나누어져야 함

import java.util.Scanner;

/*로직생각해보기
x는 1 이상, 10000 이하인 정수
정수 x를 입력받음
x를 스트링 변환 -> 각각의 자리수를 char배열로 저장
자리수합을 digitSum에 저장
x를 digitSum으로 나누었을 때 나머지가 0이면 하샤드 수 -> true
아니면 false 리턴 
*/
/*
문제 풀면서 생긴 오류 해결

*/
public class Harshadnumber {

	public static boolean solution(int x) {
        boolean answer = true;
        
        String strX = String.valueOf(x);
        char[] arrX = strX.toCharArray();
        
        int digitSum = 0;
        for (char c : arrX) {
			digitSum += c-'0';
		}
        if(x%digitSum==0) {
        	
        	return answer;
        }
        else {
        	answer = false;
			return answer;
		}
        
    }
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int input = sc.nextInt();
		
		//System.out.println(String.valueOf(solution(input)));
		System.out.println(solution(input));
	}

}
