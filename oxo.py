import numpy as np


class Board:
    def __init__(self, size_array=9):
        self.sizeArray = size_array

    def __str__(self):
        res = ""
        line_board = np.array_split(self.createdBoard(), 3)
        for line in line_board:
            res += f"\n -------------  \n"
            for column in line:
                res += f" | {column}" if column == 0 else str(column.value) + "|"

        return res

    def createdBoard(self):
        board = []
        diagonal_list = [[], []]
        # print(int(self.sizeArray/3))
        for i in range(0, int(self.sizeArray)):
            '''
            if(i%4 == 0):
                a = i + 2
                diagonal_list[0].append(0)
                diagonal_list[1].append(a)
            print(f"diagonal :{diagonal_list}")

            '''
            board.append(0)
        '''
        line_board = np.array_split(board, 3)
        data = {"line_board": line_board, "board": board }
        '''
        return board


def check_inputs(this_input, array=[]):
    array.append(this_input)
    correct = True
    if this_input > 9:
        correct = False
    else:
        for i in array:
            print(i)
    print(array)
    return correct


def addPoint(board, num, player):
    board[num] = player

    return board


'''
FUNC_DICT = {
    "check_inputs":check_inputs()
}
'''


class Oxo:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2

    def __str__(self):
        return f"{self.player1} vs {self.player2} \n {self.board}"

    def role(self):
        print("chose your case")
        all_input_move = []
        win = False
        i = 0
        white_board = self.board.createdBoard()
        print(f"whiteboard : {white_board}")
        while i < 9 or win:
            try:
                input_move = int(input())
                if check_inputs(input_move, all_input_move):

                    if i % 2:
                        print(f'{self.player2} a joué a la case {input_move}')
                        self.board = addPoint(white_board, input_move, 1)
                    else:
                        print(f'{self.player1} a joué a la case {input_move}')
                        self.board = addPoint(white_board, input_move, 2)

                    i = i + 1
                    # print(input_move)
                    # print(f"whiteboard : {white_board}")
                    print(self.__str__())
                else:
                    print("Please use a number between 0-9")

            except ValueError:
                print("Please only input digits")


if __name__ == "__main__":
    exe = Oxo("gilles", "susu")
    print(exe)
    exe.role()
