#include <iostream>
#include <queue>

using namespace std;
queue<int> Q[10]; // 0~9까지의 버킷

int max_value(int* arr, int size) {
    int max = 0;
    for(int i = 0; i < size; i++) {
        if (max < arr[i]) max = arr[i];
    }
    return max;
}

void radixSort(int* arr, int size) {
    int max = max_value(arr, size);
    int radix = 1; // 최대 자릿수를 구하기 위해 사용될 변수
    while(1) {
        if (radix >= max) break; //ex) radix가 1000에서 멈춘다면 max자릿수는 3자리수
        radix = radix * 10;
    }
    for (int i = 1; i < radix; i = i * 10) { //1의 자리부터 10씩 곱하면서 최대 자릿수까지 반복
        for (int j = 0; j < size; j++) { //모든 배열 탐색
            int k;
            if (arr[j] < i) k = 0; // i자릿수보다 작은 숫자는 모두 0버킷에 저장
            else k = (arr[j] / i) % 10; //그게 아니라면 해당 자리수의 값에 해당하는 버킷에 저장
            Q[k].push(arr[j]); // 해당 버킷에 저장
        }

        int idx = 0;
        for (int j = 0; j < 10; j++) //0~9까지 Queue에 저장된 값들을 순차적으로 빼내기 위한 반복문
        {
            while (Q[j].empty() == 0) // 해당 index번호의 버킷이 빌 때까지 빼낸다.
            {
                arr[idx] = Q[j].front(); //하나씩 빼서 배열에 다시 저장
                Q[j].pop();
                idx++;
            }
        }
    }
}

int main() {
    int arr[10] = {41, 152, 2, 73, 33, 674, 1247, 28, 388, 69};
    radixSort(arr, 10);
    for(int i = 0; i < 10; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}