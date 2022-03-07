// 백준 17388번

package codingTest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class WaggleWaggle {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int soongsil = Integer.parseInt(st.nextToken());
		int korea = Integer.parseInt(st.nextToken());
		int hanyang = Integer.parseInt(st.nextToken());
		
		int sum = soongsil + korea + hanyang;
		
		int min = Math.min(soongsil, korea);
		min = Math.min(min, hanyang);
		
		if (sum >= 100) {
			System.out.println("OK");
		} else {
			if (min == soongsil) {
				System.out.println("Soongsil");
			} else if(min == korea) {
				System.out.println("Korea");
			} else {
				System.out.println("Hanyang");
			}
		}
		
	}
}
