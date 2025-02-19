"""
importing os
"""
import os

class UtilFunctions:
    @staticmethod
    def ltrim(s):
        i = 0
        while i < len(s) and (s[i] == ' ' or s[i] == '\t'):
            i += 1
        return s[i:]

    @staticmethod
    def rtrim(s):
        i = 1
        while i <= len(s) and (s[-i] == ' ' or s[-i] == '\n' or s[-i] == '\t'):
            i += 1
        return s[:len(s) + 1 - i]

    @staticmethod
    def trim(s):
        return UtilFunctions.rtrim(UtilFunctions.ltrim(s))

    @staticmethod
    def custom_append(lst, item):
        lst.append(item)
        return lst

    @staticmethod
    def str_to_int(s):
        output = 0
        is_negative = False
        i = 0
        
        s = s.strip()
        
        if s[0] == '-':
            is_negative = True
            i += 1
        elif s[0] == '+':
            i += 1

        for i in range(i, len(s)):
            char = s[i]

            if '0' <= char <= '9':
                output = output * 10 + (ord(char) - ord('0'))
            else:
                raise ValueError("Input file has wrong format")

        if is_negative:
            output = -output
        return output

    @staticmethod
    def merge(array, left, mid, right):
        sub_array_one = mid - left + 1
        sub_array_two = right - mid

        left_array = [0] * sub_array_one
        right_array = [0] * sub_array_two

        for i in range(sub_array_one):
            left_array[i] = array[left + i]
        for j in range(sub_array_two):
            right_array[j] = array[mid + 1 + j]

        index_of_sub_array_one = 0
        index_of_sub_array_two = 0
        index_of_merged_array = left

        while index_of_sub_array_one < sub_array_one and index_of_sub_array_two < sub_array_two:
            if left_array[index_of_sub_array_one] <= right_array[index_of_sub_array_two]:
                array[index_of_merged_array] = left_array[index_of_sub_array_one]
                index_of_sub_array_one += 1
            else:
                array[index_of_merged_array] = right_array[index_of_sub_array_two]
                index_of_sub_array_two += 1
            index_of_merged_array += 1

        while index_of_sub_array_one < sub_array_one:
            array[index_of_merged_array] = left_array[index_of_sub_array_one]
            index_of_sub_array_one += 1
            index_of_merged_array += 1

        while index_of_sub_array_two < sub_array_two:
            array[index_of_merged_array] = right_array[index_of_sub_array_two]
            index_of_sub_array_two += 1
            index_of_merged_array += 1

    @staticmethod
    def merge_sort(array, begin, end):
        if begin >= end:
            return
        mid = begin + (end - begin) // 2
        UtilFunctions.merge_sort(array, begin, mid)
        UtilFunctions.merge_sort(array, mid + 1, end)
        UtilFunctions.merge(array, begin, mid, end)

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

    def insert(self, r, c, val):
        if r >= self.rows or c >= self.cols:
            raise ValueError("Invalid matrix position")
        if val != 0:
            UtilFunctions.custom_append(self.data, [r, c, val])

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices dimensions do not match")

        result = SparseMatrix(self.rows, self.cols)
        UtilFunctions.merge_sort(self.data, 0, len(self.data) - 1)
        UtilFunctions.merge_sort(other.data, 0, len(other.data) - 1)
        
        apos = 0
        bpos = 0
        while apos < len(self.data) and bpos < len(other.data):
            a_row, a_col, a_val = self.data[apos]
            b_row, b_col, b_val = other.data[bpos]

            if a_row < b_row or (a_row == b_row and a_col < b_col):
                UtilFunctions.custom_append(result.data, [a_row, a_col, a_val])
                apos += 1
            elif b_row < a_row or (b_row == a_row and b_col < a_col):
                UtilFunctions.custom_append(result.data, [b_row, b_col, b_val])
                bpos += 1
            else:
                if a_val + b_val != 0:
                    UtilFunctions.custom_append(result.data, [a_row, a_col, a_val + b_val])
                apos += 1
                bpos += 1

        while apos < len(self.data):
            UtilFunctions.custom_append(result.data, self.data[apos])
            apos += 1

        while bpos < len(other.data):
            UtilFunctions.custom_append(result.data, other.data[bpos])
            bpos += 1
OB
OB        return result

    def subtract(self, other):
OB        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices dimensions do not match")
OBOBOBOBOB
OB        result = SparseMatrix(self.rows, self.cols)
OB        UtilFunctions.merge_sort(self.data, 0, len(self.data) - 1)
OBOB        UtilFunctions.merge_sort(other.data, 0, len(other.data) - 1)

OB        apos = 0
        bpos = 0
        while apos < len(self.data) and bpos < len(other.data):
            a_row, a_col, a_val = self.data[apos]
OBOBOBOBOBOBOBOB            b_row, b_col, b_val = other.data[bpos]
OB
            if a_row < b_row or (a_row == b_row and a_col < b_col):
OB                UtilFunctions.custom_append(result.data, [a_row, a_col, a_val])
                apos += 1
