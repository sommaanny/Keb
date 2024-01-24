#include <iostream>

int main() {
    int arr[9][9]{0};  //std::array<array<int, 9>, 9> arr;
    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < 9; j++) {
            std::cin >> arr[i][j];
        }
    }
    int max = arr[0][0];
    int max_idx[2]{0};

    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < 9; j++) {
            if(arr[i][j] > max) {
                max = arr[i][j];
                max_idx[0] = i;
                max_idx[1] = j;
            }
        }
    }

    std::cout << max << std::endl << max_idx[0] + 1 << " " << max_idx[1] + 1;
    return 0;
}
    
