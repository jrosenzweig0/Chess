from board import *

class Chess:
	def __init__(self, player1, player2):
		self.white = player1
		self.black = player2
		self.board = Board(player1, player2)

class Player:
	def __init__(self, color):
		self.color = color


if __name__ == "__main__":
	white = Player("white")
	black = Player("black")
	game = Chess(white, black)
	game.board.print_board()