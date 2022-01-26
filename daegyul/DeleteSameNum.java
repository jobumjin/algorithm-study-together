package codingtest;

import java.util.ArrayList;
import java.util.Scanner;



//프로그래머스 같은 숫자는 싫어
//배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
//연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
//남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지하는 solution

/*로직생각해보기
배열 arr의 크기 : 1,000,000 이하의 자연수
0보다 크거나 같고 9보다 작거나 같은 정수 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
arr배열을 읽어와 for-each문으로 하나씩 원소를 읽어온다.
answer배열이 비어있으면 읽어온 숫자를 저장하고, checkConsecutiveNumber를 초기화한다.
비어있지않으면 읽어온 원소와 checkConsecutiveNumber를 비교하고 같으면 contiune
같지 않으면 answer배열에 저장하고 checkConsecutiveNumber변수 초기화
위 과정을 반복 
*/
/*
문제 풀면서 생긴 오류 해결
이클립스 자동완성 - https://devlimk1.tistory.com/9

*/
public class DeleteSameNum {

	
	
	public static ArrayList<Integer> solution(int []arr) {
        //int[] answer = {};
		
		ArrayList<Integer> answer = new ArrayList<Integer>();
		
        int checkConsecutiveNumber = -1; //연속되는 숫자 -1초기화
        //int index=0;
        
        for(int num : arr) {
        	if(answer.isEmpty() == true) {
        		answer.add(num);
        		checkConsecutiveNumber = num;
        	}
        	else {
        		if(num == checkConsecutiveNumber) {
        			continue; //스킵
        		}
        		else {
        			answer.add(num);
        			checkConsecutiveNumber = num;
        		}
        	}
        }

        return answer;
    }
	
	public static void main(String[] args) {
		
		Scanner sc =new Scanner(System.in);
		int length = sc.nextInt(); // 입력되는 숫자 개수
		int[] input = new int[length]; //배열 선언
		
		for(int i=0; i<length; i++) {
			input[i] = sc.nextInt();
		}
		
		System.out.println(solution(input));
		
	}

}
