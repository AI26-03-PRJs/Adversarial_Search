"""
University: University of Isfahan
Faculty: Mathematics and Statistics
Department: Computer Science
Course: Artificial Intelligence
Professor: Dr. Faria Nasiri Mofakham
TAs: MehrAzin Marzough, Mohammad Karimi, Anahita Honarmandian
Project: Adversarial Search in Othello (Minimax and Alpha-Beta Pruning)
"""

from agents.random_agent import RandomAgent
from agents.greedy_agent import GreedyAgent
from agents.minimax_agent import MinimaxAgent
from agents.alphabeta_agent import AlphaBetaAgent
from tournament import play_game
from datetime import datetime


for agent1 in [MinimaxAgent, AlphaBetaAgent]:
    for depth in [2, 3, 4]:
        print('='*120)
        print(f'{agent1.__name__} for depth {depth}')
        print('=' * 120)
        print('         agent         |    number of games     |     number of wins    |     win rate      |        run time     ')
        for agent2 in [GreedyAgent, RandomAgent]:
            win = 0
            run_time = 0
            for i in range(20):
                t1 = datetime.now()
                result = play_game(agent1(), agent2())
                print(result)
                t2=datetime.now()
                run_time += (t2-t1).total_seconds()
                if result[0]> result[1]:
                    win +=1
            print('*'*100)
            av_time = run_time/20
            print(f'    {agent2.__name__}        |          20            |          {win}           |          {(win/20)*100}%    |           {av_time}')

            print("_"*120)
# print(play_game(GreedyAgent(), MinimaxAgent()))
# print(play_game(GreedyAgent(), MinimaxAgent()))
# print(play_game(MinimaxAgent() ,GreedyAgent()))
# print(play_game(MinimaxAgent() ,GreedyAgent()))