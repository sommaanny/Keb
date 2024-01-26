#include <iostream>

using namespace std;

void counting_sort(int* arr, int size) {
    int* counting_list, *sorted;
    int max = 0;
    for (int i = 0; i < size; i++)
        if(arr[i] > max) max = arr[i];
    counting_list = new int[max + 1]{0}; //0으로 초기화하지 않으면 쓰레기값이 들어가 누적합에서 이상이 발생함
    //max + 1로 하는 이유는 0부터 시작해 max에서 끝나기 때문이다.
    sorted = new int[size]{0}; //인덱스 번호와 카운팅수를 뒤집을 때 쓰이는 배열
    
    for(int i = 0; i < size; i++) counting_list[arr[i]]++;

    //누적합
    for(int i = 1; i < max + 1; i++) counting_list[i] += counting_list[i - 1];

    //인덱스 번호와 카운팅 수를 뒤집기
    for(int i = 0; i < size; i++) {
        sorted[counting_list[arr[i]] - 1] = arr[i]; //counting_list[[arr[i]] - 1]는 해당 원소의 값보다 작은 값들이 몇 번 나왔는지를 알려줌(누적합) 즉, 해당 숫자 밑에 n개가 있으니 해당 숫자는 n번 째
        counting_list[arr[i]]--;
    }

    //arr에 다시 할당
    for(int i = 0; i < size; i++) arr[i] = sorted[i];
    //동적할당 해제
    delete[] counting_list;
    delete[] sorted;
}

int main() {
    int N;
    cin >> N;
    int arr[N];
    for(int i = 0; i < N; i++)
        cin >> arr[i];
    counting_sort(arr, N);

    for(int i = 0; i < N; i++)
        cout << arr[i] << "\n";

    return 0;
}