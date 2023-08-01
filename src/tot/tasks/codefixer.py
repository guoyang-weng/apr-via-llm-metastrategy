import os
import re
from tot.tasks.base import Task, DATA_PATH
from tot.prompts.codefixer import *
from tot.models import gpt


class CodeFixerTask(Task):
    """
    Input (x)   : a piece of buggy Python code
    Output (y)  : a repaired Python code
    Reward (r)  : # TODO
    Input Example: 
    Output Example: 
    """
    def __init__(self, file='data_3_buggy_code_filenames.txt'):
        """
        file: a text file, each line is some Python code
        """
        super().__init__()
        path = os.path.join(DATA_PATH, 'buggy_code', file)
        with open(path) as file:
            self.data = [line.strip() for line in file]       
        self.steps = 2
        self.stops = ['\n###Fixed code:###\n', None]

    def __len__(self) -> int:
        return len(self.data)
    
    def get_input(self, idx: int) -> str:
        path = os.path.join(DATA_PATH, 'buggy_code', self.data[idx])
        # Read the buggy code from the file
        with open(path, 'r') as file:
            data = file.read()
        return data
    
    def test_output(self, idx: int, output: str):
        output = output.split('\n###Fixed code:###\n')[-1]
        prompt = score_prompt + output
        score_outputs = gpt(prompt, n=5, model='gpt-4')
        scores = []
        for score_output in score_outputs:
            pattern = r".*fixed code quality score is (\d+).*"
            match = re.match(pattern, score_output, re.DOTALL)
            if match:
                score = int(match.groups()[0])
                scores.append(score)
            else:
                print(f'------------------score no match: {[score_output]}')
        print(scores)
        info = {'rs': scores, 'r': sum(scores) / len(scores) if scores else 0}
        return info
    
    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        return standard_prompt.format(input=x) + y

    @staticmethod
    def cot_prompt_wrap(x: str, y:str='') -> str:
        return cot_prompt.format(input=x) + y

    @staticmethod
    def vote_prompt_wrap(x: str, ys: list) -> str:
        prompt = vote_prompt
        for i, y in enumerate(ys, 1):
            prompt += f'Choice {i}:\n{y}\n'
        return prompt
    
    @staticmethod
    def vote_outputs_unwrap(vote_outputs: list, n_candidates: int) -> list:
        vote_results = [0] * n_candidates
        for vote_output in vote_outputs:
            pattern = r".*best choice is .*(\d+).*"
            match = re.match(pattern, vote_output, re.DOTALL)
            if match:
                vote = int(match.groups()[0]) - 1
                if vote in range(n_candidates):
                    vote_results[vote] += 1
            else:
                print(f'vote no match: {[vote_output]}')
        return vote_results

    @staticmethod
    def compare_prompt_wrap(x: str, ys: list) -> str:
        assert len(ys) == 2, 'compare prompt only supports 2 candidates'
        ys = [y.split('Fixed Python\n')[-1] for y in ys]
        prompt = compare_prompt + f'Repair 1:\n{ys[0]}\n\nRepair 2:\n{ys[1]}\n'
        return prompt
    
    @staticmethod
    def compare_output_unwrap(compare_output: str):
        if 'more effective repair is 1' in compare_output:
            return 0
        elif 'more effective repair is 2' in compare_output:
            return 1
        elif 'both repairs are similarly effective' in compare_output:
            return 0.5
        else:
            print(f'-----------------compare no match: {[compare_output]}')
            return -1