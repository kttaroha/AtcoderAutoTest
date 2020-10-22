from crawler import Crawler
from executor import Executor
import argparse


def setup(args):
    contest_name = args.contest_name
    crawler = Crawler(contest_name)
    crawler.run()


def run_test(args):
    excutor = Executor(args.contest_name)
    excutor.excute_test_cases(args.problem_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("contest_name", type=str)
    parser.add_argument("-s", "--setup", action="store_true")
    parser.add_argument("-p", "--problem_name", type=str)

    args = parser.parse_args()

    if args.setup:
        setup(args)

    if args.problem_name:
        run_test(args)
