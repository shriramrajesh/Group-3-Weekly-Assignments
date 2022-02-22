import java.io.*;
import java.util.Scanner;
public class Assignment {
	public static void main(String[] args) 
	  throws IOException
	  {
	   Scanner sc = new Scanner( System.in );
	   int i,s=0;
	   int[] j = new int [50];
	   System.out.println("Input:");
	   i=sc.nextInt();
	   for (int k=0;k<i;k++) {
		 j[k]=sc.nextInt();
		 s+=j[k];
		}
	   System.out.println("Output:");
	   System.out.print(s);
	  }
}
