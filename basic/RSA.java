import java.util.*;


public class Main {
	static int gcd(int a, int b) {
  		return a == 0 ? b : gcd(b % a, a);
	}

	public static void main(String[] args) {
		Integer p = 23;
		Integer q = 41;
		
		Integer n = p * q;
		System.out.println("n :" + n);
		
		Integer z = (p-1) * (q-1);
		System.out.println("z :" + z);
		
		int e = -1;
		for (int i=2; i < z; i++) {
			if (i % 2 != 0 && gcd(i, n) == 1) {
				e = i;
				break;
			}
		}
		
		System.out.println("e :" + e);
		
		int i = 1;
		int d = 0;
		int x = 1 + i * z;
		
		while (x % e != 0){
			i++;
			
			x = 1 + i * z;
		}
		
		d = x / e;
		
		System.out.println("d :" + d);
		
	}	
	
}
