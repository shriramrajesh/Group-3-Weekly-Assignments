import java.io.*;
import java.util.Scanner;
public class Assignment {
	public static void main(String[] args) 
	  throws IOException
	  {
	  Scanner sc = new Scanner( System.in );
	  int i;
	  String j="";
	  System.out.println("Input");
	  i=sc.nextInt();
	  j+=i;
	  System.out.println("Output");
	  System.out.println(j);
	  System.out.println(j.getClass().getSimpleName());
	  System.out.println("Conversion Successful");
	}
}
