#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<pair<int, int>> sizes(n);
    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        sizes[i] = {a, b};
    }

    sort(sizes.begin(), sizes.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return (a.first - a.second) > (b.first - b.second);
    });

    int compress_size = 0;
    int initial_size = 0;
    for (const auto& size : sizes) {
        initial_size += size.first;
        compress_size += size.second;
    }

    if (compress_size > m) {
        cout << -1 << endl;
    } else if (initial_size == m) {
        cout << 0 << endl;
    } else {
        int count = 0;
        for (const auto& size : sizes) {
            initial_size -= size.first - size.second;
            count++;
            if (initial_size <= m) {
                break;
            }
        }
        cout << count << endl;
    }

    return 0;
}
