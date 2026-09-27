## Git Stash Command Log

### 1. git stash
Command:
git stash

Output:
Saved working directory and index state WIP on feature/add-course

### 2. git stash list
Command:
git stash list

Output:
stash@{0}: WIP on feature/add-course: 61fc29a added course duration feature

### 3. git stash show
Command:
git stash show

Output:
course.py | 5 +++++

### 4. git stash apply
Command:
git stash apply

Output:
Changes restored to the working directory.
The stash remained in the stash list.

### 5. git stash pop
Command:
git stash pop

Output:
Changes restored and the stash entry was removed.

### 6. git stash drop
Command:
git stash drop stash@{0}

Output:
Dropped stash@{0}

## Difference Between git stash apply and git stash pop

git stash apply:
Restores the stashed changes but keeps the stash entry.

git stash pop:
Restores the stashed changes and removes the stash entry after applying it.

Therefore, apply is useful when we may need the same stash again, while pop is useful when we are sure the stash is no longer needed.