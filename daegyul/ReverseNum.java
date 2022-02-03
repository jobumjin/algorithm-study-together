package codingtest;
//프로그래머스 자연수 뒤집어 배열로 만들기
//자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴

import java.util.Arrays;
import java.util.Scanner;

/*로직생각해보기
n은 10,000,000,000이하인 자연수
long형 자연수를 입력받기
입력받은 자연수 n을 String.valueof(n)을 통해 문자열로 변환
문자열 길이만큼 answer배열을 초기화
문자열의 뒤에서부터 읽어온 뒤, answer배열은 처음부터 채우기
*/

/*
문제 풀면서 생긴 오류 해결
longToStr.charAt(i)-'0'

*/
public class ReverseNum {
	
	public static int[] solution(long n) {
        int[] answer = {};
        
        String longToStr = String.valueOf(n);
        
        answer = new int[longToStr.length()];
        int index = 0;
        for(int i=longToStr.length()-1; i>=0; i--) {
        	answer[index++] = longToStr.charAt(i)-'0';
        	
        }
        
        return answer;
    }
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		long input = sc.nextLong();
		
		System.out.println(Arrays.toString(solution(input)));
	}

}
