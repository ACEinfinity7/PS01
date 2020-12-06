package binaryToHex;

import java.util.Scanner;

public class BinaryToHex {
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter a binary number: ");
		String input = scanner.next();
		int num = Integer.parseInt(input,2);
		System.out.print(input);
		
		char hex_chars[] = 
		{'1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
		
		String output = "";
		
		while(num > 0) {
			int remaining = num % 16;
			System.out.printf(remaining + "\n");
			output = hex_chars[remaining-1] + output;
			num = num / 16;
		}
		
		System.out.print("Binary Number in Hexadecimal: ");
		System.out.print(output);
	}

}

