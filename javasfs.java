import java.util.ArrayList;  
import java.util.List;  
  
public class Graph {  
    private List<Integer>[] adj; // 邻接表  
    private int V;  // 顶点数目  
    private int E;  // 边的数目  
      
    public Graph(int V) {  
        this.V = V;  
        adj = (List<Integer>[])new List[V];  
        E = 0;  
        for (int i = 0; i < V; i++) {  
            adj[i] = new ArrayList<Integer>();  
        }  
    }  
      
    public void addEdge(int v, int w) {  
        adj[v].add(adj[v].size(), w);  
        adj[w].add(adj[w].size(), v);  
        E++;  
    }  
      
    public List<Integer> adj(int v) {  
        return adj[v];  
    }  
      
    public int V() {  
        return V;  
    }  
      
    public int E() {  
        return E;  
    }  
      
    public String toString() {  
        String s = V + " 个顶点, " + E + " 条边\n";  
        for (int i = 0; i < V; i++) {  
            s += i + ": ";  
            for (Integer node : adj(i)) {  
                s += node + " ";  
            }  
            s += "\n";  
        }  
        return s;  
    }  
  
}  


import java.util.Stack;  
      
public class DepthFirstSearch {  
    private boolean[] isMarked;  
    private int begin;  
    private int count;  
    private Integer[] edgeTo;   
      
    public DepthFirstSearch(Graph g, int begin) {  
        isMarked = new boolean[g.V()];  
        edgeTo = new Integer[g.V()];  
        count = 0;  
        this.begin = begin;  
        dfs(g, begin);  
    }  
      
    public void dfs(Graph g, int begin) {  
        isMarked[begin] = true;  
        for (Integer i : g.adj(begin)) {  
            if (!isMarked[i]) {  
                edgeTo[i] = begin;  
                count++;  
                dfs(g, i);  
            }  
        }  
    }  
      
      
    public boolean hasPath(int v) {  
        return isMarked[v];  
    }  
      
    public int count() {  
        return count;  
    }  
      
    public String pathTo(int v) {  
        if (!hasPath(v)) return "";  
        Stack<Integer> stack = new Stack<>();  
        stack.push(v);  
        for (int i = v; i != begin; i = edgeTo[i]) {  
            stack.push(edgeTo[i]);  
        }  
          
        return stack.toString();  
    }  
      
      
}  

import java.util.LinkedList;  
import java.util.Queue;  
import java.util.Stack;  
  
public class BreadthFirstSearch {  
      
    private boolean[] isMarked;  
    private Integer[] edgeTo;  
    private int begin;  
    private int count; // 多少个点连通  
      
    public BreadthFirstSearch(Graph g, int begin) {  
        isMarked = new boolean[g.V()];  
        edgeTo = new Integer[g.V()];  
        this.begin = begin;  
        count = 0;  
        bfs(g, begin);  
    }  
      
    private void bfs(Graph g, int begin) {  
        Queue<Integer> queue = new LinkedList<>();  
        isMarked[begin] = true;  
        queue.offer(begin);  
        while (!queue.isEmpty()) {  
            Integer temp = queue.poll();  
            for (Integer i : g.adj(temp)) {  
                if (!isMarked[i]) {  
                    isMarked[i] = true;  
                    count++;  
                    edgeTo[i] = temp;  
                    queue.offer(i);  
                }  
            }  
        }  
    }  
      
    public boolean hasPath(int v) {  
        return isMarked[v];  
    }  
      
    public int count() {  
        return count;  
    }  
      
    public String pathTo(int v) {  
        if (!hasPath(v)) return "";  
        Stack<Integer> stack = new Stack<>();  
        stack.push(v);  
        for (int i = v; i != begin; i = edgeTo[i]) {  
            stack.push(edgeTo[i]);  
        }  
          
        return stack.toString();  
    }  
  
}  