#include <iostream>
#include <vector>

int main() {
    std::vector<int> count_list;
    int N, M, count_w, count_b, min;
    char color;
    std::cin >> N >> M;
    int board[N][M];

    for(int i = 0; i < N; i++) {
        for(int j =0; j < M; j++) {
            std::cin >> color;
            if (color == 'B')
                board[i][j] = 0;  //black
            else
                board[i][j] = 1; //white
        }
    }

    for(int i = 0; i <  N - 7; i++) {
        for(int j = 0; j < M - 7; j++) {          //체스판 8 * 8 쪼개기
            count_w = 0;
            count_b = 0;
            for(int a = i; a < i + 8; a++) {
                for(int b = j; b < j + 8; b++) {
                    if((a + b) % 2 == 0) {
                        if (board[a][b] != 1) {
                            count_w++;
                        }
                        else {
                            count_b++;
                        }
                    }
                    else {
                        if(board[a][b] != 1) {
                            count_b++;
                        }
                        else
                            count_w++;

                    }
                }
            }
        
            count_list.push_back(count_w);
            count_list.push_back(count_b);
        }
    }
    min = count_list[0];
    for(int i = 0; i < count_list.size(); i++) {
        if (min > count_list[i]) {
            min = count_list[i];
        }
    }
    std::cout << min;
    return 0;
}