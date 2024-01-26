#include <iostream>
#include <vector>

using namespace std;

void quickSort(int *data, int start, int end) {
    if(start < end) {
        int pivot = start; // 기준값
        int i = start + 1; // pivot을 제외하고 앞에서부터 pivot보다 큰 값을 찾는 포인터
        int j = end; //pivot을 제외하고 뒤에서부터 pivot 보다 작은 값을 찾는 보인터

        while (i <= j) { //포인터가 엇갈릴 때까지 반복
            while (data[i] <= data[pivot] && i <= end) i++; //기준값 보다 큰 값을 만날 때까지 오른쪽으로 이동
            while (data[j] >= data[pivot] && j > start) j--;
            if (i > j) { //현재 엇갈린 상태면 pivot 값과 j값을 바꿈 교체
                int temp = data[j];
                data[j] = data[pivot];
                data[pivot] = temp;
            }
            else // 엇갈리지 않는 상태면 i값과 j값을 바꿈
            {
                int temp = data[j];
                data[j] = data[i];
                data[i] = temp;
            }
        }
        //분할 계산
        quickSort(data, start, j - 1);
        quickSort(data, j + 1, end);
    }
    else //원소가 1개인 경우
        return;
}

int main() {
    int data[7] = {9, 3, 8, 5, 4, 1, 2};

    quickSort(data, 0, 6);

    for (int i = 0; i < 7; i++)
       cout << data[i] << " ";
    cout << "\n";
    return 0;
}