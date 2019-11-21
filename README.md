# Skel

Making it easier to handle python project boilerplate, and keep up-to-date with
best practices if you have a lot of repositories and want them to all look
similar.

If you make edits after merging (for example adding a new makefile target),
those will either be kept or shown as a conflict by git.


# Quick Start

```
(in existing repo)
git checkout --orphan -b skel
git reset --hard
/path/to/skel/regen.py
(answer questions)
git commit -m "Create skel $(date +%Y%m%d)"

git checkout master
git merge --allow-unrelated-histories skel
(handle conflicts)
```

# Updating later

```
git checkout skel
/path/to/skel/regen.py
git commit -m "Update skel $(date +%Y%m%d)"

git checkout master
git merge skel
(handle any conflicts)
```

# License

skel is copyright [Tim Hatch](http://timhatch.com/), and licensed under
the MIT license.  I am providing code in this repository to you under an open
source license.  This is my personal repository; the license you receive to
my code is from me and not from my employer. See the `LICENSE` file for details.
