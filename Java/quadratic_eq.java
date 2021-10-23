import java.util.Scanner;  
public class QuadraticEquation  
{  
    public static void main(String[] Strings)   
    {  
         Scanner input = new Scanner(System.in);  
         System.out.print("Enter the value of p: ");  
         double p = input.nextDouble();  
         System.out.print("Enter the value of q: ");  
         double q = input.nextDouble();  
         System.out.print("Enter the value of r: ");  
         double r = input.nextDouble();  
         double d= q * q - 4.0 * p * r;  
         if (d> 0.0)   
         {  
             double r1 = (-q + Math.pow(d, 0.5)) / (2.0 * p);  
             double r2 = (-q - Math.pow(d, 0.5)) / (2.0 * p);  
             System.out.println("The roots are " + r1 + " and " + r2);  
         }   
         else if (d == 0.0)   
         {  
             double r1 = -q / (2.0 * p);  
             System.out.println("The root is " + r1);  
         }   
         else   
         {  
              System.out.println("Roots are not real.");  
          }  
      }  
}  
