import nox


@nox.session
def flake8(session):
    session.install("flake8")
    session.run("flake8", "bot")


@nox.session
def codespell(session):
    session.install("codespell")
    session.run("codespell", "bot")


@nox.session
def mypy(session):
    session.install("mypy")
    session.run("mypy", "bot")
