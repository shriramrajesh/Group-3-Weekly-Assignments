import java.io.*;
public class Assignment {
	public static void main(String[] args) 
	  throws IOException
	  {
	  BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
	  String str;
	  String[] a= new String[10];
	  int i;
	  System.out.println("Input");
	  for(i=0;i<5;i++)
	  {
		  str=br.readLine();
		  a[i]=str;
	  }
	  System.out.println("Output");
	  for(i=0;i<5;i++)
		  System.out.println(a[i]); 
	}
}
