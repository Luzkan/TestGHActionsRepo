from rich import print
from git.repo import Repo

__version__ = "0.5.0"


def do_versioning(branch_name: str):
    repo = Repo('.')
    branch = repo.create_head(branch_name)
    branch.checkout()
    repo.git.commit("--allow-empty", "-m", f'A: Feature1 ({branch_name})')
    repo.git.commit("--allow-empty", "-m", f'A: Feature2 ({branch_name})')
    repo.git.commit("--allow-empty", "-m", f'A: Feature3 ({branch_name})')
    repo.git.commit("--allow-empty", "-m", f'R: Something4 ({branch_name})')
    repo.git.commit("--allow-empty", "-m", f'R: Something5 ({branch_name})')
    repo.remote("origin").push()


def main():
    print(f"Hello from the Test Environment. Version: {__version__}")


if __name__ == "__main__":
    do_versioning('TBA')
