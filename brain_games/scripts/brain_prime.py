#!/usr/bin/env python3
from brain_games.games import prime
from brain_games import engine


def main():
    engine.game_engine(prime.game_logic, prime.TEST)


if __name__ == '__main__':
    main()
