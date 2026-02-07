package exercises;

import java.util.*; 
import java.io.*;

class Main {
  public static long getFactorial(int num) {
    if( num <= 1) return 1;
    return num * getFactorial(num-1);
  }

  public static String RecursionChallenge(int num) {
    String challengeToken = "hbs2oim9c1a";
    String factorialString = getFactorial(num) + "";
    String result = "";
    int maxLength = Math.max(factorialString.length(), challengeToken.length());

    for(int i = 0; i < maxLength; i++) {
      if (i < factorialString.length()) {
        result += factorialString.charAt(i);
      }
      if (i < challengeToken.length()) {
        result += challengeToken.charAt(i);
      }
    }

    return result;
  }

  public static void main (String[] args) {  
    // keep this function call here     
    Scanner s = new Scanner(System.in);
    // System.out.print(RecursionChallenge(s.nextLine())); 

  }}
