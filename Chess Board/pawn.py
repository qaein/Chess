from piece import piece

class pawn(piece):
    def _reset_piece(self, board):
        board.demote(self.loc)
        super(pawn,self)._reset_piece(board)
    
    def _adjacent_columns(self, loc1, loc2):
        adj_sets = [("A","B"),("B","A"),("B","C"),("C","B"),
                    ("C","D"),("D","C"),("D","E"),("E","D"),
                    ("E","F"),("F","E"),("F","G"),("G","F"),
                    ("G","H"),("H","G")]
        this_set = (loc1[0], loc2[0])
        return this_set in adj_sets
    
    def move(self, newLoc, board):
        loc = self.loc
        newLoc = newLoc.upper()
        legal = False
        if ((self.color == self.TOP_COLOR) and (loc[1] == '2')): #top of board moving down, starting location
            if (newLoc[0] == loc[0]): #same column - just need to check if it's 1 or 2 below
                if ((newLoc[1] == '3') or (newLoc[1] == '4')): 
                    # probable legal move verified - need to check if anything is in our way
                    if (board.get_cell(loc[0] + '3') == ""): # cell 3 is clear
                        if (newLoc[1] == '3'): 
                            legal = True # move ok if moving to cell 3
                        elif (board.get_cell(loc[0] + '4') == ""): # cell 4 is clear
                            legal = True # move ok if moving to cell 4
                #else illegal - don't need to explicitly add that case here
            elif (self._adjacent_columns(loc,newLoc)): # attacking from start location
                target_piece = board.get_cell(newLoc)
                if ( not (target_piece[0] == self.color) and not (target_piece == "")):
                    # piece exists in cell, cell is adjacent, need to verify new cell is 
                    # in ++ cell if Top Color or -- cell if bottom color
                    if (newLoc[1] == '3'):
                        legal = True
        elif ((self.color == self.BOTTOM_COLOR) and (loc[1] == '7')): #bottom of board moving up, starting location
            if ((newLoc[1] == '6') or (newLoc[1] == '5')): 
                # probable legal move verified - need to check if anything is in our way
                if (board.get_cell(loc[0] + '6') == ""): # cell 6 is clear
                    if (newLoc[1] == '6'): 
                        legal = True # move ok if moving to cell 6
                    elif (board.get_cell(loc[0] + '5') == ""): # cell 5 is clear
                        legal = True # move ok if moving to cell 5
            #else illegal - don't need to explicitly add that case here
            elif (self._adjacent_columns(loc,newLoc)): # attacking from start location
                target_piece = board.get_cell(newLoc)
                if ( not (target_piece[0] == self.color) and not (target_piece == "")):
                    # piece exists in cell, cell is adjacent, need to verify new cell is 
                    # in ++ cell if Top Color or -- cell if bottom color
                    if (newLoc[1] == '6'):
                        legal = True
        else: #all non-starting positions
            if (newLoc[0] == loc[0]):
                # moving forward
                if (board.get_cell(newLoc) == ""):
                    # can only move forward if space is empty
                    locCol = int(loc[1])
                    newLocCol = int(newLoc[1])
                    if ((self.color == self.BOTTOM_COLOR) and (newLocCol = locCol - 1)):
                        legal = True
                    elif ((self.color == self.TOP_COLOR) and (newLocCol = locCol + 1)):
                        legal = True
            elif (self._adjacent_columns(loc, newLoc)):
                target_piece = board.get_cell(newLoc)
                if ( not (target_piece == "") and not (target_piece[0] == self.color)):
                    locCol = int(loc[1])
                    newLocCol = int(newLoc[1])
                    if ((self.color == self.BOTTOM_COLOR) and (newLocCol = locCol - 1)):
                        legal = True
                        board.capture(newLoc)
                    elif ((self.color == self.TOP_COLOR) and (newLocCol = locCol + 1)):
                        legal = True
                        board.capture(newLoc)
                elif (target_piece == ""):
                    #might be en passant
                    pass #implement en passant check
        if legal:
            loc = newLoc
        if ((loc[1] == "1") or (loc[1] == "8")):
            board.promote(loc)
        return legal