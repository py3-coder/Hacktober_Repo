import java.util.*;
public class Main
{
    void left_rotate(int arr[],int d ,int n){
        for(int i=0;i<d;i++){
            left_r(arr,n);
        }
    }
    void left_r(int arr[],int n){
        int i,temp;
        temp=arr[0];
        for(i=0;i<n-1;i++){
            arr[i] =arr[i+1];
        }
        arr[n-1] =temp;
    }
	public static void main(String[] args) {
	    Main rotate = new Main();
	    int arr[]=new int[]{1,2,3,4,5,6,7};
	    rotate.left_rotate(arr,4,7);
	    for(int i=0;i<7;i++){
	       System.out.println(i+": "+arr[i]+'\n'); 
	    }
	    
	}
}
