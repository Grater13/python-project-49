#!/usr/bin/env python3
from brain_games.games import even
from brain_games import engine


def main():
    engine.game_start(even)


if __name__ == '__main__':
    main()
