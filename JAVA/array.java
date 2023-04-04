import java.util.Scanner;

public class array {
    public static void main(String[] args){
        Scanner scn=new Scanner(System.in);
        int n=scn.nextInt();
        int arr[] = new int[n];
        for (int i=0;i<n;i++)
        arr[i]=scn.nextInt();
        int se=0,so=0,p=1;
        for (int i=0;i<n;i++){
            System.out.println(arr[i]&1);
            if (arr[i]%2==0)
                se+=arr[i];
            else
                so+=arr[i];
            p*=arr[i];

        }
        System.out.print(se+" "+so+" "+p);

    }
    
}
