#include <iostream>
#include <vector>

using namespace std;

vector<int> v; //arr의 처음 노드를 1로하기 위해 새로운 vector생성해서 0을 미리 넣자

void buildHeap(int* arr, int* end) { //heap형태로 만들자 여기선 maxHeap
    int root = 1, parent = 1, child = 1;
    v.push_back(0); //처음에 0을 넣어 처음 노드의 인덱스를 1로 만들어줌
    for (int i = 0; i < end - arr; i++)
        v.push_back(arr[i]);
    for (int i = end - arr - 1; i > 1; i--) { //maxHeap구현 자식노드부터 접근
        child = i;
        parent = child / 2;  //완전이진트리의 특징
        while(v[child] > v[parent] && parent != 0) { //자식이 부모보다 크다면 바꿔줌
            int tmp = v[child];
            v[child] = v[parent];
            v[parent] = tmp;
            child = parent; //인덱스도 업데이트
            parent = child / 2;
        }
    }
}

void heapify(int start, int end) { // 마지막 노드와 부모 노드를 바꾸고 원래자리 찾아오는 함수
    int current = start;
    int leftchild = 2 * current; // 왼쪽 자식의 인덱스번호 -> 완전이진트리의 특징
    int rightchild = 2 * current + 1;

    if(leftchild <= end && v[current] < v[leftchild]) current = leftchild;
    if(rightchild <= end && v[current] < v[rightchild]) current = rightchild;

    if (start != current) { //current 인덱스가 움직였다는 뜻. 즉, 트리의 변경이 일어났고, 부모보다 큰 자식노드가 있다.
        swap(v[start], v[current]); //해당 current노드 값과 시작값(부모노드)을 바꿔주고
        heapify(current, end); //해당 current노드에서부터 연쇄적으로 다시 정렬시작
    }
}

void heapSort(int* arr, int* end) {
    buildHeap(arr, end); //먼저 Heap을 만들어준다.
    for (int i = end - arr; i > 1; i--) {
        swap(v[1], v[i]); //루트 노드와 마지막 노드의 값을 바꿔준다. i가 줄어들고 있음으로 정렬된 마지막 노드는 접근하지 않음
        heapify(1, i - 1); //바꿔준 값을 정렬한다.
    }
    //Heap정렬이 완료된 값들을 다시 원레 arr로 옮겨준다. 앞에 0을 넣어놨음으로 1부터 끝까지만 넣어준다.
    for(int i = 0; i < v.size() - 1; i++) {
        arr[i] = v[i + 1];
    }

}

int main() {
    int arr[8] = {9, 6, 7, 5, 3, 1, 4, 2}; // 정렬하고 싶은 배열
    heapSort(arr, arr + 8);
    for (int i = 0; i < 8; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}