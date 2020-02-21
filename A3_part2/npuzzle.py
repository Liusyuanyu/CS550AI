

from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.searchrep import Problem

class NPuzzle(Problem):
    """
    NPuzzle - Problem representation for an N-tile puzzle
    Provides implementations for Problem actions specific to N tile puzzles.
    """
    def __init__(self, n, force_state=None, **kwargs):
        """"__init__(n, force_state, **kwargs)
        
        NPuzzle constructor.  Creates an initial TileBoard of size n.
        If force_state is not None, the puzzle is initialized to the
        specified state instead of being generated randomly.
        
        The parent's class constructor is then called with the TileBoard
        instance any any remaining arguments captured in **kwargs.
        """
        # Note on **kwargs:
        # **kwargs is Python construct that captures any remaining arguments 
        # into a dictionary.  The dictionary can be accessed like any other 
        # dictionary, e.g. kwargs["keyname"], or passed to another function 
        # as if each entry was a keyword argument:
        #    e.g. foobar(arg1, arg2, …, argn, **kwargs).

        # initialize parent
        # def __init__(self, initial, goals=None, 
        #          g = lambda oldnode, action, newnode : oldnode.depth+1, 
        #          h = lambda newnode : 0):
        nBoard = TileBoard(n, force_state=force_state)
        super().__init__(initial= nBoard, goals = nBoard.goals, g=kwargs['g'], h=kwargs['h'])
        # self.nBoard = TileBoard(n, force_state=force_state)
        # super().__init__(initial= self.nBoard.state_tuple(),goals = self.nBoard.goals, g=kwargs['g'], h=kwargs['h'])

        # raise NotImplemented

    def actions(self, state):
        "actions(state) - find a set of actions applicable to specified state"
        return super().actions(state)
        
        # nboard = TileBoard(self.nBoard.boardsize, force_state=state)
        # return nboard.get_actions()
        # raise NotImplemented
    
    def result(self, state, action):
        "result(state, action)- apply action to state and return new state"
        
        # [delta_r, delta_c] = action
        # pos = action.index(None)
        # rprime, cprime = pos//self.nBoard.boardsize+delta_r , pos %self.nBoard.boardsize + delta_c
        # newPos = rprime*self.nBoard.boardsize +  cprime
        # newState = list(state)
        # newState[pos], newPos[newPos] = newState[newPos], newPos[pos] 
        # return newState
        return state.move(action)

        # nboard = TileBoard(self.tileNum, force_state=state)
        # return nboard.move(action).state_tuple
        # raise NotImplemented
    
    def goal_test(self, state):
        "goal_test(state) - Is state a goal?"
        return super().goal_test(state.state_tuple())

        # raise NotImplemented

    
        



