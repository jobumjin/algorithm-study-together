package codingtest;

import java.awt.print.Printable;
import java.util.Scanner;

//프로그래머스 자리수 더하기
//N의 각 자릿수의 합을 구해서 return 하는 solution


/*로직생각해보기
N의 범위 : 100,000,000 이하의 자연수

입력받은 숫자 N을 읽어온다.
정수를 String.valueof(N)을 사용하여 문자열로 변환
number.toCharArray()를 이용하여 문자배열로 변환
배열에 있는 값을 하나씩 불러오고
Character.getNumericValue(d)를 통해 int형변환 한 뒤 
자리수 총합 구하기
*/
/*
문제 풀면서 생긴 오류 해결
자바 숫자 분리 - https://www.delftstack.com/ko/howto/java/how-to-get-the-separate-digits-of-an-int-number/
자바 Char to Int - https://jiwontip.tistory.com/35
*/

public class SumDigitNum {

	
	public static int solution(int n) {
        int answer = 0;
        
        String strNum = String.valueOf(n);
        char[] digitNumArray = strNum.toCharArray();
        
        for(char d : digitNumArray ) {
        	//System.out.println((int)d); //강제형변환을 하면 쓰레기값
        	//System.out.println(d);
        	answer += Character.getNumericValue(d); //Character.getNumbericValue(ch)를 통해 형변환
        	
        }

        return answer;
    }
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int input = sc.nextInt();
		System.out.println(solution(input));
	}

}
