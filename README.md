# nhlvisualizer
Visualize NHL Stats

## Setup Local Development Environment

Step 1: Clone the repo and navigate to repo folder.

```bash
git clone git@github.com:gkarp/nhlvisualizer.git
cd nhlvisualizer
```

Step 2: Setup dedicated python environment for the project.
Python version is specified in `setup.cfg`.
Setuptools is used to manage packaging and dependencies

Example:
```bash
conda create --name mynhl python=3.10
conda activate mynhl
pip install -r dev-requirements.txt
pip install -e .
```

pip-compile is used to update dependencies.
```bash
pip-compile setup.cfg
```
