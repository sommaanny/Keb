#include <iostream>

//node 구조체 정의
struct Node {
    int data;
    // 부모 노드
    Node* parent;
    // 왼쪽 자식 노드
    Node* leftChild;
    // 오른쪽 자식 노드
    Node* rightChild;
};

class binarySearchTree {
    public:
        binarySearchTree() {root = nullptr;}
        void insert(int elem);
        Node* find(int elem);
        void swap(Node* a, Node* b);
        void erase(int elem);
        void erase(Node* node);
        void print(Node* node);
        Node* getRoot();
    private:
        Node* root;
};

//insert 함수
void binarySearchTree::insert(int elem) {
    //새로 삽입할 노드
    Node* addNode = new Node;
    //맨 처음 삽입이라면 루트에 넣어주기
    if (root == nullptr) {
        addNode->data = elem;
        addNode->parent = nullptr;
        addNode->leftChild = nullptr;
        addNode->rightChild = nullptr;
        root = addNode;
        return;
    }
    //맨 처음 삽입이 아닐경우
    //현재 노드를 가르키는 노드(초기값 root노드)
    Node* curNode = root;
    while(1) {
        //인풋값이 현재 노드를 가르키는 curNode의 값보다 작다면 왼쪽으로 이동
        while (curNode->data > elem) {
            //왼쪽 자식이 없으면 그 자리에 넣어주고 부모 자식값 다시 설정.
            if (curNode->leftChild == nullptr) {
                addNode->data = elem;
                addNode->parent = curNode;
                addNode->leftChild = nullptr;
                addNode->rightChild = nullptr;
                curNode->leftChild = addNode;
                return;
            }
            else //왼쪽 자식이 이미 있다면
            {
                //curNode가 자신의 왼쪽 자식노드를 참조하게 하고 위의 행동 반복
                curNode = curNode->leftChild;
            }
        }
        //인풋값이 curNode의 값보다 크다면
        while (curNode->data <= elem) {
            if (curNode->rightChild == nullptr) {
                addNode->data = elem;
                addNode->parent = curNode;
                addNode->leftChild = nullptr;
                addNode->rightChild = nullptr;
                curNode->rightChild = addNode;
                return;
            }
            else
                curNode = curNode->rightChild;
        }
    }
}
//find함수
Node* binarySearchTree::find(int elem) {
    //현재 노드
    Node* curNode = root;
    //트리가 비어있다면 nullptr 반환
    if (curNode == nullptr) return nullptr;

    while(1) {
        while (curNode->data > elem) {
            curNode = curNode->leftChild;
        }
        while (curNode->data <= elem) {
            if (curNode->data == elem) return curNode;
            curNode = curNode->rightChild;
        }
        //만약 트리를 다 순회했음에도 못찾았으면 nullptr반환
        if (curNode == nullptr) return nullptr;
    }
}

//erase함수에 사용하기 위한 swap함수
void binarySearchTree::swap(Node* a, Node* b) {
    //swap용 임시저장 노드
    Node* tmp = new Node;
    //a가 왼쪽 자식이라면
    if(a->parent->leftChild == a) {
        //b로 바꿈, a의 부모노드의 정보를 바꿀뿐 a노드의 정보는 살아있음
        a->parent->leftChild = b;
    }
    else a->parent->rightChild = b;
    //똑같이 b에대해 수행
    if(b->parent->leftChild == b) b->parent->leftChild = a;
    else b->parent->rightChild = a;
    //이제 a와 b의 부모노드의 정보는 세팅완료, a노드와 b노드의 정보를 수정해야함 그래야 binarySearchTree의 특징을 위배하지않음.
    tmp->data = b->data;
    b->data = a->data;
    a->data = tmp->data;

    tmp->parent = b->parent;
	b->parent = a->parent;
	a->parent = tmp->parent;

	tmp->leftChild = b->leftChild;
	b->leftChild = a->leftChild;
	a->leftChild = tmp->leftChild;

	tmp->rightChild = b->rightChild;
	b->rightChild = a->rightChild;
	a->rightChild = tmp->rightChild;

	delete(tmp);
}