OB            elif b_row < a_row or (b_row == a_row and b_col < a_col):
                UtilFunctions.custom_append(result.data, [b_row, b_col, -b_val])
OB                bpos += 1
            else:
OB                if a_val - b_val != 0:
OBOB                    UtilFunctions.custom_append(result.data, [a_row, a_col, a_val - b_val])
                apos += 1
OBOB                bpos += 1
OB
        while apos < len(self.data):
            UtilFunctions.custom_append(result.data, self.data[apos])
OB            apos += 1

OB        while bpos < len(other.data):
            UtilFunctions.custom_append(result.data, [other.data[bpos][0], other.data[bpos][1], -other.data[bpos][2]])
            bpos += 1

        return result

    def transpose(self):
        result = SparseMatrix(self.cols, self.rows)
        for r, c, val in self.data:
            result.insert(c, r, val)
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Invalid matrix dimensions for multiplication")

        result = SparseMatrix(self.rows, other.cols)
        other_t = other.transpose()

        non_zero = {}
        for r, c, val in self.data:
            for r_t, c_t, val_t in other.data:
                if c == r_t:
                    key = f"{r},{c_t}"
                    if key not in non_zero:
                        non_zero[key] = 0
                    non_zero[key] += val * val_t
OBOBOBOBOBOB
OBOBOB        for key, value in non_zero.items():
OBOB            r, c = map(int, key.split(','))
OBOB            if value != 0:
OBOBOB                result.insert(r, c, value)

OBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOB        return result
OA
    def print_matrix(self):
OBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOB        print(f"Dimension: {self.rows} x {self.cols}")
        print("Sparse Matrix: Row Column Value")
        for r, c, val in sorted(self.data):
OBOBOBOBOBOBOBOBOBOBOBOBOB            print(f"{r} {c} {val}")

OBOBOBOBOBOBOBOBOBOBdef get_parts(string):
    output = []
OBOBOBOBOBOBOBOBOBOBOB    if string[0] == '(':
        part = ''
OBOBOBOBOBOBOBOB        for s in string[1:]:
            if s not in [' ', ',', ')']:
OB                part += s
            elif s == ',' or s == ')':
                UtilFunctions.custom_append(output, part)
                part = ''
    return output
OBOBOBOBOB
def custom_split(string, split_char):
    output = []
    part = ''
OBOBOB    for s in string:
OB        if s != split_char:
            part += s
        else:
            UtilFunctions.custom_append(output, part)
            part = ''
    UtilFunctions.custom_append(output, part)
OBOBOBOBOB    return output
OBOB
def process_input(input_path):
OBOBOBOBOBOBOBOBOBOBOB    dimensions = {}
OBOBOB    with open(input_path, 'r') as f:
OBOB        data = f.read().splitlines()
OBOBOB
    split_line = custom_split(data[0], '=')
OBOB    dimensions[split_line[0]] = split_line[1]
OBOBOBOBOBOBOBOBOBOBOB    split_line = custom_split(data[1], '=')
    dimensions[split_line[0]] = split_line[1]
    
OBOB    rows = UtilFunctions.str_to_int(dimensions['rows'].strip())
    cols = UtilFunctions.str_to_int(dimensions['cols'].strip())
    matrix = SparseMatrix(rows, cols)
    for line in data[2:]:
        try:
            line = line.strip()
            if not line:
OBOBOBOBOBOBOBOBOBOBOBOBOBOB                continue
            row_num, col_num, value = map(int, get_parts(line))
OBOB            matrix.insert(row_num, col_num, value)
        except Exception as e:
OBOBOB            print(f"Error processing line {line}: {e}")
            continue
OBOBOBOBOBOBOB    return matrix

def output_results(output_path, results, r, c):
OBOB    with open(output_path, 'w') as f:
        f.write(f"rows={r}\n")
        f.write(f"cols={c}\n")
        for result in results:
            f.write(f"({result[0]}, {result[1]}, {result[2]})\n")

OBOBOBOBOBOBdef main():
    input_file = input("Enter the path of the first matrix file: ")
OBOB    print('-' * 20, "Processing file", '-' * 20)
    matrix1 = process_input(input_file)
OB    print('-' * 20, "Completed", '-' * 20, '\n')
OBOBOB
    second_file = input("Enter the path of the second matrix file: ")
    matrix2 = matrix1 if input_file == second_file else process_input(second_file)
OB    print('-' * 20, "Completed", '-' * 20)

    output_file = input("Enter the path for the output file: ")
    operation_choice = input("Which operation would you like to do:\n1. Add\n2. Subtract\n3. Multiply\nEnter your choice: ")

OB    print('-' * 20, "Performing operation", '-' * 20)

    if operation_choice == '1':
        result = matrix1.add(matrix2)
    elif operation_choice == '2':
        result = matrix1.subtract(matrix2)
    elif operation_choice == '3':
        result = matrix1.multiply(matrix2)

    output_results(output_file, result.data, result.rows, result.cols)
    print("Done! Results written to", output_file)
