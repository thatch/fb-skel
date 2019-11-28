# Skel

Making it easier to handle python project boilerplate, and keep up-to-date with
best practices if you have a lot of repositories and want them to all look
similar.

It does this by using template contained in the `skel` checkout to generate
files in a `skel` branch in your repo.  You then merge those into whatever
branch your want, handling conflicts yourself using the normal merge tools.

While we do accept pull requests, if you have drastically different needs please
create a fork and give it a descriptive name.


# Quick Start

(in existing repo)

```
/path/to/skel/regen-git.py
# (answer questions)
# when completed, it will create a branch for you
Good luck, the first 'git merge --allow-unrelated-histories skel' is typically
full of conflicts.
```

# Updating later

```
# (go update the skel repo)
/path/to/skel/regen-git.py
# (maybe answer questions, if new things have been added)
# when completed, it will create a branch for you
Completed; use 'git merge skel' to pull in changes.
```


# License

skel is copyright [Tim Hatch](http://timhatch.com/), and licensed under
the MIT license.  I am providing code in this repository to you under an open
source license.  This is my personal repository; the license you receive to
my code is from me and not from my employer. See the `LICENSE` file for details.
