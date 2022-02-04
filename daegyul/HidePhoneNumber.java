package codingtest;
import java.util.Scanner;

//프로그래머스 핸드폰 번호 가리기
//전화번호가 문자열 phone_number
//전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴
/*로직생각해보기
s는 길이 4 이상, 20이하인 문자열
01033334444 >> *******4444
027778888 >> *****8888
전화번호가 들어왔을때 뒷 4자리를 제외한 모든 숫자를 *로 치환
입력받은 전화번호의 길이를 확인
길이 - 4를 하여 맨 앞 숫자만 *로 치환
*/
/*
문제 풀면서 생긴 오류 해결

*/
public class HidePhoneNumber {

	public static String solution(String phone_number) {
        String answer = "";
        
        char[] strArr = new char[phone_number.length()];
        
        strArr = phone_number.toCharArray();
        
        for(int i=0; i<phone_number.length()-4; i++) {
        	strArr[i] = '*';
        }
        answer = String.valueOf(strArr);
        return answer;
    }
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String input = sc.next();
		
		System.out.println(solution(input));
		
	}

}
