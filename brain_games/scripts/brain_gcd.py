#!/usr/bin/env python3
from brain_games.games import gcd_game
from brain_games import engine


def main():
    engine.game_engine(gcd_game.game_logic, gcd_game.test)


if __name__ == '__main__':
    main()
