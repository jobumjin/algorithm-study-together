package codingtest;

import java.util.Arrays;

//import com.sun.tools.javac.code.Attribute.Array;

//프로그래머스 K번째수
//배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수 구하기
//배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, 
//commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return

/*로직생각해보기
array의 길이는 1 이상 100 이하
array의 각 원소는 1 이상 100 이하
commands의 길이는 1 이상 50 이하
commands의 각 원소는 길이가 3

array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]
배열을 정렬하면 [2, 3, 5, 6]
위 배열의 3번째 숫자는 5

for문 i commands.length만큼
	int k =0;
	for문 j commands[i][0]-1, <commands[i][1]
		cutArr[k++]= array[j]
	cutArr 정렬 알고리즘 사용
	k번째 숫자 answer에 저장
answer 리턴


*/
/*
문제 풀면서 생긴 오류 해결

*/

public class CalcKNum {
	
	//삽입정렬 : 기준에서 기준보다 큰 수를 오른쪽으로 이동시키면서 정렬
	public static int[] AscInsertionSort(int[] array) {
		
		for(int i=1; i<array.length; i++) {
			//int k =i;
			for(int j=i-1; j>=0; j--) {
				
				if(array[j+1] < array[j]) {
					int temp = array[j];
					array[j] = array[j+1];
					array[j+1] = temp;
					//k--;
				}
				else {
					break;
				}
			}
		}
		
		return array;
	}
	
	public static int[] solution(int[] array, int[][] commands) {
        int[] answer = {};
        answer = new int[commands.length];

        
        for(int i=0; i<commands.length; i++) {
        	
        	int k =0;        	
        	int[] cutArr = new int[commands[i][1]-commands[i][0]+1];
        	
        	for(int j=commands[i][0]-1; j<commands[i][1]; j++) {
        		//System.out.println("j = "+j+"k = "+ k);
        		
        		cutArr[k++] = array[j];
        		//System.out.println(Arrays.toString(cutArr));
        	}
        	//정렬
        	answer[i] = AscInsertionSort(cutArr)[commands[i][2]-1];
        	
        	//System.out.println(Arrays.toString(answer));
        }
        
        return answer;
    }
	
	public static void main(String[] args) {

		int[] arr = {1, 5, 2, 6, 3, 7, 4};
		int[][] com = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
		//System.out.println(Arrays.toString(AscInsertionSort(arr)));
		System.out.println(Arrays.toString(solution(arr, com)));
	}

}
