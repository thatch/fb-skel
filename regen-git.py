#!/usr/bin/env python

import datetime
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional

import regen  # should live alongside this script

sys.path.insert(0, os.path.dirname(__file__))

SKEL_BRANCH = "skel"


def find_git_dir(path: Optional[Path] = None) -> Path:
    if path is None:
        path = Path(".").absolute()

    dev = path.stat().st_dev
    while path != Path("/"):
        trial = path / ".git"
        if trial.exists():
            return trial
        path = path.parent
        if path.stat().st_dev != dev:
            raise Exception("No git dir found on same device")

    raise Exception("No git dir found before root")


def main():
    git_branches = subprocess.check_output(
        ["git", "branch", "-a"], encoding="utf-8"
    ).splitlines(False)
    print("Branches", git_branches)

    if f"* {SKEL_BRANCH}" in git_branches:
        raise Exception(f"Branch {SKEL_BRANCH!r} appears to be checked out")

    existing_branch = f"  {SKEL_BRANCH}" in git_branches
    try:
        git_user = subprocess.check_output(
            ["git", "config", "--get", "--local", "user.name"]
        ).strip()
    except subprocess.CalledProcessError:
        git_user = None
    try:
        git_email = subprocess.check_output(
            ["git", "config", "--get", "--local", "user.email"]
        ).strip()
    except subprocess.CalledProcessError:
        git_email = None

    git_dir = find_git_dir()

    print(f"Using git_dir {git_dir!r}")
    with tempfile.TemporaryDirectory() as d:
        os.chdir(d)

        if not existing_branch:
            subprocess.check_call(["git", "init"])
            if git_user:
                subprocess.check_call(["git", "config", "user.name", git_user])
            if git_email:
                subprocess.check_call(["git", "config", "user.email", git_email])

            subprocess.check_call(["git", "remote", "add", "origin", git_dir])
            subprocess.check_call(["git", "checkout", "--orphan", SKEL_BRANCH])
            regen.main()
            subprocess.check_call(["git", "add", "-A"])
            try:
                subprocess.check_call(["git", "commit", "-m", "Initialize skel"])
            except subprocess.CalledProcessError as e:
                print("\x1b[33mNo changes?\x1b[0m")
                raise
            subprocess.check_call(["git", "push", "origin", SKEL_BRANCH])
            print(
                "Good luck, the first "
                f"'\x1b[32mgit merge --allow-unrelated-histories {SKEL_BRANCH}\x1b[0m' "
                "is typically full of conflicts."
            )
        else:
            subprocess.check_call(["git", "clone", "-b", SKEL_BRANCH, git_dir, "t"])
            os.chdir("t")
            if git_user:
                subprocess.check_call(["git", "config", "user.name", git_user])
            if git_email:
                subprocess.check_call(["git", "config", "user.email", git_email])

            regen.main()
            subprocess.check_call(["git", "add", "-A"])

            date = datetime.datetime.now().strftime("%Y-%m-%d")
            try:
                subprocess.check_call(["git", "commit", "-m", f"Update skel {date}"])
            except subprocess.CalledProcessError as e:
                print("\x1b[33mNo changes?\x1b[0m")
                return

            subprocess.check_call(["git", "push", "origin", SKEL_BRANCH])
            print(
                f"Completed; use '\x1b[32mgit merge {SKEL_BRANCH}\x1b[0m' to pull in changes."
            )


if __name__ == "__main__":
    main()
