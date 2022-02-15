#include <iostream>
#include <limits.h>
#include <queue>
#include <string.h>

using namespace std;

#define NUM_VERTICES 6

bool bfs(int G[NUM_VERTICES][NUM_VERTICES], int s, int d, int parent[]){
	bool visited[NUM_VERTICES];
	memset(visited, 0, sizeof(visited));
	
	queue<int> q;
	q.push(s);
	visited[s] = true;
	parent[s] = -1;
	
	while(!q.empty()){
		int u = q.front();
		q.pop();
		
		for(int v=0; v < NUM_VERTICES; v++){
			if(visited[v] == false && G[u][v] > 0){
				if(v == d){
					parent[v] = u;
					return true;
				}
				
				q.push(v);
				parent[v] = u;
				visited[v] = true;
			}
		}
	}
	
	return false;
}

int ford_fulkerson(int graph[NUM_VERTICES][NUM_VERTICES], int s, int t){
	int u, v;
	
	int G[NUM_VERTICES][NUM_VERTICES];
	
	for(u=0; u < NUM_VERTICES; u++){
		for(v=0; v < NUM_VERTICES; v++){
			G[u][v] = graph[u][v];
		}
	}
	
	int parent[NUM_VERTICES];
	int max_flow = 0;
	
	while(bfs(G, s, t, parent)){
		int path_flow = INT_MAX;
		
		// find the min resudal capacity in graph
		for(v = t; v != s; v = parent[v]){
			u = parent[v];
			path_flow = min(path_flow, G[u][v]);
		}
		
		// update the resudal capacities
		// even update the reverse capacities
		for(v = t; v != s; v = parent[v]){
			u = parent[v];
			
			G[u][v] -= path_flow;
			G[v][u] += path_flow;
		}
		
		max_flow += path_flow;
	}
	
	return max_flow;
}

int main(){
	int graph[NUM_VERTICES][NUM_VERTICES]
        = { { 0, 16, 13, 0, 0, 0 }, { 0, 0, 10, 12, 0, 0 },
            { 0, 4, 0, 0, 14, 0 },  { 0, 0, 9, 0, 0, 20 },
            { 0, 0, 0, 7, 0, 4 },   { 0, 0, 0, 0, 0, 0 } };
 
    cout << "The maximum possible flow is "
         << ford_fulkerson(graph, 0, 5);
 
    return 0;
}