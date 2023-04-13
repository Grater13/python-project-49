from brain_games.games import calc
from brain_games import engine


def main():
    engine.game_engine(calc.game_logic, calc.test)

if __name__ == '__main__':
    main()
