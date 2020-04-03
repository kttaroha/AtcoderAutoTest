from login import Login
from bs4 import BeautifulSoup
from pathlib import Path
import os
from urllib import request
from urllib.error import URLError, HTTPError


class Crawler(object):
    def __init__(self):
        login = Login()
        login.login()
        self.session = login.session

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





if __name__ == "__main__":
    c = Crawler()
    c.output_test_cases("https://atcoder.jp/contests/abc160/tasks/abc160_b", "../ABC160_B")
    print(c.check_url_existance("https://atcoder.jp/contests/abc160/tasks/abc160_g"))