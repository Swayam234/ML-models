import java.util.*;
class Calculator
{
    public static void main(String args[])
    {
        int choice,n1,n2;
        Scanner sc= new Scanner(System.in);
        do
        {
         System.out.println("Calculator");
         System.out.println("1.Addition");
         System.out.println("2.Subtraction");
         System.out.println("3.Multiplication");
         System.out.println("4.Division");
         System.out.println("5.Exit");
         System.out.print("Enter choice:");
         choice=sc.nextInt();
         switch(choice)
         {
            case 1:System.out.print("Enter number 1:");
                   n1=sc.nextInt();
                   System.out.print("Enter number 2:");
                   n2=sc.nextInt();
                   System.out.println("The sum is:"+(n1+n2));
                   break;   
            case 2:System.out.print("Enter number 1:");
                   n1=sc.nextInt();
                   System.out.print("Enter number 2:");
                   n2=sc.nextInt();
                   System.out.println("The difference is:"+(n1-n2));
                   break;      
            case 3:System.out.print("Enter number 1:");
                   n1=sc.nextInt();
                   System.out.print("Enter number 2:");
                   n2=sc.nextInt();
                   System.out.println("The product is:"+(n1*n2));
                   break;      
            case 4:System.out.print("Enter number 1:");
                   n1=sc.nextInt();
                   System.out.print("Enter number 2:");
                   n2=sc.nextInt();
                   System.out.println("The division is:"+(n1/n2));
                   break; 
            case 5:break;       
            default: System.out.println("Invalid");      
         }
        }while(choice!=5);
        
    }
}