cot_prompt_step2a = '''
You will be given two parts of the input. The first part, after the line "Buggy code:", contains a snippet of buggy Python code with a bug on a single line, and maybe unit test information. The second part, after the line "Fault hypothesis:", contains a hypothesis about the fault's location and reason. Given these inputs, output the fixed code after the line "Fixed code:".

Buggy code:
    {buggy_code}

Fault hypothesis:
    {rc_examplation}
    
Fixed code:
'''