class piece:
    
    self.TOP_COLOR = "w"
    self.BOTTOM_COLOR = "b"
    
    def __init(self, loc, color):
        self.startLoc = loc.upper()
        if color in [self.TOP_COLOR,self.BOTTOM_COLOR]:
            self.startColor = color.lower()
        else:
            raise IOError(f"Color must be either {self.TOP_COLOR} or {self.BOTTOM_COLOR}. Use 'piece.TOP_COLOR' or 'piece.BOTTOM_COLOR' only.")
        self._reset_piece
    
    def _reset_piece(self, board):
        self.location = self.startLoc
        self.on_board = True
        self.color = self.startColor
    
    def move(self, newLoc, board):
        return False # must override
        # Return value is whether the piece believes it can move to the provided location
    
    def captured():
        self.on_board = False
    
    def get_captured():
        return not self.on_board
        
    def get_pos():
        if self.on_board:
            return self.location
        return ""