# How to Develop and Experiment Within This Template

Instead of creating a whole new repository for every change, the best practice is to use **development branches**. Think of a branch as a parallel timeline or a "draft mode" for your project. You can experiment freely on a branch without affecting the stable `main` version.

This is the standard and most efficient way to manage changes.

## Your New Development Workflow

### 1. Create a New Branch
Before you start working on a new feature, bug fix, or experiment, create a new branch from `main`. Give it a descriptive name.

```bash
# Make sure you are on the main branch and have the latest changes
git checkout main
git pull origin main

# Create your new branch and switch to it
# Example names: 'feature/add-new-tool', 'fix/login-bug', 'experiment/refactor-prompts'
git checkout -b <your-branch-name>
```

### 2. Do Your Work
Now you are on your new branch. You can make any changes you want: edit files, add new files, and commit your progress. These changes are isolated to this branch and won't affect `main`.

```bash
# Work on your files...
git add .
git commit -m "Add awesome new feature"
```

### 3. Merge Your Changes
When you are happy with your work and have tested it, you can merge it back into the `main` branch.

```bash
# Switch back to the main branch
git checkout main

# Merge the work from your branch into main
git merge <your-branch-name>
```

### 4. Push to GitHub
Push the updated `main` branch to share your changes.

```bash
git push origin main
```

### 5. Clean Up (Optional)
After merging, you can delete your development branch.

```bash
# Delete the local branch
git branch -d <your-branch-name>

# Delete the remote branch (if you pushed it)
git push origin --delete <your-branch-name>
```

This workflow keeps your `main` branch clean and stable while allowing for flexible and safe development.