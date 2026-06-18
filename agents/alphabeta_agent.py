class AlphaBetaAgent:

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
    def alphabeta(self, game, depth, alpha, beta, maximizing, root_player):
      
        current_player = root_player if maximizing else -root_player

        if depth == 0 or game.game_over():
            return self.evaluate(game, root_player), None

        moves = game.get_valid_moves(current_player)

        if not moves:
            value,mo = self.alphabeta(game,depth-1,alpha,beta,not maximizing,root_player)
            return value, None

        best_move = moves[0]
        if maximizing:
            best_score = float('-inf')
            for move in moves:
                next_game = game.copy()
                next_game.make_move(current_player, move[0], move[1])
                score,m = self.alphabeta(next_game,depth - 1,alpha,beta,False,root_player)
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
            return best_score, best_move

        else:
            best_score = float('inf')
            for move in moves:
                next_game = game.copy()
                next_game.make_move(current_player, move[0], move[1])
                score, m = self.alphabeta(next_game,depth - 1, alpha, beta,True,root_player)
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta,score)
                if beta <= alpha:
                    break
            return best_score, best_move

    def choose_move(self, game, player):
        value, move = self.alphabeta(
            game, self.depth, float('-inf'), float('inf'), True, player)
        return move
