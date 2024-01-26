#include <iostream>
#include <vector>

int main() {
    int N, min;
    int three = 0;
    int five = 0;
    std::vector<int> result;
    std::cin >> N;
    five = N / 5;
    if(five == 0) {
        if(N == 3){
            std::cout << "1";
            return 0;
        }
        else {
            std::cout << "-1";
            return 0;
        }
    }
    else{
    while(five >= 0) {
        three = 0;
        while(1) {
            if(five * 5 + three * 3 == N) {
                result.push_back(five + three);
                three++;
            }
            else if(five * 5 + three * 3 > N) {
                break;
            }
            else
                three++;
        }
        five--;
    }
    }

    if(result.size() == 0)
        std::cout << "-1";
    else {
        min = result[0];
        for(int i = 0; i < result.size(); i++) {
            if(min > result[i])
                min = result[i];
        }
        std::cout << min;
    }
    return 0;
}