#!/usr/bin/env python3
from brain_games.games import progression
from brain_games import engine


def main():
    engine.game_engine(progression.game_logic, progression.test)


if __name__ == '__main__':
    main()
