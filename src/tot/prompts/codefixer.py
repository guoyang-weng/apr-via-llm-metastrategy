standard_prompt = '''
#####You will be provided with a piece of Python code, and your task is to find and fix bugs in it.
###Buggy Python
{input}
###Fixed Python
'''

cot_prompt = '''
###You will be provided with a piece of Python code with a bug on a single line, and your task is to find and fix the bug in it. 
###Buggy Python
{input}
###Analyze root cause and localize the faulty line by understanding the difference between actual output and expected output, then fix program. Your output should be of the following format:

###Only root cause analysis and a faulty line localization, no fixed code:###
Your root cause analysis here.

###Fixed code:###
Your fixed Python code here.
'''

vote_prompt = '''Given an instruction and several choices, decide which choice is most promising. Analyze each choice in detail, then conclude in the last line "The best choice is {s}", where s the integer id of the choice.
'''

compare_prompt = '''Briefly analyze the effectiveness of the following two code repairs. Conclude in the last line "The more effective repair is 1", "The more effective repair is 2", or "Both repairs are similarly effective".
'''

score_prompt = '''Analyze the following fixed code, then at the last line conclude "Thus the fixed code quality score is {s}", where s is an integer from 1 to 10.
'''