from piece import piece
from pawn import pawn
from rook import rook
from knight import knight
from bishop import bishop
from queen import queen
from king import king


class board:
    def __init__():
        self.board = {
                        "A1": rook("A1",piece.TOP_COLOR),
                        "A2": knight("A2",piece.TOP_COLOR),
                        "A3": bishop("A3",piece.TOP_COLOR),
                        "A4": queen("A4",piece.TOP_COLOR),
                        "A5": king("A5",piece.TOP_COLOR),
                        "A6": bishop("A6",piece.TOP_COLOR),
                        "A7": knight("A7",piece.TOP_COLOR),
                        "A8": rook("A8",piece.TOP_COLOR),
                        "B1": pawn("B1",piece.TOP_COLOR),
                        "B2": pawn("B2",piece.TOP_COLOR),
                        "B3": pawn("B3",piece.TOP_COLOR),
                        "B4": pawn("B4",piece.TOP_COLOR),
                        "B5": pawn("B5",piece.TOP_COLOR),
                        "B6": pawn("B6",piece.TOP_COLOR),
                        "B7": pawn("B7",piece.TOP_COLOR),
                        "B8": pawn("B8",piece.TOP_COLOR),
                        "C1": "",
                        "C2": "",
                        "C3": "",
                        "C4": "",
                        "C5": "",
                        "C6": "",
                        "C7": "",
                        "C8": "",
                        "D1": "",
                        "D2": "",
                        "D3": "",
                        "D4": "",
                        "D5": "",
                        "D6": "",
                        "D7": "",
                        "D8": "",
                        "E1": "",
                        "E2": "",
                        "E3": "",
                        "E4": "",
                        "E5": "",
                        "E6": "",
                        "E7": "",
                        "E8": "",
                        "F1": "",
                        "F2": "",
                        "F3": "",
                        "F4": "",
                        "F5": "",
                        "F6": "",
                        "F7": "",
                        "F8": "",
                        "G1": pawn("G1",piece.BOTTOM_COLOR),
                        "G2": pawn("G2",piece.BOTTOM_COLOR),
                        "G3": pawn("G3",piece.BOTTOM_COLOR),
                        "G4": pawn("G4",piece.BOTTOM_COLOR),
                        "G5": pawn("G5",piece.BOTTOM_COLOR),
                        "G6": pawn("G6",piece.BOTTOM_COLOR),
                        "G7": pawn("G7",piece.BOTTOM_COLOR),
                        "G8": pawn("G8",piece.BOTTOM_COLOR),
                        "H1": rook("H1",piece.BOTTOM_COLOR),
                        "H2": knight("H2",piece.BOTTOM_COLOR),
                        "H3": bishop("H3",piece.BOTTOM_COLOR),
                        "H4": king("H4",piece.BOTTOM_COLOR),
                        "H5": queen("H5",piece.BOTTOM_COLOR),
                        "H6": bishop("H6",piece.BOTTOM_COLOR),
                        "H7": knight("H7",piece.BOTTOM_COLOR),
                        "H8": rook("H8",piece.BOTTOM_COLOR)
                    }
    
    def move(loc1,loc2):
        # Piece.move(newLoc,board) requires self be passed for the second argument
        # Piece collision will take place in the Piece's move function
        pass
    
    def get_cell(loc):
        index = self.loc2index(loc)
        retVal = ""
        if not (self.state[index] == "")
        return retVal
    
    def loc2index(loc):
        colHead = ["A","B","C","D","E","F","G","H"]
        colNum = colHead.index(loc[0])
        rowNum = int(loc[1])
        return (colNum * 8) + rowNum
        
    def capture(loc):
        
        
    def promote(loc):
        # only works on pawns, only pawns will call
        pass
    
    def demote(loc):
        # only works on pawns, only pawns will call

