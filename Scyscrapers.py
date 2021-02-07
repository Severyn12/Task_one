'''
In this module was implemented game, named
Scyscrapers.
'''

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    Also returns False if argument is not a string.
    >>> read_input(["check.txt"])
    False
    """
    if not isinstance(path,str):
        return False
    result = []
    with open(path,'r',encoding='UTF-8') as data:
        for line in data:
            result.append(line.strip())

    return result


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible
    looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    count = 1
    line = [i for i in input_line[1:len(input_line)-1] if  i.isdigit() ]
    comp = line[0]
    for i,char in enumerate(line):
        if char>comp:
            comp = char
            count +=1
    if count >= pivot:
        return True
    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game
    board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5',\
    '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in board:
        for ele in i:
            if ele == '?':
                return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
    '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    check = []
    for i in board[1:len(board)-1]:
        for ele in i[1:len(i)-1]:
            if (ele != '*') and (ele in check):
                return False
            check.append(ele)
        check.clear()
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    value,value2 = True,True
    for i in board[1:len(board)-1]:
        if i[0] != '*':
            value = left_to_right_check(i,int(i[0]))
        if i[len(i)-1] != '*':
            num = int(i[len(i)-1])
            row = i[::-1]
            value2 = left_to_right_check(row,num)
        if not (value and value2):
            return False
    return True


def unique_columns(board:list)->bool:
    '''
    Checks if all numbers in columns are unique.
    >>> unique_columns(['**21*', '4124*', '4235*',\
    '*5432', '*2*1*'])
    True
    >>> unique_columns([ '**4','1**','**1'])
    True
    '''
    for num in range(len(board[0])-2):
        check = list()
        for row in board[1:len(board)-1]:
            ele = row[num+1]
            if (ele in check) and (ele != '*'):
                return False
            check.append(row[num+1])
    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of
    unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical
    case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
    '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
    '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*',\
    '*41532*', '*2*1***'])
    False
    """
    if not unique_columns(board):
        return False
    count = 0
    value = True
    for i in board[::len(board)-1]:
        for num,ele in enumerate(i[1:len(i)-1]):
            if ele.isdigit():
                row = [i[num+1] for i in board]
                if count == 1:
                    row = row[::-1]
                value = left_to_right_check(''.join(row),int(ele))
            if not value:
                return False
        count += 1
    return True


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    Also returns False if argument is not a string.
    >>> check_skyscrapers(123)
    False
    """
    if not isinstance(input_path,str):
        return False
    board =  read_input(input_path)
    flag = check_not_finished_board(board)
    flag2 = check_uniqueness_in_rows(board)
    flag3 = check_columns(board)
    flag4 = check_horizontal_visibility(board)
    if flag and flag2 and flag3 and flag4:
        return True
    return False
