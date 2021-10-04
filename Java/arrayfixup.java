//Array fix up code :
//arr[i]=i if not present then arr[i] =-1
import java.lang.*;
import java.util.*;
public class Main{
    void Array_fix(int arr[],int n){
        int temp;
        for(int i =0;i<n;i++){
            for (int j=0;j<n;j++){
                if(arr[j]==i){
                    temp=arr[j];
                    arr[j] =arr[i];
                    arr[i] =temp;
                    break;
                }
            }
        }
    for(int i=0;i<n;i++){
        if(arr[i] != i){
            arr[i] = -1;
        }
    }
}
void print(int arr[]){
    for(int i=0;i<arr.length;i++){
        System.out.println(i+":"+arr[i]);
    }
}
public static void main(String args[]){
    int arr[] =new int []{2,3,5,7,8,1,4};
    Main obj =new Main();
    obj.Array_fix(arr,arr.length);
    obj.print(arr);
}
}

