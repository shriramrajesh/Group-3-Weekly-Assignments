import java.io.*;
import java.util.Scanner;
public class Assignment {
	public static void main(String[] args) 
	  throws IOException
	  {
	   Scanner sc = new Scanner( System.in );
	   int i,p=1,l;
	   int[] j = new int [25];
	   System.out.println("Input:");
	   i=sc.nextInt();
	   for (int k=0;k<i;k++) {
		 j[k]=sc.nextInt();
		 p*=j[k];
		}
	   System.out.println("Output:");
	   System.out.print(p);
	  }
}
