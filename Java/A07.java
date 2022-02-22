import java.io.*;
import java.util.Scanner;
public class Assignment {
	public static void main(String[] args) 
	  throws IOException
	  {
	   Scanner sc = new Scanner( System.in );
	   int i;
	   System.out.println("Input:");
	   i=sc.nextInt();
	   System.out.println("Output");
	   if ((i>=1)&& (i<=30))
		System.out.println("SMALL");
	   if ((i>=31)&& (i<=60))
		 System.out.println("MEDIUM");
	   if ((i>=61)&& (i<=100))
		   System.out.println("LARGE"); 
		}
	  }
