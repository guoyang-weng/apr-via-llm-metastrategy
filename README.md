# Code Fixer Task of Tree of Thoughts (ToT)
Automatic Bug Fixing via Deliberate Problem Solving with Large Language Models

## Requirement
SAP AI Core as Proxy for Azure OpenAI Services
https://github.com/SAP-samples/azure-openai-aicore-cap-api

Official Repo of Tree of Thoughts (ToT)
https://github.com/princeton-nlp/tree-of-thought-llm

## Setup
1. Set up BTP Azure OpenAI API key and store in environment variable ``AZURE_OPENAI_API_KEY``. 

## Quick Start
The following minimal script will attempt to fix a bug (might be a bit slow as it's using GPT-4):
```python
import argparse
from tot.methods.bfs import solve
from tot.tasks.codefixer import CodeFixerTask

args = argparse.Namespace(backend='gpt-4', temperature=0.7, task='codefixer', naive_run=False, prompt_sample='cot', method_generate='sample', method_evaluate='vote', method_select='greedy', n_generate_sample=5, n_evaluate_sample=5, n_select_sample=1)

task = CodeFixerTask()
ys, infos = solve(args, task, 1)
print(ys[0])
```

## Paper Experiments

Run experiments via ``py scripts/codefixer/bfs.py``.





## Citations
Please cite the paper and star this repo if you use codefixer task of ToT and find it interesting/useful, thanks! Feel free to contact guoyang.weng@gmail.com or open an issue if you have any questions.

```bibtex
@misc{weng2023fixer,
      title={Automatic Bug Fixing via Deliberate Problem Solving with Large Language Models}, 
      author={Guoyang Weng and Artur Andrzejak},
      year={2023}
}
```
