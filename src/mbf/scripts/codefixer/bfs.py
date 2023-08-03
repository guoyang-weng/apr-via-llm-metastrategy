import subprocess

command = [
    "py",
    "run.py",
    "--task",
    "codefixer",
    "--task_start_index",
    "0",
    "--task_end_index",
    "3",
    "--prompt_sample",
    "cot",
    "--method_generate",
    "sample",
    "--method_evaluate",
    "vote",
    "--method_select",
    "greedy",
    "--n_generate_sample",
    "2",
    "--n_evaluate_sample",
    "2",
    "--n_select_sample",
    "1"
]

subprocess.run(command)