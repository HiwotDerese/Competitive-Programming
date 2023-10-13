#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<vector<int>> graph(m, vector<int>(3));
    for (int i = 0; i < m; i++) {
        cin >> graph[i][0] >> graph[i][1] >> graph[i][2];
    }

    vector<double> dist(n, INFINITY);
    dist[0] = 0.0;

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < m; j++) {
            int u = graph[j][0];
            int v = graph[j][1];
            int w = graph[j][2];
            if (dist[u - 1] != INFINITY && dist[u - 1] + w < dist[v - 1]) {
                dist[v - 1] = dist[u - 1] + w;
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < k; i++) {
        int s, y;
        cin >> s >> y;

        if (dist[s - 1] >= y) {
            ans += 1;
        } else {
            dist[s - 1] = y;
        }
    }

    cout << ans << endl;

    return 0;
}
