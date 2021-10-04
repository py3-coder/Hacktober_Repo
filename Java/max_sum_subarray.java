import java.util.*;

public class Main
{
    static int  max_sum_subarray(int arr[],int n){
        int sum_end =0;
		int sum_curr =0;
		for(int i=0;i<n;i++){
		    sum_end =sum_end+arr[i];
		
		if(sum_end >sum_curr){
		    sum_curr =sum_end;
		}
		if(sum_end<0){
		    sum_end =0;
		}
		}
		return sum_curr;
    }
    
	public static void main(String[] args) {
	int arr[] = {-2, -3, 4, -1, -2, 1, 5, -3};
	int n =arr.length;
	max_sum_subarray(arr,n);
	
	}
}

