#include <iostream>

#define MAX_TABLE 1000 // 예시: 해시 테이블의 최대 크기를 1000으로 정의

int hash(const char * str) {
	int hash = 401;
	int c;

	while (*str != '\0') {
		hash = ((hash << 4) + (int)(*str)) % MAX_TABLE;
		str++;
	}

	return hash % MAX_TABLE;
}