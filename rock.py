#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ["rock", "paper", "scissors"]

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def __init__(self):
        self.score = 0
        self.my_move = random.choice(moves)
        self.their_move = "paper"


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            answer = input("choose your move\n")
            if answer in moves:
                return answer
            else:
                print("i do not understand.")


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        self.my_move
        return cycle(self.my_move)


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


def cycle(self):

    if self == "scissors":
        return "paper"
    elif self == "paper":
        return "rock"
    elif self == "rock":
        return "scissors"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1.score += 1
            print("Player 1 wins!")
            print(f"Player 1:{self.p1.score}, Player 2 :{self.p2.score}")
        elif beats(move2, move1):
            self.p2.score += 1
            print("Player 2 wins!")
            print(f"Player 1:{self.p1.score}, Player 2 :{self.p2.score}")
        else:
            move1 == move1
            print("its a tie!")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def result(self):
        if self.p1.score > self.p2.score:
            print("Player 1 wins !\n")
        else:
            print("Player 2 wins !\n")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        self.result()
        print(f"Final score: Player 1:{self.p1.score}, Player 2 :{self.p2.score}")
        if self.p1.score > self.p2.score:
            print("Player 1 wins !\n")
        else:
            print("Player 2 wins !\n")
        replay = input("do you want to play again?\n")
        if replay == "yes":
            return self.play_game()
        else:
            print("Game over!")


if __name__ == "__main__":
    game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()
