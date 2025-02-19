import os

class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        if matrixFilePath:
            self.read_from_file(matrixFilePath)
        elif numRows is not None and numCols is not None:
            self.numRows = numRows
            self.numCols = numCols
            self.data = {}

    def read_from_file(self, filePath):
        """ Read the sparse matrix from a given file """
        with open(filePath, 'r') as f:
            # Read the number of rows and columns
            first_line = f.readline().strip()
            second_line = f.readline().strip()

            self.numRows = int(first_line.split('=')[1])
            self.numCols = int(second_line.split('=')[1])

            self.data = {}

            # Read the sparse matrix entries
            for line in f:
                row, col, value = map(int, line.strip()[1:-1].split(','))
                if value != 0:  # Only store non-zero values
                    self.data[(row, col)] = value

    def getElement(self, currRow, currCol):
        """ Get the element at the given row and column """
        return self.data.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        """ Set the element at the given row and column """
        if value == 0:
            if (currRow, currCol) in self.data:
                del self.data[(currRow, currCol)]  # Remove if setting value to zero
        else:
            self.data[(currRow, currCol)] = value

    def __str__(self):
        """ Return a string representation of the sparse matrix """
        return f"SparseMatrix({self.numRows}x{self.numCols}, non-zero elements: {len(self.data)})"

# Test the SparseMatrix class
if __name__ == "__main__":
    # File path for the input sample matrix file
    sample_input_file = 'dsa/sparse_matrix/sample_inputs/sparse_matrix.txt'

    # Create a SparseMatrix instance by reading from the file
    matrix = SparseMatrix(matrixFilePath=sample_input_file)

    # Test getting an element from the sparse matrix
    print(f"Element at (0, 381): {matrix.getElement(0, 381)}")  # Should print -694
    print(f"Element at (0, 128): {matrix.getElement(0, 128)}")  # Should print -838

    # Test setting an element in the sparse matrix
    matrix.setElement(0, 100, 500)
    print(f"New element at (0, 100): {matrix.getElement(0, 100)}")  # Should print 500

    # Print matrix details
    print(matrix)
