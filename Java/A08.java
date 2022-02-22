import java.io.*;
import java.util.Scanner;
public class Assignment {
	public static void main(String[] args) 
	  throws IOException
	  {
	   Scanner sc = new Scanner( System.in );
	   BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	   String a;
	   int i;
	   System.out.println("Input:");
	   a=br.readLine();
	   i=sc.nextInt();
	   System.out.println("Output");
	   System.out.println(a);
	   System.out.println(i);
		}
	  }
