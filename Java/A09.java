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
	   if((i%2!=0)||((i%2==0)&&(i>=6)&&(i<=20)))
		   System.out.println("Weird");
	   if(((i%2==0)&&(i>=2)&&(i<=5))||((i%2==0)&&(i>=20)))
		   System.out.println("Not Weird");   
		}
	  }
