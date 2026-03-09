import random
import math
import connect383


BOT_NAME =  'CANCER_BOT'


class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""
  
    rseed = None  # change this to a value if you want consistent random choices

    def __init__(self):
        if self.rseed is None:
            self.rstate = None
        else:
            random.seed(self.rseed)
            self.rstate = random.getstate()

    def get_move(self, state):
        if self.rstate is not None:
            random.setstate(self.rstate)
        return random.choice(state.successors())


class HumanAgent:
    """Prompts user to supply a valid move.  Very slow and not always smart!"""

    def get_move(self, state, depth=None):
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = None
        while move not in move__state:
            try:
                move = int(input(prompt))
            except ValueError:
                continue
        return move, move__state[move]


class MinimaxAgent:
    """Artificially intelligent agent that uses minimax to optimally select the best move."""

    def get_move(self, state):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, next_state in state.successors():
            util = self.minimax(next_state)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, next_state
        return best_move, best_state

    def minimax(self, state):
        #base case
        if state.is_full():
            return state.utility()
        
        #recursive case if the player is the maximizer
        if state.next_player() == 1:
            #lower bound set to negative infinity
            best_util = -math.inf
            #checked each of the possible states (no need for move)
            for move, next_state in state.successors():
                #recursive call to minimax for each of the possible states
                util = self.minimax(next_state)
                best_util = max(best_util, util)
            return best_util
        
        #recursive case if the player is the minimizer
        if state.next_player() == -1:
            best_util = math.inf
            for move, next_state in state.successors():
                util = self.minimax(next_state)
                #looks for the lowest value across all states insetad of max
                best_util = min(best_util, util)
            return best_util
    
        
        
        
        """Determine the minimax utility value of the given state.

        Gets called by get_move() to determine the value of each successor state.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the exact minimax utility value of the state
        """


class MinimaxLookaheadAgent(MinimaxAgent):
    """Artificially intelligent agent that uses depth-limited minimax to select the best move.
 
    Hint: Consider what you did for MinimaxAgent. What do you need to change to get what you want? 
    """

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state.

        Gets called by get_move() to determine the value of successor states.

        The depth data member (set in the constructor) determines the maximum depth of the game 
        tree that gets explored before estimating the state utilities using the evaluation() 
        function.  If depth is 0, no traversal is performed, and minimax returns the results of 
        a call to evaluation(). 

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the (possibly estimated) minimax utility value of the state
        """
        #
        # Fill this in!
        #
        return 9  # Change this line!

    def minimax_depth(self, state, depth):
        """This is just a helper method for minimax(). Feel free to use it or not. """
        pass

    def evaluation(self, state):
        
        #feature 1 = calculating the points present on the board
        score = state.utility()
        
        
        #feature 2 = 2/3 in a row
        #using the helper functions, we convert hte 2D board into a 1D list
        all_lines = state.get_rows() + state.get_cols() + state.get_diags()
        #parsing through all the lines
        for line in all_lines:
            #create a window that looks at 4 pieces
            for i in range(len(line)-3):
                window4 = line[i:i+4]
                #if there are 1 pieces and 1 empty spaces, adds a larger weight to the score
                if window4.count(1) == 3 and window4.count(0) == 1:
                    score += 5
                elif window4.count(-1) == 3 and window4.count(0) == 1:
                    score -= 5
                #if there are 3 pieces and 1 empty space, adds a larger weight to the score
                elif window4.count(1) == 2 and window4.count(0) == 2:
                    score += 2
                elif window4.count(-1) == 2 and window4.count(0) == 2:
                    score -= 2
            for i in range(len(line) - 2):
                window3 = line[i:i+3]
                if window3.count(1) == 2 and window3.count(0) == 1:
                    score += 3
                elif window3.count(-1) == 2 and window3.count(0) == 1:
                    score -= 3
                    
        #feature 3 = starting in the middle columns
        #step 1, find the middle columns
        center = state.num_cols // 2
        
        #step 2, store the list of the middle column pieces in middle_column
        columns = state.get_cols()
        col_weights = {0:0.15, 1:0.05, -1:0.05}
        for offset, weight in col_weights.items():
            col_index = center + offset
            if 0 <= col_index < state.num_cols:
                col = columns[col_index]
                score += col.count(1) * weight
                score -= col.count(-1) * weight
        
        return score
    
        
            
        
        

        """Estimate the utility value of the game state based on features.

        Gets called by minimax() once the depth limit has been reached.  
        N.B.: This method must run in "constant" time for all states!

        Args:
            state: a connect383.GameState object representing the current board

        Returns: a heuristic estimate of the utility value of the state
        """



class AltMinimaxLookaheadAgent(MinimaxAgent):
    """Alternative heursitic agent used for testing"""

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state."""
        #
        # Fill this in, if it pleases you.
        #
        return 19  # Change this line, unless you have something better to do.


class MinimaxPruneAgent(MinimaxAgent):
    def minimax(self, state):
        #we run the agent through the helper function which was the alphabeta function
        return self.alphabeta(state, -math.inf, math.inf)
        

    def alphabeta(self, state,alpha, beta):
        #same as before
        if state.is_full():
            return state.utility()
    
        if state.next_player() == 1:
            best_util = -math.inf
            for move, next_state in state.successors():
                #recursive call to alphabeta 
                util = self.alphabeta(next_state, alpha, beta)
                best_util = max(best_util, util)
                alpha = max(alpha, best_util)
                if beta <= alpha:
                    break
            return best_util
        
        if state.next_player() == -1:
            best_util = math.inf
            for move, next_state in state.successors():
                util = self.alphabeta(next_state, alpha, beta)
                best_util = min(best_util, util)
                beta = min(beta, best_util)
                if beta <= alpha:
                    break
            return best_util


def get_agent(tag):
    if tag == 'random':
        return RandomAgent()
    elif tag == 'human':
        return HumanAgent()
    elif tag == 'mini':
        return MinimaxAgent()
    elif tag == 'prune':
        return MinimaxPruneAgent()
    elif tag.startswith('look'):
        depth = int(tag[4:])
        return MinimaxLookaheadAgent(depth)
    elif tag.startswith('alt'):
        depth = int(tag[3:])
        return AltMinimaxLookaheadAgent(depth)
    else:
        raise ValueError("bad agent tag: '{}'".format(tag))       
