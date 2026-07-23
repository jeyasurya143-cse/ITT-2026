void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sortColors(int* nums, int numsSize) {
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] > nums[j]) {
                swap(&nums[i], &nums[j]);
            }
        }
    }
}