void binarySearchTree::erase(int elem) {
    //매개변수로 들어온 elem값을 찾아서 트리에서 제거하는 함수
    //네 가지의 경우의 수가 있음(해당 노드가 리프노드일 때, 왼쪽자식만 가지고 있을 때, 오른쪽 자식만 가지고 있을 때, 둘 다 가지고 있을 때)
    Node* delNode = find(elem);
    if (delNode == nullptr) return;
    //삭제할 노드가 리프노드일 때
    if (delNode->leftChild == nullptr && delNode->rightChild == nullptr) {
        //해당 노드의 부모노드에서 해당 원소 제거
        if(delNode->parent->leftChild == delNode) delNode->parent->leftChild = nullptr;
        else delNode->parent->rightChild = nullptr;
    }
    //오른쪽 자식만 있을 때
    else if (delNode->leftChild == nullptr) {
        //만약 삭제할 노드가 부모노드의 왼쪽 자식이라면
        if (delNode->parent->leftChild == delNode) {
            delNode->parent->leftChild = delNode->rightChild;
        }
        else {
            delNode->parent->rightChild = delNode->rightChild;
        }
        //해당 원소의 오른쪽 자식의 부모노드를 해당 원소의 부모노드로 업데이트해준다
        delNode->rightChild->parent = delNode->parent;
    }
    //왼쪽 자식만 있을 때
    else if (delNode->rightChild == nullptr) {
        if (delNode->parent->leftChild == delNode) {
            delNode->parent->leftChild = delNode->leftChild;
        }
        else delNode->parent->rightChild = delNode->leftChild;
        
        delNode->leftChild->parent = delNode->parent;
    }
    //둘 다 있을 때는 삭제할 노드의 오른쪽 서브트리에서 제일 작은값과 교체
    else {
        //일단 오른쪽 서브트리의 루트노드부터 시작해서 반복문을 통해 제일 작은 값을 찾아줌
        Node* curNode = delNode->rightChild;
        while (curNode->leftChild != nullptr) {
            curNode = curNode->leftChild;
        }
        //두 노드를 바꿔주고
        swap(curNode, delNode);
        //해당 원소의 부모노드에서 해당 원소 제거
        if (delNode->parent->leftChild == delNode) {
            delNode->parent->leftChild = nullptr;
        }
        else delNode->parent->rightChild = nullptr;
    }
    delete delNode;
}

//지우려는 노드를 가르키는 포인터를 인수로받고 삭제하는 함수
void binarySearchTree::erase(Node* node) {
	//해당 원소가 리프 노드라면 
	if (node->leftChild == nullptr && node->rightChild == nullptr) {
		//해당 원소의 부모노드에서 해당 원소 제거
		if (node->parent->leftChild == node) node->parent->leftChild = nullptr;
		else node->parent->rightChild = nullptr;
	}
	//해당원소가 오른쪽 자식만 있을 때
	else if (node->leftChild == nullptr) {
		//만약 del노드가 del의 부모노드의 왼쪽자식이라면
		if (node->parent->leftChild == node) {
			node->parent->leftChild = node->rightChild;
		}
		//del노드가 부모노드의 오른쪽자식이라면
		else {
			node->parent->rightChild = node->rightChild;
		}
		//해당원소의 오른쪽자식의 부모노드를 해당원소의 부모노드로 설정
		node->rightChild->parent = node->parent;
	}
	//해당원소가 왼쪽 자식만 있을 때
	else if (node->rightChild == nullptr) {
		//del노드가 부모 노드의 왼쪽자식이라면
		if (node->parent->leftChild == node) {
			//부모노드의 왼쪽 자식을 해당원소의 왼쪽 자식으로 설정
			node->parent->leftChild = node->leftChild;
		}
		else {
			node->parent->rightChild = node->leftChild;
		}
		//해당원소의 왼쪽자식의 부모노드를 해당원소의 부모노드로 설정
		node->leftChild->parent = node->parent;
	}
	//해당 원소가 두 자식 다 있을 때 오른쪽 서브트리에서 제일 작은값과 교체
	else {
		//오른쪽 서브트리의 루르노드부터 시작해서
		Node* curNode = node->rightChild;
		//오른쪽 서브트리의 제일 작은 노드까지 
		while (curNode->leftChild != nullptr) {
			curNode = curNode->leftChild;
		}
		//두 노드를 바꿔주고
		swap(curNode, node);
		//해당 원소의 부모노드에서 해당 원소 제거
		if (node->parent->leftChild == node) node->parent->leftChild = nullptr;
		else node->parent->rightChild = nullptr;
	}
	delete(node);
}

//트리의 모든 원소를 출력해주는 print함수, 중위순회방식을 통해 출력
//중위순회란 왼쪽 자식 -> 현재 -> 오른쪽 자식 순으로 순회하는 것
void binarySearchTree::print(Node* node) {
    if (node == nullptr) return;
    print(node->leftChild);
    std::cout << node->data;
    print(node->rightChild);
}

Node* binarySearchTree::getRoot() {
    return root;
}

//ex)
int main() {
	binarySearchTree* bst=new binarySearchTree();
	bst->insert(5);
	bst->insert(2);
	bst->insert(3);
	bst->insert(4);
	bst->insert(1);
	bst->insert(6);
	bst->insert(7);
	
    //출력
	bst->print(bst->getRoot());
	std::cout << '\n';
	//3값 지우기
	bst->erase(3);
	bst->print(bst->getRoot());

	std::cout << '\n';
    //3값 다시 추가
	bst->insert(3);
	bst->print(bst->getRoot());
	std::cout << '\n';
    //3값 하나 더 추가
	bst->insert(3);
	bst->print(bst->getRoot());
	std::cout << '\n';
	//3노드를 매개변수로 줘서 3값 지우기
	bst->erase(bst->find(3));
	bst->print(bst->getRoot());
	std::cout << '\n';
	//3노드 찾아서 데이터값 출력
	std::cout<<bst->find(3)->data;
}
