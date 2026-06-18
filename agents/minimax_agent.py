# TODO: STUDENT IMPLEMENTATION
import math

class MinimaxAgent:
    def __init__(self, depth=4):
        self.depth = depth

    def evaluate(self, game, player):
        opponent = -player
        
        if game.game_over():
            black_score, white_score = game.score()
            return (black_score - white_score) if player == 1 else (white_score - black_score)

        w1 = 1.0
        w2 = 0.6
        w3 = 2

        black_score, white_score = game.score()
        if player == 1:
            agent_score = black_score
            opponent_score = white_score
        else:
            agent_score = white_score
            opponent_score = black_score
        
        score_diff = agent_score - opponent_score


        agent_moves = len(game.get_valid_moves(player))
        opponent_moves = len(game.get_valid_moves(opponent))
        moves_diff = agent_moves - opponent_moves

        corners = [(0, 0), (0, game.size - 1), (game.size - 1, 0), (game.size - 1, game.size - 1)]
        corner_score = 0
        for row, col in corners:
            if game.board[row][col] == player:
                corner_score += 1
            elif game.board[row][col] == opponent:
                corner_score -= 1


        return (w1 * score_diff + w2 * moves_diff + w3 * corner_score)

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
