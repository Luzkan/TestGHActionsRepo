from git.repo import Repo
from rich import print

__version__ = "0.8.2-alpha.1+build.1"


def do_versioning(branch_name: str):
    repo = Repo('.')
    branch = repo.create_head(branch_name)
    branch.checkout()
    repo.git.commit("--allow-empty", "-m", f'A: Feature1 ({branch_name})')
    repo.git.commit("--allow-empty", "-m", f'A: Feature2 ({branch_name})')
    repo.git.commit("--allow-empty", "-m", f'A: Feature3 ({branch_name})\nF: Fixed something too! #patch')
    repo.git.commit("--allow-empty", "-m", f'A: Feature4 ({branch_name})\nC: Logger width\nR: Trash Code')
    repo.git.commit("--allow-empty", "-m", f'A: Feature5 ({branch_name})\nElaboration about random stuff\nJIRA/Trello or whatever ID: 4')
    repo.git.commit("--allow-empty", "-m", f'R: Something4 ({branch_name})')
    repo.git.commit("--allow-empty", "-m", f'R: Something5 ({branch_name}) #minor')
    repo.remote("origin").push()


def main():
    print(f"Hello from the Test Environment. Version: {__version__}")


if __name__ == "__main__":
    do_versioning('testing/random1')
