class Logic:
    @staticmethod
    def shift_row_right(array, row_index):
        row = array[row_index]
        first_elem = row[0]
        row[0] = row[3]
        row[3] = row[2]
        row[2] = row[1]
        row[1] = first_elem

    @staticmethod
    def shift_row_left(array, row_index):
        row = array[row_index]
        first_elem = row[0]
        row[0] = row[1]
        row[1] = row[2]
        row[2] = row[3]
        row[3] = first_elem

    @staticmethod
    def shift_col_down(array, col_index):
        t = array[3][col_index]
        array[3][col_index] = array[2][col_index]
        array[2][col_index] = array[1][col_index]
        array[1][col_index] = array[0][col_index]
        array[0][col_index] = t

    @staticmethod
    def shift_col_up(array, col_index):
        t = array[0][col_index]
        array[0][col_index] = array[1][col_index]
        array[1][col_index] = array[2][col_index]
        array[2][col_index] = array[3][col_index]
        array[3][col_index] = t