#include <stdio.h>

int sum_mults_3_5(){
	int sum = 0;
	for (int i = 3; i < 1000; i++){
		if (i % 3 == 0 || i % 5 == 0){
			sum += i;
		}
	}
	return sum;
}

int main(){
	printf("%d\n", sum_mults_3_5());

	return 0;
}
