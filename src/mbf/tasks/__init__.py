# This file is a modified version of the file /src/tot/tasks/__init__.py from the repository https://github.com/princeton-nlp/tree-of-thought-llm.
# The original file was created by the authors of the paper "Tree of Thoughts: Deliberate Problem Solving with Large Language Models", arxiv.org/abs/2305.10601

def get_task(name):
    if name == 'game24':
        from mbf.tasks.game24 import Game24Task
        return Game24Task()
    elif name == 'text':
        from mbf.tasks.text import TextTask
        return TextTask()
    elif name == 'crosswords':
        from mbf.tasks.crosswords import MiniCrosswordsTask
        return MiniCrosswordsTask()
    elif name == 'codefixer':
        from mbf.tasks.codefixer import CodeFixerTask
        return CodeFixerTask()
    else:
        raise NotImplementedError
