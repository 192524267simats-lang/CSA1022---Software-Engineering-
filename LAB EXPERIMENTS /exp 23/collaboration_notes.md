# Pull collaborator changes

After a collaborator pushes to `main`, update your local branch:
```bash
git switch main
git pull origin main
```
Verify the collaborator's new commit and changed file with `git log --oneline -5` and `git status`.
