import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        
        
        List<List<Integer>> graph = new ArrayList<>();
        for(int i=0; i<=n; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] wire : wires){
            int a = wire[0];
            int b = wire[1];
            
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        
        
        for(int[] wire : wires){
            int start_wire = wire[0];
            int end_wire = wire[1];
            
            int count = bfsCount(graph, start_wire, end_wire,n);
            int diff = Math.abs((n-count) - count);
            answer = Math.min(answer, diff);
        }
        
        
        
        
        return answer;
    }
    
    private int bfsCount(List<List<Integer>> graph,int a,int b, int n){
        boolean[] visited = new boolean[n+1];
        Queue<Integer> queue = new LinkedList<>();
        
        queue.offer(a);
        visited[a] = true;
        int count = 1;
        
        while(!queue.isEmpty()){
            int x = queue.poll();
            
            for(int num : graph.get(x)){
                if((x==a && num ==b) || (x==b && num==a)) continue;
                
                if(!visited[num]){
                    queue.offer(num);
                    visited[num]=true;
                    count++;
                }
            }
            
        }
        
        return count;
    }
}