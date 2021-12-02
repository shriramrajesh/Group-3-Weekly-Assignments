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
	   for(int j=1;j<11;j++)
		   System.out.println(i+"*"+j+"="+i*j);  
		}
	  }
