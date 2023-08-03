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