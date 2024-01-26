#include <iostream>
#include <vector>

using namespace std;

vector<int> result(1000001);
vector<int> arr;

void merge(int start, int end) {
    int mid = (start + end) / 2;
    int i = start;
    int j = mid + 1;
    int k = start;  // result배열의 인덱스
    while(i <= mid && j <= end) {
        if(arr[i] <= arr[j]) {
            result[k++] = arr[i++];
        }
        else
            result[k++] = arr[j++];
    }
    //합병정렬 후 남은 원소들 삽입
    while(i <= mid) {
        result[k++] = arr[i++];
    }
    while(j <= end) {
        result[k++] = arr[j++];
    }
    //원래 배열에 다시 저장
    for(int i = start; i<=end; i++) arr[i] = result[i];
}

void merge_sort(int start, int end) {
    if(start < end) {
        int mid = (start + end) / 2;
        merge_sort(start, mid);
        merge_sort(mid + 1, end);
        merge(start, end);
    }
}

int main() {
    int N;
    int num;
    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> num;
        arr.push_back(num);
    }

    merge_sort(0, N - 1);

    for(int i = 0; i < N; i++) {
        cout << arr[i] << "\n";
    }

    return 0;
}