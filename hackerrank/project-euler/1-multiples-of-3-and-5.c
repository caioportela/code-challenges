#include <stdio.h>

int main() {
    int i;
    long int T, N;
    long long int div3, div5, div15;
    long long int sum, sum3, sum5, sum15;
    
    scanf("%ld", &T);
    
    for(i = 0; i < T; i++) {
        scanf("%d", &N);
        
        div3 = (N - 1) / 3;
        div5 = (N - 1) / 5;
        div15 = (N - 1) / 15;
        
        sum3 = 3 * (div3 * (div3 + 1)) / 2;
        sum5 = 5 * (div5 * (div5 + 1)) / 2;
        sum15 = 15 * (div15 * (div15 + 1)) / 2;
        
        sum = sum3 + sum5 - sum15;
        printf("%lld\n", sum);
    }
    
    return 0;
}
