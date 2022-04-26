from invoke import task

SRC_DIR = "auto_hedge"
@task
def mypy(c):
    c.run(f"mypy {SRC_DIR}")

@task
def test(c):
    c.run(f"pytest --typeguard-packages={SRC_DIR} {SRC_DIR}")

@task
def docs_build(c):
    c.run(f"sphinx-build docs docs/_build")

