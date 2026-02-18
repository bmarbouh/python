#!/usr/bin/env python3

import sys


def analyse():
    args = sys.argv
    valid_args = list()
    if len(args) <= 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
            )
        return
    try:
        count = 1
        while count < len(args):
            valid_args.append(int(args[count]))
            count += 1
        print("=== Player Score Analytics ===")
        print(f"Scores processed: {valid_args}")
        print(f"Total players: {len(valid_args)}")
        print(f"Total score: {sum(valid_args)}")
        print(f"Average score: {sum(valid_args) / len(valid_args)}")
        print(f"High score: {max(valid_args)}")
        print(f"Low score: {min(valid_args)}")
        print(f"Score range: {max(valid_args) - min(valid_args)}")
    except ValueError:
        print("You need to entre valid numbers")


if __name__ == "__main__":
    analyse()
