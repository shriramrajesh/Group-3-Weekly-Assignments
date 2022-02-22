import java.io.*;
import java.util.Scanner;
public class Assignment {
	public static void main(String[] args) 
	  throws IOException
	  {
	   Scanner sc = new Scanner( System.in );
	   int i;
	   System.out.println("Input");
	   i=sc.nextInt();
	   System.out.println("Output");
	   if(i%2==0)
	    System.out.println("GOOD");
	   else
		   System.out.println("BAD");
	}
}
