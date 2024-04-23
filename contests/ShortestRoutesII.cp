#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
    long long n, m, q;
    cin >> n >> m >> q;
    
    vector<vector<long long>> dist(n, vector<long long>(n, LLONG_MAX));

    for (long long idx = 0; idx < m; ++idx) {
        long long a, b, c;
        cin >> a >> b >> c;
        dist[a - 1][b - 1] = min(dist[a - 1][b - 1], c);
        dist[b - 1][a - 1] = min(dist[b - 1][a - 1], c);
    }

    for (long long i = 0; i < n; ++i) {
        dist[i][i] = 0LL;
    }

    for (long long k = 0; k < n; ++k) {
        for (long long i = 0; i < n; ++i) {
            for (long long j = 0; j < n; ++j) {
                if (dist[i][k] != LLONG_MAX && dist[k][j] != LLONG_MAX) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    for (long long i = 0; i < q; ++i) {
        long long a, b;
        cin >> a >> b;
        long long ans = dist[a - 1][b - 1];
        cout << (ans == LLONG_MAX ? -1 : ans) << endl;
    }

    return 0;
}
