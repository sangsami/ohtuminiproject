from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def win_start(ctx):
    ctx.run("py src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def pylint(ctx):
    ctx.run("pylint src")

@task
def robot(ctx):
    ctx.run("echo 'If this doesn't work - make sure to start the application in a different cli, and try again.'")
    ctx.run("robot src/tests")