void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    int rows = matrixSize;
    int cols = *matrixColSize;
    int zero_rows[rows];
    int zero_cols[cols];
    for(int i = 0; i < rows; i++) zero_rows[i] = 0;
    for(int j = 0; j < cols; j++) zero_cols[j] = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (matrix[i][j] == 0) {
                zero_rows[i] = 1;
                zero_cols[j] = 1;
            }
        }
    }
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (zero_rows[i] == 1 || zero_cols[j] == 1) {
                matrix[i][j] = 0; 
            }
        }
    }
}
