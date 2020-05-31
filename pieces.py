class Piece:
	def __init__(self, player, square, value, name):
		self.player = player
		self.color = player.color
		self.piece_value = value
		self.name = name
		self.has_moved = False

class Pawn(Piece):
	def __init__(self, player, square):
		super().__init__(player, square, 1, "Pawn")


class King(Piece):
	def __init__(self, player, square):
		super().__init__(player, square, 15, "King")

class Queen(Piece):
	def __init__(self, player, square):
		super().__init__(player, square, 9, "Queen")

class Bishop(Piece):
	def __init__(self, player, square):
		super().__init__(player, square, 3, "Bishop")

class Knight(Piece):
	def __init__(self, player, square):
		super().__init__(player, square, 3, "Knight")

class Rook(Piece):
	def __init__(self, player, square):
		super().__init__(player, square, 5, "Rook")

