#include <limits.h>
#include <stdlib.h>

int compareDescending(const void *a, const void *b) {
    int valA = *(const int*)a;
    int valB = *(const int*)b;
    if (valA > valB) return -1;
    if (valA < valB) return 1;
    return 0;
}


void cycleSortDescending(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), compareDescending);
}

int maximumGap(int* nums, int numsSize) {
    if (numsSize < 2) {
        return 0;
    }

    cycleSortDescending(nums, numsSize);

    int maxGap = 0;
    for (int i = 0; i < numsSize - 1; i++) {
        int sub = nums[i] - nums[i + 1];
        if (sub > maxGap) {
            maxGap = sub;
        }
    }

    return maxGap;
}
