# What is trading-helper?

I have an interest in financial markets and stock trading. A while ago I've decided to apply my knowledge in software engineering and interest in finance to algorithmic trading. And to develop some algorithms in the process.

And [Python](https://www.python.org/) is a go-to language of choice for algorithmic trading. However, I need some functions/code which I repeat over and over again in multiple projects. So, why not to make a library out of it?

This project is a collection of functions/code I use in my multiple projects to simplify my coding. Feel free to use them!

Also, it's a great way for me to learn Python for real-life scenarios.

# Local development

To run the project locally, please use Python 3.12+.

Then create a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

To install dependencies, execute:

```
pip install -e .
```

Make sure you use Python from `.venv` folder with its dependencies.

# Running tests

To run tests, execute:

```
pytest
```

# Installing library

To install library into your project, execute:

```
pip install git+https://github.com/ernestaskardzys/trading-helper.git
```

If you want, you can save all dependencies with:

```
pip freeze >> requirements.txt
```