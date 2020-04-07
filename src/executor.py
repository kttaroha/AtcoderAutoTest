import subprocess
import glob 


class Executor(object):
    def __init__(self, contest_name):
        self.contest_name = contest_name.upper
        self.py_files = glob.glob(f"./{self.contest_name}*.py")
    
    def get_test_cases(self):
        all_problems = glob.glob("./cases/*")
        self.problem_names = {
            p.split("/")[-1].replace(self.contest_name, ""):
            p for p in all_problems
            }   
   
      
if __name__ == "__main__":
    e = Executor("ABC160")
    e.read_test_cases()
