class Main
{
    static int majorityElement(int a[], int size)
    {
        int temp,co;
        int r=-1;
        int count =0;
        for(int i=0;i<size;i++){
            temp=a[i];
            co =counter(a,temp);
            if(co > (size/2)){
                r=temp;
            }
            else{
                if(r<0){
                r =-1;
            }
            }
        }
        System.out.println(r);
        return r;
        
    }
    static int counter(int a[],int num){
        int count=0;
        for(int i=0;i<a.length;i++){
            if (a[i] == num){
                count +=1;
            }
        }
        return count;
    }
    public static void main(String args[]){
        int a[] =new int[]{1,13,1};
        int size =a.length;
        majorityElement(a,size);
    }
}
