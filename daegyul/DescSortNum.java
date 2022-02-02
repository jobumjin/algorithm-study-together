package codingtest;

import java.util.Arrays;
import java.util.Scanner;




//프로그래머스 정수 내림차순으로 배치하기
// n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴

/*로직생각해보기
n은 1이상 8000000000 이하인 자연수
입력받은 정수 n을 string으로 변환
변환한 것을 int배열에 하나씩 순서대로 넣기
삽입정렬을 통해 배열을 sort
sort한 배열을 스트링으로 바꾼뒤 long형으로 형변환
*/
/*
문제 풀면서 생긴 오류 해결

문자 정수형 - https://cokes.tistory.com/80
자바 int를 자릿수 int배열로 분할
https://zetawiki.com/wiki/%EC%9E%90%EB%B0%94_int%EB%A5%BC_%EC%9E%90%EB%A6%BF%EC%88%98_int_%EB%B0%B0%EC%97%B4%EB%A1%9C_%EB%B6%84%ED%95%A0
digits.toString()은 오브젝트 정보를 스트링으로 출력
Arrays.toString(digits)는 [1,3,4,5,2]로 출력
String을 long으로 변환 - https://wotres.tistory.com/entry/Java-String%EC%9D%84-long%EC%9C%BC%EB%A1%9C-%EB%B3%80%ED%99%98%ED%95%98%EB%8A%94-%EB%B2%95
*
*/
public class DescSortNum {
	
	//기준인덱스로부터 왼쪽에 있는 수가 크면 오른쪽으로 이동시키면서 정렬
	public static int[] DescInsertionSort(int array[]) {
		
		for(int i=1; i<array.length; i++) {
			int pivot = i;
			
			for(int j=i-1; j>=0; j--) {
				if(array[j] < array[pivot]) {
					int tmp = array[j];
					array[j] = array[pivot];
					array[pivot] = tmp;
					pivot = j;							
				}
				else {
					break;
				}
			}
		}
		
		return array;
	}
	
	public static long solution(long n) {
		long answer =0;
		String temp = Long.toString(n);
		int[] digits = new int[temp.length()];
		
		for(int i=0; i<temp.length(); i++) {
			digits[i] = temp.charAt(i)-'0'; //char to int
		}
		
		
		String intTostr = Arrays.toString(DescInsertionSort(digits)).replace(", ","").replace("[","").replace("]","");
		
		
		answer = Long.parseLong(intTostr);
		return answer;
    }
	
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		long input = sc.nextLong();
				
		
		System.out.println(solution(input));
	}


	

}
