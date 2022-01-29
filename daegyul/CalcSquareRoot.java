package codingtest;

import java.awt.print.Printable;
import java.util.Scanner;

//프로그래머스 정수 제곱근 판별
//양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단
//n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, 
//n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성

/*로직생각해보기
n은 1이상, 50000000000000 이하인 양의 정수
math클래스 sqrt()메소드 활용 
입력받은 정수를 Math.sqrt()로 제곱근을 구한다.
double형 -> long형으로 변환
구해진 값 x을 제곱한 결과와 입력받은 n을 비교하여 다르면 -1
같으면 x+1하고 제곱한 결과를 반환
*/
/*
문제 풀면서 생긴 오류 해결
자바 제곱근 - https://coding-factory.tistory.com/532
*/
public class CalcSquareRoot {

	public static long solution(long n) {
        long answer = 0;
        
        long resultInputSqrt = (long) Math.sqrt(n);
        
        if((resultInputSqrt*resultInputSqrt) == n) {
        	answer = (resultInputSqrt+1)*(resultInputSqrt+1);
        }
        else {
        	answer = -1;
        }
        return answer;
    }
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		long input = sc.nextLong();
		
		System.out.println(solution(input));
		
		
	}

}
