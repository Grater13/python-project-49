from brain_games.games import prime
from brain_games import engine


def main():
    engine.game_engine(prime.game_logic, prime.test)


if __name__ == '__main__':
    main()
