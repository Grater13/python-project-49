#!/usr/bin/env python3
from brain_games.games import even
from brain_games import engine


def main():
    engine.game_engine(even.game_logic, even.test)


if __name__ == '__main__':
    main()
