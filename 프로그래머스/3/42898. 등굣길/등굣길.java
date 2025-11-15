import java.util.Arrays;
class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int num = 1000000007;
        
        int[][] miniMap = new int[n+1][m+1];
        boolean[][] puddle = new boolean[n+1][m+1];
        miniMap[1][1] = 1;
        // miniMap[n][m] = 1;
        for(int[] p : puddles){
            int y = p[0];
            int x = p[1];
            puddle[x][y] = true;
        }
        
        for(int i =1; i <= n; i++){
            for(int j=1; j <= m; j++){
                if (puddle[i][j]){
                    miniMap[i][j] = 0;
                    continue;
                }
                
                if (i==1 && j==1) continue;
                
                miniMap[i][j] = (miniMap[i-1][j] + miniMap[i][j-1]) %num;
                
                    
            }
        }
        
        return miniMap[n][m] ;
    }
}