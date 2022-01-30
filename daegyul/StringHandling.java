package codingtest;

import java.util.Scanner;

//프로그래머스 문자열 다루기 기본
//문자열 s의 길이가 4 혹은 6
//숫자로만 구성돼있는지 확인해주는 함수, solution을 완성

/*로직생각해보기
s는 길이 1 이상, 길이 8 이하인 문자열


length를 통해 문자열 s의 길이가 4 OR 6인지 확인 하고
숫자로만 구성 돼있는지 확인
*/
/*
문제 풀면서 생긴 오류 해결
자바 문자열 숫자인지 구분 - https://blog.naver.com/hoon4672/222204799623
정규표현식

*/

public class StringHandling {

	
	public static boolean solution(String s) {
        boolean answer = false;
        if(s.length()==4 || s.length()==6) {
        	//boolean isNumeric = s.matches("[+-]?\\d*(\\.\\d+)?");
        	boolean isNumeric = s.matches("^[0-9]+$"); //^ 문자열 시작, [0~9]숫자 인정,+ 0~9 숫자 개수 제한없음, $ 문자열 종료
        	if(isNumeric) {
        		answer = true;
        	}
        	
        }        
        return answer;
    }
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		String input = sc.nextLine();
		System.out.println(solution(input));
	}

}
