package codingtest;

import java.util.Scanner;

//프로그래머스 최대공약수와 최소공배수
//두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성
//배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환

/*로직생각해보기
두 수는 1이상 1000000이하의 자연수
예를 들어 3과 12의 최대공약수는 3, 최소공배수는 12
유클리드 호제법 두 자연수 a>b일 때 최대공약수는 gcd(b, a%b)로 나머지가 0이 될 때까지 반복
최소공배수는 두 자연수 a와 b의 곱을 한 뒤 최대공약수로 나눠준다. a*b/gcd
gcd재귀함수를 만들어 최대공약수를 구하고 나머지가 0이면 출력, 아니면 나머지가 0이 될때까지 반복
answer배열에 첫번째에는 gcd(n,m)결과를 넣고 두번째에는 n*m/gcd(n,m)을 넣고 리턴 
*/
/*
문제 풀면서 생긴 오류 해결
유클리드 호제법 - https://myjamong.tistory.com/138
*/

public class CalcGCDLCM {

	public static int gcd(int n, int m) {
		
		if(m == 0) return n;
		
		return gcd(m, n%m);
	}
	
	public static int[] solution(int n, int m) {
        int[] answer = {};
        
        answer = new int[2];
        
        answer[0] = gcd(n,m);
        answer[1] = n*m/answer[0];
        
         return answer;
    }
	
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int input1 = sc.nextInt();
		int input2 = sc.nextInt();
		
		System.out.print(solution(input1, input2)[0]+", ");
		System.out.println(solution(input1, input2)[1]);
		
		
	}

}




