package codingtest;

import java.util.Arrays;

//프로그래머스 완주하지 못한 선수
//단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주
//마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion
//완주하지 못한 선수의 이름을 return

/*로직생각해보기
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하
completion의 길이는 participant의 길이보다 1 작다
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자
참가자 중에는 동명이인이 있을 수 있다

participant 배열과 completion배열을 sort
for문을 통해 인덱스별로 비교 다른 것이 있으면 participant에 있는 값이 완주하지 못한 선수
for문이 완료되었는데도 완주하지 못한 사람을 못 찾으면 마지막 인덱스에 있는 사람이 완주하지 못한 선수

*/
/*
문제 풀면서 생긴 오류 해결
https://coding-grandpa.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80-%EB%AA%BB%ED%95%9C-%EC%84%A0%EC%88%98-%ED%95%B4%EC%8B%9C-Lv-1

이클립스 상에서 for문의 if 조건문을 아래와같이 해도 정상적으로 결과가 나온다.
        	if(participant[i] !=completion[i])
하지만 프로그래머스에 제출하면 오류가 발생하여 오답으로 나오는데 해결방법으로는 
        	if(!participant[i].equals(completion[i]))
equals를 활용하여 비교하는 것이다.
*/
public class Marathon {

	public static String solution(String[] participant, String[] completion) {
        String answer = "";
        
        //배열 정렬
        Arrays.sort(participant);
        Arrays.sort(completion);
        
        
        //String raceRetire=null; //완주못한 선수를 저장할 변수
        
        //참가자 배열과 완주자 배열을 비교해서 다르면 참가자 배열값에 있는 선수가 완주못한 선수
        for(int i=0; i<participant.length-1; i++) {
        	if(participant[i] !=completion[i]) {
        		
        		return participant[i];
        	}
        }
        
        //for문을 완료해도 완주 못한 선수를 못 찾으면 참가자 배열에서 마지막 선수가 retire
        return participant[participant.length-1];
    }
	
	public static void main(String[] args) {
		
		String[] str = {"leo", "kiki", "eden"}; // eden kiki leo 
		String[] str1 = {"eden", "kiki"};
		
		//String[] str = {"marina", "josipa", "nikola", "vinko", "filipa"};
		//String[] str1 = {"josipa", "filipa", "marina", "nikola"};
		//System.out.println(solution(str, str1));
		
		//String[] str = {"mislav", "stanko", "mislav", "ana"};
		//String[] str1 = {"stanko", "ana", "mislav"};
		
				
		System.out.println(solution(str, str1));
	}

}

