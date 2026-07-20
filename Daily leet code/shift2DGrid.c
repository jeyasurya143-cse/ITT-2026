#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** shiftGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes) {
    int row = gridSize;
    int col = *gridColSize;
    int total_elements = row * col;
    *returnSize = row;
    *returnColumnSizes = (int*)malloc(row * sizeof(int));
    int** result = (int**)malloc(row * sizeof(int*));
    for (int i = 0; i < row; i++) {
        (*returnColumnSizes)[i] = col;
        result[i] = (int*)malloc(col * sizeof(int));
    }

    k = k % total_elements;

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            int current_1D_index = i * col + j;
            int new_1D_index = (current_1D_index + k) % total_elements;
            int new_row = new_1D_index / col;
            int new_col = new_1D_index % col;
            

            result[new_row][new_col] = grid[i][j];
        }
    }

    return result;
}

