import java.util.Scanner;
  
public class Main{
  
  public static void main(String args[]){
    Scanner a = new Scanner(System.in);
    
    double  r = a.nextDouble();
    double area = 3.14159 * r * r;
    
    
    System.out.printf("A=%.4f\n", area);
    
  }
}
