package codingtest;

import java.util.Scanner;

//프로그래머스 문자열 내 p와 y의 개수
//대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
//s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution.

/*로직생각해보기
문자열 s 길이는 50이하의 자연수
for문을 이용해서 문자열을 하나씩 읽어와 p또는 y면 카운트
마지막에  pCount와 yCount를 비교 후 true or false를 출력
*/
/*
 문제 풀면서 생긴 오류 해결
 문자 비교할 때는 메소드 str.equals(str1) 이런식으로 해야 비교됨
 */
public class NumPnY {

	static boolean solution(String s) {
        boolean answer = true;
        int pCount =0;
        int yCount =0;
        
        for(String ch : s.split("")) {
        	System.out.println(ch);
        	if(ch.equals("p") || ch.equals("P")) {
        		pCount= pCount+1;
        	}
        	else if(ch.equals("y") || ch.equals("Y")) {
        		yCount= yCount+1;
        	}
        }
        
        if(pCount == yCount) {
        	answer = true;
        }
        else {
        	answer = false;
        }
        System.out.println(pCount);
        System.out.println(yCount);
        return answer;
    }
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("입력하세요: ");
		String input = sc.next();
		
		System.out.println(solution(input));
	}

}
