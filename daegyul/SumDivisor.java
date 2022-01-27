package codingtest;

import java.util.Scanner;

//프로그래머스 약수의 합
//정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

/*로직생각해보기
 n은 0 이상 3000이하 정수
 정수 12의 약수는 1, 2, 3, 4, 6, 12이다.
 정수 0이 들어오면 0 처리
 for문을 이용해서 2부터 ~자기자신까지 나눠지는지 확인하고 answer에 더하기
 */
public class SumDivisor {

	
	
	public static int solution(int n) {
        int answer = 1;
        
        if(n == 0) {
        	return 0;
        }
        else {
        	
        	for(int i =2; i<=n; i++) {
        		if(n%i == 0) {
        			answer += i;
        		}
        	}
        	
        }               
        
        return answer;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("정수 n을 입력하세요: ");
		int input = sc.nextInt();
		
		System.out.println(input + "의 약수 총합은 " + solution(input) + "입니다.");
		
		
	}

}
