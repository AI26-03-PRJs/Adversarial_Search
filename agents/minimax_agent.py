# TODO: STUDENT IMPLEMENTATION
import math

class MinimaxAgent:
    def __init__(self, depth=4):
        self.depth = depth

    def evaluate(self, game, player):
        opponent = -player
        black_score, white_score = game.score()
        
        if player == 1: 
            agent_score = black_score
            opponent_score = white_score
        else: 
            agent_score = white_score
            opponent_score = black_score
        
        agent_moves = len(game.get_valid_moves(player))
        opponent_moves = len(game.get_valid_moves(opponent))
        
        score_diff = agent_score - opponent_score
        moves_diff = agent_moves - opponent_moves
        
        return score_diff + 2 * moves_diff

    def minimax(self, game, depth, maximizing, root_player):
        if game.game_over() or depth == 0:
            return self.evaluate(game, root_player), None

        opponent = -root_player
        if maximizing:
            current_player= root_player
        else:
            current_player=opponent

        moves = game.get_valid_moves(current_player)

        if not moves:
            value, _ = self.minimax(game, depth - 1, not maximizing, root_player)
            return value, None

        best_move = None

        if maximizing:
            best_value = -math.inf
            for move in moves:
                g = game.copy()
                g.make_move(current_player, *move)
                value, _ = self.minimax(g, depth - 1, False, root_player)
                if value > best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move

        else:
            best_value = math.inf
            for move in moves:
                g = game.copy()
                g.make_move(current_player, *move)
                value, _ = self.minimax(g, depth - 1, True, root_player)
                if value < best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move


    def choose_move(self, game, player):
        value, move = self.minimax(game, self.depth, True, player)
        return move
