import os

os.chdir(f"..{os.sep}Chess Board")

from chess import board

def move_test():
    b = board()
    init_state = b.get_state()
    
    #start by moving pawns -- top goes first
    assert (b.move("b2","c2"))
    move1_state = b.get_state()
    assert (move1_state[8] == "") # after moving, this cell should be empty
    assert (move1_state[16] == init_state[8]) # we moved the piece from cell 8 to cell 16
    
    
    assert(b.move("g5","e5"))  # now it's bottom's turn
    # start cell: 8*6 gets g1, + 4 = g5 -- g5 is 52
    # end cell: 8*4 gets e1, + 4 = e5 -- e5 is 36
    move2_state = b.get_state()
    assert (move2_state[52] == "") # after moving, this cell should be empty
    assert (move2_state[36] == move1_state[52])
    
    #try moving a pawn incorrectly in a few ways
    #first move forward 2 after having moved forward 1
    assert not (b.move("c2","e2"))
    
    #it's still top's turn, try moving a non-moved pawn forward 3
    assert not (b.move("b1","e1"))
    
    #still top's turn, try moving a pawn backwards
    assert not (b.move("c2","b2"))
    
    #ok, move a pawn horizontally
    assert not (b.move("c2","c3")
    
    #and now diagonally forward without attacking
    assert not (b.move("c2","d3")
    
    #ok, pawn movement is correct (as far as we can test for now) - let's move to knights
    assert (b.move("a2","c3")
    move3_state = b.get_state()
    assert (move3_state[1] == "")
    assert (move3_state[18] == move2_state[1])
    
    #finally back to bottom's move
    assert (b.move("h7","f6")
    move4_state = b.get_state
    assert (move4_state[62] == "")
    assert (move4_state[45] == move3_state[62])
    
    #knight moves seem ok generally - now to edge test
    #move the knight forward 1 and sideways 1
    assert not (b.move("c3","d3")
    assert not (b.move("c3","c4")
    
    #move knight onto another same color piece
    assert not (b.move("c3","b5"))
    