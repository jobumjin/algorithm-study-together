package codingtest;

import java.util.Arrays;
import java.util.Scanner;



//프로그래머스 나누어 떨어지는 숫자 배열
//array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수
//divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1

/*로직생각해보기
array와 divisor 값을 입력받기
for문과 연산자 %를 통해 divisor로 나누었을 때 나머지가 0인 숫자를 answer배열에 넣기
for문이 끝났는데 answer배열에 아무것도 없으면 -1을 answer배열에 넣기
answer배열 반환
*/
/*
문제 풀면서 생긴 오류 해결

*/
public class DivNumArray {

	//삽입정렬
	//기준의 왼쪽에 있는 수가 크면 오른쪽으로 넘기면서 정렬
	public static int[] insertion(int[] arr) {
		
		for(int i=1; i<arr.length; i++) {
			int k = i;
			for(int j=i-1; j>=0; j--) {
				if(arr[j]> arr[k]) {
					int tempNum = arr[j];
					arr[j] = arr[k];
					arr[k] = tempNum;
					k--;
				}
				
			}
		}
		
		return arr;
	}
	public static int[] solution(int[] arr, int divisor) {
        int[] answer = {};
        
        
        int[] tempArr = new int[arr.length];
        int arrIndex = 0;
        for(int i=0; i<arr.length; i++) {
        	if(arr[i]%divisor == 0) {
        		tempArr[arrIndex++] = arr[i];
        	}
        }
        if(arrIndex==0) {
        	answer = new int[1];
        	answer[0] = -1;
        }
        else {
        	System.out.println(arrIndex);
        	answer = new int[arrIndex];
        	int k =0;
        	for (int i=0; i<arrIndex; i++) {
				answer[i] = tempArr[i];
			}
        	answer = insertion(answer);
        }
        return answer;
    }
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();
		String[] input_arr = input.split(" ");
		int[] input_IntArr = new int[input_arr.length];
		
		for(int i=0; i<input_arr.length; i++) {
			input_IntArr[i] = Integer.parseInt(input_arr[i]);
		}
		//5 9 7 10
		//5
		//2 36 1 3
		//1
		int input_divisor = sc.nextInt();
		
		System.out.println(Arrays.toString(solution(input_IntArr, input_divisor)));
	}

}
