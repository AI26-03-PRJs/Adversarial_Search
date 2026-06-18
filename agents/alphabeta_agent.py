class AlphaBetaAgent:

    def __init__(self, depth=4):
        self.depth = depth

    def evaluate(self, game, player):
        b, w = game.score()
        if player == 1:
            my_score = b
            opp_score = w
        else:
            my_score = w
            opp_score = b
        score = 0.9*(my_score - opp_score)
        corners = [(0, 0),(0, game.size - 1),(game.size - 1, 0),(game.size - 1, game.size - 1)]
        for row, col in corners:
            if game.board[row][col] == player:
                score += 2
            elif game.board[row][col] == -player:
                score -= 2

        my_moves = len(game.get_valid_moves(player))
        opp_moves = len(game.get_valid_moves(-player))
        score += 0.5*(my_moves - opp_moves)

        return score

    def alphabeta(self, game, depth, alpha, beta, maximizing, root_player):
      
        current_player = root_player if maximizing else -root_player

        if depth == 0 or game.game_over():
            return self.evaluate(game, root_player), None

        moves = game.get_valid_moves(current_player)

        if not moves:
            value,mo = self.alphabeta(game,depth - 1,alpha,beta,not maximizing,root_player)
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
        moves = game.get_valid_moves(player)
        if not moves:
            return None

        s, move = self.alphabeta(game, self.depth,float('-inf'),float('inf'),True,player)
        return move