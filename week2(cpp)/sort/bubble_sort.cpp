#include <iostream>

void bubble_sort(int *arr, int size) {
    int temp = 0;
    for(int i = 0; i < size; i++) {
        for(int j = 0; j < size - 1; j++) {
            if(arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int N;
    std::cin >> N;
    int arr[N];

    for(int i = 0; i < N; i++)
        std::cin >> arr[i];
    
    bubble_sort(arr, N);

    for(int i = 0; i < N; i++)
        std::cout << arr[i] << std::endl;

}