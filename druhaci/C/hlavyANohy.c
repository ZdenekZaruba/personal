#include <stdio.h>
#include <stdlib.h>
#include <math.h>

const int heads = 22;
const int legs = 72;

int main() {
    int cow, hen;

    cow = (legs - 2 * heads) / (4 - 2);
    hen = heads - cow;

    printf("Cows = %d\nHens = %d", cow, hen);
}