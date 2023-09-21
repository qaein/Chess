from piece import piece

class rook(piece):
    def _same_row(self, loc, newLoc):
        return (loc[0] == newLoc[0])
    
    def _same_col(self, loc, newLoc):
        return (loc[1] == newLoc[1])

    def move(self, newLoc, board):
        legal = False
        sameRow = self._same_row(self.loc,newLoc)
        sameCol = self._same_col(self.loc,newLoc)
        myRow = int(self.loc[1])
        myCol = self.loc[0]
        newRow = int(newLoc[1])
        newCol = newLoc[0]
        if (sameRow):
            # walk along row and make sure nothing except last location has a piece in it
            # if newLoc has a piece in it, make sure it's the opposing color
            # castling will occur here
            canMove = True
            for c in range(myCol,newCol):
                square = board.get_cell[c+str(myRow)]
                if not (square == ""):
                    canMove = False
                elif ((r == newRow) and not (square[0] == self.color)): # taking piece?
                    canMove = True
                    board.capture(newLoc)
            if canMove:
                legal = True
                loc = newLoc
            else:
                #need to check if castling, then determine if castling is legal if so
                pass
        elif (sameCol): 
            canMove = True
            for r in range(myRow,newRow):
                square = board.get_cell[myCol + str(r)]
                if not (square == ""):
                    canMove = False
                elif ((r == newRow) and not (square[0] == self.color)): # taking piece?
                    canMove = True
                    board.capture(newLoc)
            if canMove:
                legal = True
                loc = newLoc
            # no castling equivalant
        return legal