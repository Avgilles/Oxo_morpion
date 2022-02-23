import numpy as np


class Board:
    def __init__(self, size_array=9):
        self.sizeArray = size_array
        self.boardArray = self.createdBoard()

    def __str__(self):
        self.check_win()

        res = ""
        line_board = np.array_split(self.boardArray, 3)
        for line in line_board:
            res += f"\n -------------  \n"
            col = 0
            for column in line:
                res += f" | {column} |" if col == 0 else f" {column} |"
                col = col + 1

        return res

    def createdBoard(self):
        board = []
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
        self.boardArray = board
        return self.boardArray

    def check_win(self):
        line_board = np.array_split(self.boardArray, 3)
        print(f"{line_board}")

        """ horizontal """
        horizontal_board = []
        diagonal_list = [[], []]

        for i in range(0, len(self.boardArray)):

            if i % 2 == 0:
                a = i + 2
                diagonal_list[0].append(i)
                diagonal_list[1].append(a)
            print(f"diagonal :{diagonal_list}")

            """
            h_b = []
            if i % 3 == 0:
                print(i)
                h_b[0].append()
            """


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
        # self.length_board = Board().__init__()
        self.player1 = player1
        self.player2 = player2

    def __str__(self):
        return f"{self.player1} vs {self.player2} \n {self.board} \n"

    def check_inputs(self, this_input, array=[]):
        correct = True
        if this_input > 8:
            correct = False
        else:
            if this_input not in array:
                array.append(this_input)
            else:
                correct = False

        print(array)
        return correct

    def role(self):
        print("chose your case")
        all_input_move = []
        win = False
        i = 0
        white_board = self.board.createdBoard()
        print_the_board = self.board
        # print(f"whiteboard : {white_board}")
        while i < 8 or win:
            try:
                input_move = int(input())
                if self.check_inputs(input_move, all_input_move):

                    if i % 2:
                        print(f'{self.player2} a joué a la case {input_move}')
                        addPoint(white_board, input_move, 1)
                        print(print_the_board)
                    else:
                        print(f'{self.player1} a joué a la case {input_move}')
                        addPoint(white_board, input_move, 2)
                        print(print_the_board)

                    i = i + 1
                    # print(input_move)
                    # print(f"whiteboard : {white_board}")

                    print(self.__str__())
                else:
                    print("Please choose a number between 0-9 and a case not used")

            except ValueError:
                print("Please only input digits")

        print(self.__str__())


if __name__ == "__main__":
    exe = Oxo("gilles", "susu")
    # help(exe)
    # print(dir(exe))
    # print(Oxo.__dict__)
    print(exe)
    exe.role()
