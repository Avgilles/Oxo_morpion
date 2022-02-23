#!/usr/bin/env python
# coding: utf-8

import random

class Board:
    def __init__(self, height:int, width:int):
        self.__board = [[None for w in range(width)] for h in range(height)]

    def __str__(self):
        res = ""
        for indexi, line in enumerate(self.__board):
            res += "---------------\n"
            for indexj, column in enumerate(line):
                if indexj == 0:
                    res += f"{indexi }"
                res += f"| {column} |" if column is not None else "|   |"
            res += '\n'
        res += "---------------\n"
        return res
    
    def add(self, pos:tuple, number):
        self.__board[pos[0]][pos[1]] = number
    
    def winned(self):
        return False

class Player:
    def __init__(self, nickname, token):
        self.nickname = nickname
        self.token = token

    def play(self):
        print(f"Player {self.nickname}")
        line = input("Please select line: ")
        column = input("Please select column: ")
        return (int(line), int(column)), self.token

class Game:
    def __init__(self, player1, player2):
        self.p1 = Player(player1, 'x')
        self.p2 = Player(player2, 'o')
        self.board = Board(3,3)
        self.currentPlayer = 0
        self.finished = False

    def __str__(self):
        return self.board.__str__()
    
    def play(self, values):
        self.board.add(*values)
        if self.board.winned():
            self.finished = True
            return self.board.winned()
        self.currentPlayer = (self.currentPlayer + 1) % 2
        # self.currentPlayer = 1 if self.currentPlayer == 2 else 1


# PLAYER_TURN = {
#     "1": game.p1.play,
#     "2": game.p2.play
# }



if __name__ == "__main__":
    game = Game("Hector", "Gilles")

    PLAYER_TURN = [game.p1.play, game.p2.play]

    game.currentPlayer = random.choice([0,1])

    while not game.finished:
        print(game)
        # game.play(PLAYER_TURN[str(game.currentPlayer)]())
        print(f"game.currentPlayer = {game.currentPlayer}")
        game.play(PLAYER_TURN[game.currentPlayer]())


