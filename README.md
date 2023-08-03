# Multistage Bug Fixer: Automatic Bug Fixing via Deliberate Problem Solving with Large Language Models

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
This repository contains the implementation and evaluation of an approach 
for automatic bug fixing by enhancing large language models (here ChatGPT 4.0) with
a multistage interactive process inspired by the 
[Tree-of-Thoughts (ToT)](https://arxiv.org/abs/2305.10601)
approach by S. Yao et al., 2023.

## Prerequisites
- SAP AI Core as a Proxy for Azure OpenAI Services. Access it [here](https://github.com/SAP-samples/azure-openai-aicore-cap-api).
- Official Repo of Tree of Thoughts (ToT). Access it [here](https://github.com/princeton-nlp/tree-of-thought-llm).

## Installation
1. Set up your BTP Azure OpenAI API key and store it in the environment variable `AZURE_OPENAI_API_KEY`.

## Getting Started
The following minimal script will attempt to fix a bug. Please note that the process might be slow as it utilizes GPT-4:

```python
import argparse
from mbf.methods.bfs import solve
from mbf.tasks.codefixer import CodeFixerTask

args = argparse.Namespace(backend='gpt-4', temperature=0.7, task='codefixer', naive_run=False, prompt_sample='cot',
                          method_generate='sample', method_evaluate='vote', method_select='greedy', n_generate_sample=5,
                          n_evaluate_sample=5, n_select_sample=1)

task = CodeFixerTask()
ys, infos = solve(args, task, 1)
print(ys[0])
```

## Reproduceing Paper Experiments
You can reproduce the experiments from our paper by running `py scripts/codefixer/bfs.py` which calls `run.py` file. 

## Citation & Contact
If you find the Code Fixer Task of Tree of Thoughts useful or interesting, please consider citing our paper and starring this repository. Your support is greatly appreciated!

For any queries or issues, feel free to contact guoyang.weng@gmail.com or open an issue on this repository.

```bibtex
@misc{weng2023fixer,
      title={Automatic Bug Fixing via Deliberate Problem Solving with Large Language Models}, 
      author={Guoyang Weng and Artur Andrzejak},
      year={2023},
      note={submitted to ISSRE 2023, Fast Abstracts Track}
}
```
