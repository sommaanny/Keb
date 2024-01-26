#include <iostream>

using namespace std;

struct Point {
    int x, y;
};

void merge(Point* p, int s, int e) {
    int mid = (s + e) / 2;
    int n1 = mid - s + 1;
    int n2 = e - mid;

    Point L[n1], R[n2];
    for (int i = 0; i < n1; i++) L[i] = p[s + i];
    for (int i = 0; i < n2; i++) R[i] = p[mid + 1 + i];

    int i = 0, j = 0, k = s;
    while(i < n1 && j < n2) {
        if(L[i].x < R[j].x || (L[i].x == R[j].x && L[i].y <= R[j].y))
            p[k++] = L[i++];
        else
            p[k++] = R[j++];
    }
    while(i < n1)
        p[k++] = L[i++];
    while(j < n2)
        p[k++] = R[j++];
}

void merge_sort(Point* p, int start, int end) {
    if (start < end) {
        int mid = (start + end) / 2;
        merge_sort(p, start, mid);
        merge_sort(p, mid + 1, end);
        merge(p, start, end);
    }
}

int main() {

    ios::sync_with_stdio(false);
	cin.tie(NULL);

    int N;
    cin >> N;
    Point points[N];
    for(int i = 0; i < N; i++)
        cin >> points[i].x >> points[i].y;
    
    merge_sort(points, 0, N -1);

    for(int i = 0; i < N; i++) {
        cout << points[i].x << " " << points[i].y << "\n";
    }

    return 0;
}