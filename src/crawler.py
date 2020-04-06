from login import Login
from bs4 import BeautifulSoup
from pathlib import Path
import os
from urllib import request
from urllib.error import URLError, HTTPError


class Crawler(object):
    def __init__(self, contest_name, base_savepath="./cases"):
        login = Login()
        login.login()
        self.base_savepath = Path(base_savepath)
        os.makedirs(self.base_savepath, exist_ok=True)
        self.session = login.session
        self.contest_name = contest_name.lower()

    def fetch_test_cases(self, url_problem):
        content = self.session.get(url_problem)
        s = BeautifulSoup(content.text, 'html5lib')
        test_cases = [tag.get_text() for tag in s.find_all("pre")]
        test_inputs = []
        test_answers = []
        for i in range(1, len(test_cases) // 2):
            if i % 2 == 0:
                test_answers.append(test_cases[i])
            else:
                test_inputs.append(test_cases[i])

        return test_inputs, test_answers

    def output_test_cases(self, url_problem, output_file_dir):
        output_path = Path(output_file_dir)
        os.makedirs(output_path, exist_ok=True)
        test_inputs, test_answers = self.fetch_test_cases(url_problem)
        assert len(test_answers) == len(test_inputs)
        for i in range(len(test_inputs)):
            test_input = test_inputs[i]
            test_answer = test_answers[i]
            test_input_file = f"test_input{i+1}.txt"
            test_answer_file = f'test_answer{i+1}.txt'
            with open(output_path.joinpath(test_input_file), mode="w") as w:
                w.write(test_input)
            with open(output_path.joinpath(test_answer_file), mode="w") as w:
                w.write(test_answer)

    def check_url_existance(self, url):
        try:
            request.urlopen(url)
            return True
        except (URLError, HTTPError):
            return False

    def run(self):
        base_url = "https://atcoder.jp/contests/"
        problem_nums = ["a", "b", "c", "d", "e", "f"]
        contest_url = f'{base_url}{self.contest_name}/tasks/'
        for n in problem_nums:
            problem_url = f"{contest_url}{self.contest_name}_{n}"
            if self.check_url_existance(problem_url):
                save_dir = f"{self.contest_name}{n}".upper()
                save_path = self.base_savepath.joinpath(save_dir)
                self.output_test_cases(problem_url, save_path)
            else:
                print(f"{problem_url} dose not exist!")
