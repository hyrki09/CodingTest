import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        List<Integer> max_arr = new ArrayList<Integer>();
        List<Integer> min_arr = new ArrayList<Integer>();
        
        for(int[] size : sizes){
            int max = Arrays.stream(size).max().getAsInt();
            int min = Arrays.stream(size).min().getAsInt();
            max_arr.add(max);
            min_arr.add(min);
        }
        
        int best_max = Collections.max(max_arr);
        int best_min = Collections.max(min_arr);
        
        
        
        
        return best_max * best_min;
    }
}