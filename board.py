from pieces import *

class Board:
	def __init__(self, player1, player2):
		self.white = player1
		self.black = player2
		self.set_up_board()

	def set_up_board(self):
		self.board = [[Square(x,y) for x in range(8)] for y in range(8)]

		# Pawns
		for x in range(8): 
			self.board[1][x].piece = Pawn(self.black, self.board[1][x])
			self.board[6][x].piece = Pawn(self.white, self.board[6][x])

		# Black back row
		self.board[0][0].piece = Rook(self.black, self.board[0][0])
		self.board[0][7].piece = Rook(self.black, self.board[0][7])
		self.board[0][1].piece = Knight(self.black, self.board[0][1])
		self.board[0][6].piece = Knight(self.black, self.board[0][6])
		self.board[0][2].piece = Bishop(self.black, self.board[0][2])
		self.board[0][5].piece = Bishop(self.black, self.board[0][5])
		self.board[0][3].piece = Queen(self.black, self.board[0][3])
		self.board[0][4].piece = King(self.black, self.board[0][6])

		# White back row
		self.board[7][0].piece = Rook(self.white, self.board[7][0])
		self.board[7][7].piece = Rook(self.white, self.board[7][7])
		self.board[7][1].piece = Knight(self.white, self.board[7][1])
		self.board[7][6].piece = Knight(self.white, self.board[7][6])
		self.board[7][2].piece = Bishop(self.white, self.board[7][2])
		self.board[7][5].piece = Bishop(self.white, self.board[7][5])
		self.board[7][3].piece = Queen(self.white, self.board[7][3])
		self.board[7][4].piece = King(self.white, self.board[7][6])

	def print_board(self):
		piece_letter = {"King": "K", "Queen": "Q", "Bishop": "B", "Knight": "N", "Rook": "R", "Pawn": "P"}
		for row in self.board:
			for square in row:
				try:
					print(piece_letter[square.piece.name], end = "  ")
				except:
					print(" ", end = "  ")
			print()



class Square:
	def __init__(self, x, y, piece = None):
		self.piece = piece
		self.x = x
		self.y = y