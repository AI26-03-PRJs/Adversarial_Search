class AlphaBetaAgent:
    """Simple Alpha-Beta agent for Othello / Reversi."""

    def __init__(self, depth=4):
        self.depth = depth

    def evaluate(self, game, player):
        """Return a simple score for the board from the player's point of view."""
        black_score, white_score = game.score()

        if player == 1:
            my_score = black_score
            opp_score = white_score
            
        else:
            my_score = white_score
            opp_score = black_score

        score = my_score - opp_score

        # Corners are very important in Othello.
        corners = [
            (0, 0),
            (0, game.size - 1),
            (game.size - 1, 0),
            (game.size - 1, game.size - 1),
        ]

        for row, col in corners:
            if game.board[row][col] == player:
                score += 30
            elif game.board[row][col] == -player:
                score -= 30

        # Mobility: more valid moves is usually better.
        my_moves = len(game.get_valid_moves(player))
        opp_moves = len(game.get_valid_moves(-player))
        score += my_moves - opp_moves

        return score

    def alphabeta(self, game, depth, alpha, beta, maximizing, root_player):
      
        current_player = root_player if maximizing else -root_player

        if depth == 0 or game.game_over():
            return self.evaluate(game, root_player), None

        moves = game.get_valid_moves(current_player)

        if not moves:
            # If the current player has no moves, pass to the opponent.
            value, _ = self.alphabeta(
                game,
                depth - 1,
                alpha,
                beta,
                not maximizing,
                root_player,
            )
            return value, None

        best_move = None

        if maximizing:
            best_score = float('-inf')
            for move in moves:
                next_game = game.copy()
                next_game.make_move(current_player, move[0], move[1])
                score, _ = self.alphabeta(
                    next_game,
                    depth - 1,
                    alpha,
                    beta,
                    False,
                    root_player,
                )
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
                score, _ = self.alphabeta(
                    next_game,
                    depth - 1,
                    alpha,
                    beta,
                    True,
                    root_player,
                )
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return best_score, best_move

    def choose_move(self, game, player):
        """Return the best move for the player."""
        moves = game.get_valid_moves(player)
        if not moves:
            return None

        _, move = self.alphabeta(
            game,
            self.depth,
            float('-inf'),
            float('inf'),
            True,
            player,
        )
        return move