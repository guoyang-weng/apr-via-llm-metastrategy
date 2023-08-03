standard_prompt = '''
#####You will be provided with a piece of Python code, and your task is to find and fix bugs in it.
###Buggy Python
{input}
###Fixed Python
'''

cot_prompt_step1a = '''
You will be given an input. The input, after the line "Buggy code:", contains a snippet of buggy Python code with a bug on a single line, and maybe unit test information. Given the input, analyze root cause and localize the faulty line by understanding the difference between actual output and expected output, finally output the a hypothesis about the fault's location and reason after the line "Fault hypothesis:".

Buggy code:
    {input}

Fault hypothesis:
'''

cot_prompt_step2a = '''
You will be given two parts of the input. The first part, after the line "Buggy code:", contains a snippet of buggy Python code with a bug on a single line, and maybe unit test information. The second part, after the line "Fault hypothesis:", contains a hypothesis about the fault's location and reason. Given these inputs, output the fixed code after the line "Fixed code:".

Buggy code:
    {input1}

Fault hypothesis:
    {input2}
    
Fixed code:
'''

vote_prompt = '''Given an instruction and several choices, decide which choice is most promising. Analyze each choice in detail, then conclude in the last line "The best choice is {s}", where s the integer id of the choice.

Instruction: You will be provided with a piece of Python code, and your task is to find and fix bugs in it.

Buggy code:
'''

score_prompt = '''Analyze the following fixed code, then at the last line conclude "Thus the fixed code quality score is {s}", where s is an integer from 1 to 10.
'''