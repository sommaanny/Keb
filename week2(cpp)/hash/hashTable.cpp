#include <iostream>

#define MAX_TABLE	8191
#define MAX_KEY		64

typedef long long ll;

using namespace std;

typedef struct Hash {
	char key[MAX_KEY + 1];
	int data;
} Hash;
Hash table[MAX_TABLE];

ll hashGen(char key[]) {
	ll h = 5381;
	while (*key != '\0')
		h = (((h << 5) + h) + *key++) % MAX_TABLE;
	return h;
}

int m_strcmp(const char* str1, const char* str2) {
	while (*str1 != '\0' || *str2 != '\0') {
		if (*str1 != *str2) return *str1 - *str2;
		str1++; str2++;
	}
	return 0;
}

void m_strcpy(char dsc[], char src[]) {
	while (*src != '\0')
		*(dsc++) = *(src++);
}

int hashDelete(char key[]) {
	ll h = hashGen(key);
	int cnt = MAX_TABLE;

	while (table[h].key[0] != 0 && cnt--) {
		if (!m_strcmp(table[h].key, key)) {
			table[h].key[0] = 0;
			table[h].data = 0;
			return 1;
		}
		h = (h + 1) % MAX_TABLE;
	}
	return 0;
}

int hashAdd(char key[], int data) {
	ll h = hashGen(key);
	int cnt = MAX_TABLE;

	while (table[h].key[0] != 0 && cnt--) {
		if (!m_strcmp(table[h].key, key)) {
			table[h].data = data;
			return 1;
		}
		else cout << "[충돌 발생]\n";
		h = (h + 1) % MAX_TABLE;
	}

	if (cnt == -1) return 0;
	m_strcpy(table[h].key, key);
	table[h].data = data;
	return 1;
}

int hashFind(char key[], int* data) {
	ll h = hashGen(key);
	int cnt = MAX_TABLE;

	while (table[h].key[0] != 0 && cnt--) {
		if (!m_strcmp(table[h].key, key)) {
			*data = table[h].data;
			return 1;
		}
		h = (h + 1) % MAX_TABLE;
	}
	return 0;
}

int main(void) {
	while (true) {
		char key[64];
		int data;
		char c;
		cout << "[명령]\n1. 삽입\n2. 찾기\n3. 삭제\n4. 테이블 조회\n5. 종료\n→ ";
		cin >> c;

		switch (c) {
		case '1':
			cout << "[Key, Data 입력] ";
			cin >> key >> data;
			if (hashAdd(key, data)) cout << "[성공] 입력 완료\n";
			else cout << "[실패] 해시가 가득 찼습니다.\n";
			cout << "-----------------------------\n";
			break;
		case '2':
			cout << "[Key 입력] ";
			cin >> key;
			if (hashFind(key, &data)) cout << "[성공] " << data << '\n';
			else cout << "[실패] 존재하지 않는 데이터입니다.\n";
			cout << "-----------------------------\n";
			break;
		case '3':
			cout << "[Key 입력] ";
			cin >> key;
			if (hashDelete(key)) cout << "[성공] 삭제되었습니다.\n";
			else cout << "[실패] 존재하지 않는 데이터입니다.\n";
			cout << "-----------------------------\n";
			break;
		case '4':
			for (int i = 0; i < MAX_TABLE; i++)
				cout << "[" << i << "] " << table[i].key << ", " << table[i].data << '\n';
			cout << "-----------------------------\n";
			break;
		case '5':
			return 0;
		default:
			cout << "잘못 입력하였습니다.\n";
			cout << "-----------------------------\n";
			continue;
		}
	}

	return 0;
}