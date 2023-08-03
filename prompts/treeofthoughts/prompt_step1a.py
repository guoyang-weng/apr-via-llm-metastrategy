cot_prompt_step1a = '''
You will be given an input. The input, after the line "Buggy code:", contains a snippet of buggy Python code with a bug on a single line, and maybe unit test information. Given the input, analyze root cause and localize the faulty line by understanding the difference between actual output and expected output, finally output the a hypothesis about the fault's location and reason after the line "Fault hypothesis:".

Buggy code:
    {buggy_code}

Fault hypothesis:
'''