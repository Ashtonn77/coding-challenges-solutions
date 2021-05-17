import java.util.Scanner;

public class Main {
        
   static int n;
   static int[] a = new int[2005];
   static int ans = 0;
    
    public static void dfs(int x, int s){
        
        if(x == -1) return;
            ans = Math.max(ans, s);
        
        dfs(a[x], s + 1);
        
    }
    
    
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        
        for(int i = 1; i <= n; i++){
            int x = in.nextInt();
            a[i] = x;
        }
        
        for (int i = 1; i <= n; i++){
            dfs(i, 1);
        }

        System.out.println(ans);
    
    }
}
