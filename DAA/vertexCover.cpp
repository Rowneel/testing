#include <bits/stdc++.h>

using namespace std;

// Graph representation using adjacency list
class Graph {
public:
    int V;
    vector<vector<int>> adjList;

    Graph(int V) {
        this->V = V;
        adjList.resize(V);
    }

    void addEdge(int u, int v) {
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }
};

// Greedy algorithm for Vertex Cover Problem
unordered_set<int> vertexCover(Graph& graph) {
    unordered_set<int> cover;

    // Initialize the set of uncovered edges
    vector<bool> visited(graph.V, false);
    for (int u = 0; u < graph.V; u++) {
        for (int v : graph.adjList[u]) {
            if (!visited[u] && !visited[v]) {
                cover.insert(u);
                cover.insert(v);
                visited[u] = visited[v] = true;
            }
        }
    }

    return cover;
}

// Driver code
int main() {
    Graph graph(4);
    graph.addEdge(0, 1);
    graph.addEdge(1, 2);
    graph.addEdge(2, 3);

    unordered_set<int> cover = vertexCover(graph);

    cout << "Vertex cover: ";
    for (int v : cover) {
        cout << v << " ";
    }
    cout << endl;

    return 0;
}
