import java.util.*;

class Solution {
    public int solution(int[][] game_board, int[][] table) {
        // int answer = -1;
        
        List<int[][]> game_list= getShape(game_board, 0);
        List<int[][]> table_list=getShape(table, 1);
        boolean[] used = new boolean[table_list.size()];
        
            
        int count = 0;
        
        for(int[][] game_shape : game_list){
            
            for (int i = 0; i < table_list.size(); i++) {
                if (used[i]) continue;

                if (canFit(game_shape, table_list.get(i))) {
                    used[i] = true;
                    count += cellCount(game_shape);
                    break;
                }
            }
        }
        
        return count;
    }
    
    private List<int[][]> getShape(int[][] blank, int target){
        int n = blank.length;
        int m = blank[0].length;
        boolean[][] visited = new boolean[n][m];
        List<int[][]> shape = new ArrayList<>();
        
        
        for(int i=0; i<n; i++){
            for(int j=0; j<blank[0].length; j++){
                if(blank[i][j] == target && !visited[i][j]){
                    shape.add(getBfsShape(blank,visited,i,j,target));                
                }
            }
        }
        
        return shape;
    }
    
    private int[][] getBfsShape(int[][] blank,boolean[][] visited, int r, int c, int target){
        Queue<int[]> que = new LinkedList<>();
        List<int[]> cell_list = new ArrayList<>();
        
        visited[r][c]=true;
        int n = blank.length;
        int m = blank[0].length;
        que.offer(new int[]{r,c});
        cell_list.add(new int[]{r,c});
        
        int minR=r, minC=c, maxR=r, maxC=c;
        
        
        int[] dr = {0,0,1,-1};
        int[] dc = {1,-1,0,0};
        
        while(!que.isEmpty()){
            int[] cell = que.poll();
            
            for(int i=0; i<4; i++){
                int row = cell[0] + dr[i];
                int col = cell[1] + dc[i];
                
                if(row < 0 || row >= n || col < 0 || col >= m || blank[row][col] != target || visited[row][col]) continue;
                
                que.offer(new int[]{row, col});
                visited[row][col]=true;
                cell_list.add(new int[]{row, col});
                
                if (minR > row) minR = row;
                if (minC > col) minC = col;
                if (maxR < row) maxR = row;
                if (maxC < col) maxC = col;
            }
        }
        
        int shape_r = maxR-minR + 1; 
        int shape_c = maxC-minC + 1; 
        
        int[][] shape = new int[shape_r][shape_c];
        
        for(int[] cell_part : cell_list){
            int cell_r = cell_part[0]-minR;
            int cell_c = cell_part[1]-minC;
            
            shape[cell_r][cell_c] = 1;
        }
        
        return shape;
    }
    
    private int cellCount(int[][] shape){
        int count = 0;
        for(int i =0; i<shape.length; i++){
            for(int j =0; j < shape[0].length; j++){
                if(shape[i][j] == 1)
                    count++;
            }
        }
        return count;
    }
    
     private boolean canFit(int[][] blank, int[][] piece) {
        
        if (cellCount(blank) != cellCount(piece)) return false;
        
        int[][] rotated = piece;
        for (int k = 0; k < 4; k++) {
            if (isSameShape(blank, rotated)) {
                return true;
            }
            rotated = rotate(rotated); 
        }
        return false;
    }
    
    private boolean isSameShape(int[][] a, int[][] b) {
        if (a.length != b.length) return false;
        if (a[0].length != b[0].length) return false;
        
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[0].length; j++) {
                if (a[i][j] != b[i][j]) return false;
            }
        }
        return true;
    }
    
    private int[][] rotate(int[][] shape){
        int n = shape.length;
        int m = shape[0].length;
        int[][] result = new int[m][n];
        
        for(int i =0; i<shape.length; i++){
            for(int j =0; j < shape[0].length; j++){
                int r = j;
                int c = n-1-i;
                
                result[r][c] = shape[i][j];
            }
        }
        return result;
        
    }
    
    
    
    
}