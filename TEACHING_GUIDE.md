# 🧭 GitHub Desktop — Step-by-Step Guide (ARTI 409)

This guide walks you through the core GitHub Desktop workflow using this chatbot
project. No command line required — everything happens with buttons and clicks.

**The big idea:** Git takes snapshots of your project over time. GitHub stores those
snapshots online so you can back them up, share them, and work together. GitHub
Desktop is the friendly app that does this for you.

---

## Vocabulary (read this first — it's quick)

| Term | Plain-English meaning |
| --- | --- |
| **Repository** ("repo") | A project folder that Git is tracking. |
| **Commit** | A saved snapshot of your changes, with a short message describing them. |
| **Push** | Upload your commits to GitHub. |
| **Fetch** | Check GitHub for new commits *without* downloading them yet — just a "what's new?" peek. |
| **Pull** | Download commits other people pushed. |
| **Clone** | Make a copy of a GitHub repo on your computer. |
| **origin** | The default nickname for the copy of your repo on GitHub. So "Push origin" just means "push to GitHub." |
| **Branch** | A parallel version of the project where you can work without affecting `main`. |
| **Pull Request** ("PR") | A request to merge your branch's changes into `main`, usually after review. |

---

## Step 0 — Install and sign in

1. Download GitHub Desktop from <https://desktop.github.com> and install it.
2. Open it and sign in with your **GitHub account** (create a free one at
   <https://github.com> if you don't have one).
3. When asked, let it configure your name and email — these get attached to your commits.

---

## Step 1 — Get the project onto your computer

**If your instructor shared a GitHub link** (most common):

First, make your *own* copy of the project on GitHub. This matters: you can only push
changes to a repo you own, so you'll work from your copy — not your instructor's.

1. Open your instructor's repository link in a web browser.
2. Near the top-right, click the green **Use this template → Create a new repository**
   button.
3. Give it a name (e.g. `arti-409-ai-chatbot`), keep it **Public** or **Private** as you
   like, then click **Create repository**. GitHub now has a copy under *your* account. 🎉

Now bring that copy down to your computer:

4. On *your* new repo's page, click the green **Code** button and copy the URL.
5. In GitHub Desktop, go to **File → Clone Repository**, paste the URL, choose where to
   save it, and click **Clone**.

> **Why "Use this template" and not just Clone?** Cloning your instructor's repo directly
> would let you download it, but GitHub would block you from pushing back to it. Working
> from your own copy means every **Push** later in this guide just works.

**If you instead have this project as a plain folder on your computer:**

1. Go to **File → Add Local Repository**.
2. Select the `arti-409-ai-chatbot` folder.
3. If GitHub Desktop says it isn't a Git repository yet, click **create a repository** —
   that turns the folder into one.

---

## Step 2 — Get to know the window

Take 30 seconds to find these parts of GitHub Desktop:

- **Current Repository** (top-left) — which project you're looking at.
- **Current Branch** (top-middle) — which branch you're on (should say `main`).
- **Changes** tab (left side) — files you've edited but not yet committed.
- **History** tab — every commit made so far.
- **Fetch / Push / Pull** button (top-right) — syncs with GitHub.

---

## Step 3 — Make your first commit

1. Open the project folder and edit **README.md** in any text editor. Find the
   **"✏️ Your turn"** section and add your name under it. Save the file.
   - Not sure where the folder is? In GitHub Desktop, use **Repository → Show in
     Finder** (Mac) / **Show in Explorer** (Windows) to open it, or **Repository →
     Open in External Editor** to jump straight into your code editor.
2. Switch back to GitHub Desktop. Your edit appears in the **Changes** tab, with the
   exact lines you added highlighted in green.
3. At the bottom-left, type a short **Summary** message, like:
   `Add my name to the README`.
4. Click **Commit to main**.

✅ You just made a commit — a saved snapshot of your change.

> **Note:** A commit is saved on *your computer* only. It's not on GitHub until you push.

---

## Step 4 — Publish / Push to GitHub

- If this is a brand-new repo, click **Publish repository** (top-right) and choose a
  name. Keep "Keep this code private" checked if you want it private.
- If you cloned it in Step 1, click **Push origin** instead.

Refresh the repository's page on github.com — your change is now online. 🌐

> 🔒 **Notice what's NOT there:** your `.env` file (with your API key) never gets
> uploaded, because `.gitignore` tells Git to skip it. Always keep secrets out of Git.

---

## Step 5 — The everyday loop: edit → commit → push

This is the rhythm you'll repeat constantly:

1. **Edit** a file (try changing the `SYSTEM_PROMPT` in `chatbot.py` to give the bot a
   new personality).
2. **Commit** it in GitHub Desktop with a clear summary.
3. **Push** it to GitHub.

Tip: commit small and often. Each commit should be one logical change with a message
that finishes the sentence *"This commit will…"* — e.g. *"…make the bot reply in pirate speak."*

---

## Step 6 — Branching (work without breaking `main`)

Branches let you experiment safely.

1. Click **Current Branch → New Branch**. Name it something like
   `pirate-personality`. Click **Create Branch**.
2. You're now on the new branch. Make a change (e.g. edit the `SYSTEM_PROMPT`), then
   **commit** it.
3. Click **Publish branch** to push the branch to GitHub.

Your `main` branch is untouched — switch back to it anytime via **Current Branch**.

---

## Step 7 — Open a Pull Request (PR)

A pull request proposes merging your branch into `main`.

1. With your branch pushed, click **Preview Pull Request** (or the banner that appears),
   then **Create Pull Request**. This opens github.com in your browser.
2. Add a title and short description of what you changed, then click
   **Create pull request**.
3. On GitHub, review the changes, then click **Merge pull request → Confirm merge**.

Your branch's changes are now part of `main`.

---

## Step 8 — Pull the latest changes

When someone else (or you, on GitHub) updates `main`, get those updates locally:

1. In GitHub Desktop, make sure you're on the `main` branch.
2. Click **Fetch origin**, then **Pull origin** if there are new changes.

Now your computer matches GitHub. Always **pull before you start working** so you're
building on the latest version.

---

## 🆘 Common hiccups

- **"I don't see my change in GitHub Desktop."** Make sure you **saved** the file in your
  editor first.
- **"I committed but it's not on GitHub."** You still need to **Push**.
- **"It won't let me push — it says pull first."** Someone pushed new commits. Click
  **Pull origin**, then push again.
- **"I edited the wrong branch."** That's okay — you can switch branches and re-do the
  edit, or ask for help. Mistakes are normal and fixable in Git.

---

## ✅ You've learned the whole core workflow

Clone → edit → commit → push → branch → pull request → pull. That's 90% of what you'll
ever do day-to-day with GitHub Desktop. Everything else builds on these steps.
