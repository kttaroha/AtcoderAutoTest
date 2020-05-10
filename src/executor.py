from pathlib import Path
import glob
import subprocess


class Executor(object):
    def __init__(self, contest_name):
        self.contest_name = contest_name.upper()
        self.py_files = glob.glob(f"./{self.contest_name}*.py")
        self.get_test_cases()

    def get_test_cases(self):
        all_problems = glob.glob("./cases/*")
        self.problem_names = {
            p.split("/")[-1].replace(self.contest_name, ""):
            p for p in all_problems
            }

    def get_test_sets(self, problem_name):
        inp_ans_set = {}
        test_files = list(Path(self.problem_names[problem_name]).glob("*"))
        test_inputs = sorted(
            [path for path in test_files if path.match("*input*")])
        test_answers = sorted(
            [path for path in test_files if path.match("*answer*")])

        for inp, ans in zip(test_inputs, test_answers):
            inp_ans_set[inp] = ans
        return inp_ans_set

    def excute_test_cases(self, problem_name, py_file):
        test_sets = self.get_test_sets(problem_name)
        test_num = 0
        correct_num = 0
        for input_file, ans_file in test_sets.items():
            test_num += 1
            with open(input_file, encoding='utf-8') as file:
                result = subprocess.run(
                    f'python3 {py_file}', shell=True, check=True, stdin=file,
                    stdout=subprocess.PIPE, universal_newlines=True)

            with open(ans_file, encoding='utf-8') as file:
                answer = file.read()

            if result.stdout == answer:
                correct_num += 1
            else:
                print(f"Failed: {test_num+1}")

        if correct_num == test_num:
            print("Passed all test cases!")


if __name__ == "__main__":
    e = Executor("ABC160")
    e.excute_test_cases("D", "ABC160D.py")
