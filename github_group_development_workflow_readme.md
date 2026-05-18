# GitHub Development Workflow

## Repository Setup

1. One group member forks the original assignment repository.
2. The forked repository becomes the main group repository.
3. All group members are added as collaborators.
4. Everyone clones the same repository locally.

---

# Clone the Repository

```bash
git clone https://github.com/YOUR_GROUP_REPO/COMP90042_2026.git
```

Enter the project folder:

```bash
cd COMP90042_2026
```

---

# Create Your Own Branch

Never work directly on `main`.

Create your own branch before starting development:

```bash
git checkout -b your-branch-name
```

Examples:

```bash
git checkout -b tokenization
git checkout -b retrieval
git checkout -b evaluation
git checkout -b junzhe-work
```

---

# Development Workflow

## Step 1 — Pull Latest Changes

Before starting work every time:

```bash
git checkout main
git pull origin main
```

Then switch back to your branch:

```bash
git checkout your-branch-name
```

Update your branch:

```bash
git merge main
```

---

## Step 2 — Make Changes

Modify your assigned files only.

Avoid editing files unrelated to your task.

---

## Step 3 — Save Changes

```bash
git add .
git commit -m "Describe your changes"
```

Examples:

```bash
git commit -m "Finish tokenization pipeline"
git commit -m "Add evidence retrieval"
git commit -m "Fix evaluation metrics"
```

---

## Step 4 — Push to GitHub

```bash
git push origin your-branch-name
```

---

## Step 5 — Create Pull Request

1. Open the GitHub repository.
2. GitHub will show a button:

```text
Compare & pull request
```

3. Create the pull request.
4. Another teammate reviews the changes.
5. Merge into `main` after confirmation.

---

# Important Rules

## Do NOT Work Directly on Main

Never push directly to:

```text
main
```

Always use branches.

---

# Jupyter Notebook Rules

`.ipynb` files are difficult to merge.

To avoid conflicts:

- One task = one notebook
- Avoid multiple people editing the same notebook
- Commit frequently

Recommended structure:

```text
notebooks/
├── tokenization.ipynb
├── retrieval.ipynb
├── evaluation.ipynb
```

---

# Dataset Rules

Do NOT:

- Rename original datasets
- Delete datasets
- Upload duplicated datasets
- Modify provided ground truth files

Store generated outputs separately:

```text
outputs/
results/
cache/
```

---

# Recommended Project Structure

```text
COMP90042_2026/
│
├── data/
├── notebooks/
├── outputs/
├── src/
├── README.md
└── requirements.txt
```

---

# Google Colab Workflow

Recommended setup:

- Use Google Colab for running notebooks
- Use GitHub for version control

Typical workflow:

1. Pull latest changes from GitHub
2. Open notebook in Colab
3. Work on notebook
4. Save notebook back to GitHub
5. Commit and push changes

---

# Common Git Commands

## Check Current Branch

```bash
git branch
```

---

## See Modified Files

```bash
git status
```

---

## Pull Latest Changes

```bash
git pull origin main
```

---

## Push Changes

```bash
git push origin your-branch-name
```

---

## Switch Branch

```bash
git checkout branch-name
```

---

# Conflict Handling

If conflicts happen:

1. Do not panic.
2. Read the conflict markers carefully.
3. Keep the correct code.
4. Remove conflict markers.
5. Commit again.

Conflict markers look like:

```text
<<<<<<< HEAD
Your code
=======
Other person's code
>>>>>>> branch-name
```

---

# Team Coordination Suggestions

Recommended task split:

| Member | Task |
|---|---|
| Person A | Retrieval |
| Person B | Tokenization |
| Person C | Evaluation |

Avoid multiple people modifying the same notebook simultaneously.

---

# Final Submission Checklist

Before submission:

- All notebooks run successfully
- No missing dataset paths
- No unnecessary output files
- No broken imports
- requirements.txt updated
- README updated
- Final code merged into main

---

# Recommended Commit Frequency

Commit small changes frequently.

Good:

```text
Implement tokenizer
Add evidence filtering
Fix retrieval bug
```

Bad:

```text
Final update
Stuff
Changes
```

---

# Recommended Branch Naming

Good examples:

```text
retrieval
tokenization
evaluation
bugfix-parser
junzhe-work
```

Avoid:

```text
newbranch
test123
finalfinal
```

---

# Important Reminder

Always:

```text
Pull before you push.
```

This prevents many merge conflicts.

