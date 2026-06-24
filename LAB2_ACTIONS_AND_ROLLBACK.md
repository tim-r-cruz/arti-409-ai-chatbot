# 🚦 GitHub Actions & Rolling Back — Step-by-Step (ARTI 409 · Lab 2)

In Lab 1 you learned to **save and share** code with GitHub Desktop. In this lab you'll
teach GitHub to **check your code automatically** every time you push, then watch it
**catch a mistake** — and learn how to **safely undo** that mistake.

**The big idea:** A real AI system isn't "done" when you ship it — it has to be *kept
healthy*. Two habits make that possible: an automatic safety net that tests your code on
every change (**Continuous Integration**), and a calm, reliable way to **roll back** to a
known-good version when something breaks. That's exactly what you'll practice today.

Everything happens in **GitHub Desktop** and the **GitHub website** — no command line.

---

## Vocabulary (read this first — it's quick)

| Term | Plain-English meaning |
| --- | --- |
| **Continuous Integration (CI)** | Having a service automatically check your code every time you push. Your safety net. |
| **GitHub Actions** | GitHub's built-in tool for running CI (and other automation) for free. |
| **Workflow** | A small `.yml` file in `.github/workflows/` that tells Actions *what to do*. |
| **Run** (or **job**) | One execution of your workflow. Every push starts a fresh run. |
| **YAML** (`.yml`) | A simple text format for settings. **Spacing matters** — indent with spaces, never tabs. |
| **Test** | A tiny piece of code that checks another piece of code is behaving correctly. |
| **Status check** | The ✅ (passed) or ❌ (failed) mark Actions reports on your commits and pull requests. |
| **Revert** | A *safe undo* — a brand-new commit that cancels out an earlier one. Nothing is lost. |

---

## Before you start

Make sure you've got Lab 1 wrapped up:

- ✅ You finished the **[TEACHING_GUIDE.md](TEACHING_GUIDE.md)** lab and have **your own
  copy** of the chatbot repo (created with **Use this template**).
- ✅ **GitHub Desktop** is signed in, and the repo opens in it.
- ✅ You're on the **`main`** branch. Click **Fetch origin**, then **Pull origin** if
  there's anything to pull, so you're starting fresh.

> **What you'll build:** two small files — a *test* (`test_chatbot.py`) and a *workflow*
> (`.github/workflows/ci.yml`). You'll create them yourself, so it doesn't matter that
> your copy came from a template. 🎉

---

## Part 1 — Warm-up (≈10 min)

Let's re-activate your Lab 1 skills and look at where CI will live.

1. In GitHub Desktop, confirm **Current Branch** says `main`, then click
   **Fetch origin** (top-right) to make sure you're up to date.
2. Open your repo on **github.com** (in Desktop: **Repository → View on GitHub**).
3. Near the top of the page, click the **Actions** tab. You'll see *"Get started with
   GitHub Actions."* It's empty — that's expected. By the end of Part 2 there'll be a run
   here. Leave this tab open in a browser; we'll come back to it.
4. Open **`chatbot.py`** (in Desktop: **Repository → Open in External Editor**) and find
   these two lines near the top — these are what our test will check:

   ```python
   MODEL = "claude-opus-4-8"
   ...
   SYSTEM_PROMPT = (
       "You are a friendly, encouraging teaching assistant for ARTI 409, "
       ...
   )
   ```

✅ **Checkpoint:** you're on `main`, up to date, and you've found the `Actions` tab and
the two lines we'll be testing.

---

## Part 2 — Add an automatic test with GitHub Actions (≈35 min)

You'll add two files **on the GitHub website** (its editor creates folders for you, which
is fiddly to do by hand), bundle them in a **pull request** like you learned in Lab 1,
and watch the test run.

### 2a. Create the test file

1. On your repo's main page (github.com), click **Add file ▾ → Create new file**.
2. In the filename box at the top, type exactly:

   ```
   test_chatbot.py
   ```
3. Paste this into the big editing area:

   ```python
   """Tiny smoke tests for the ARTI 409 chatbot. No API key needed."""

   import chatbot


   def test_model_is_a_known_claude_model():
       # If someone fat-fingers the model name, this fails before it reaches main.
       assert chatbot.MODEL in {"claude-opus-4-8", "claude-haiku-4-5"}


   def test_system_prompt_mentions_the_course():
       # The assistant should know it's helping with ARTI 409.
       assert "ARTI 409" in chatbot.SYSTEM_PROMPT
   ```
4. Scroll down to **Commit changes**. Choose **Create a new branch for this commit and
   start a pull request**, name the branch `add-ci`, and click **Propose new file**.
5. On the next screen click **Create pull request**. Leave this PR open in your browser.

> **Why a test for tiny settings?** We're keeping the *Python* dead simple so the focus
> stays on **GitHub**, exactly like Lab 1. The test just confirms two important settings
> are still sane — but it behaves like any real test: green when things are fine, red when
> they're not.

### 2b. Create the workflow file (this turns CI on)

1. Use the **branch dropdown** (the button that says `main`) and switch to your new
   **`add-ci`** branch.
2. Click **Add file ▾ → Create new file** again.
3. In the filename box, type this *exactly* — including the slashes. As you type the
   slashes, GitHub creates the folders for you:

   ```
   .github/workflows/ci.yml
   ```
4. Paste this in:

   ```yaml
   name: CI

   # Run on every push and every pull request.
   on:
     push:
     pull_request:

   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - name: Check out the code
           uses: actions/checkout@v4

         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: "3.11"

         - name: Install dependencies
           run: pip install -r requirements.txt pytest

         - name: Run the tests
           run: pytest -v
   ```
5. Scroll to **Commit changes**, make sure it says **Commit directly to the `add-ci`
   branch**, and click **Commit changes**.

> ⚠️ **YAML is picky about spacing.** Use the snippet above as-is. Every indent is
> **spaces**, never tabs, and the number of spaces matters. If your run later fails before
> any test prints, indentation is the usual culprit.

### 2c. Watch it run and merge

1. Go back to your **pull request** (the **Pull requests** tab → your `add-ci` PR). Near
   the bottom you'll now see a check running — a yellow dot 🟡 *"Some checks haven't
   completed yet."*
2. Give it a minute. It turns into a green **✅ All checks have passed**. Click
   **Details** to watch the steps (checkout → install → run tests) if you're curious.
3. Click **Merge pull request → Confirm merge**. Your test + workflow are now on `main`.

### 2d. Bring it down to your computer

1. Switch back to **GitHub Desktop**, make sure you're on **`main`**.
2. Click **Fetch origin**, then **Pull origin**. The two new files appear in your local
   folder.

✅ **Checkpoint:** Your repo now has a green ✅ next to its latest commit on github.com,
and `test_chatbot.py` + `.github/workflows/ci.yml` exist on your computer. **You now have
CI.** Every push from here on gets checked automatically.

> 🔒 **Notice (callback to Lab 1):** CI ran on a clean cloud machine that has **no `.env`
> and no API key** — and it still passed, because the tests never call Claude. Keeping
> secrets out of Git (Lab 1) is what makes free, automatic checks like this possible.

---

## Part 3 — Break it on purpose (≈20 min)

Time to see your safety net actually catch something.

1. In your code editor, open **`chatbot.py`** and find the `SYSTEM_PROMPT`. Change the
   words **`ARTI 409`** to **`your course`**, so the first line reads:

   ```python
   SYSTEM_PROMPT = (
       "You are a friendly, encouraging teaching assistant for your course, "
   ```
   Save the file. (Pretend a teammate "improved" the wording and accidentally dropped the
   course name — a small, realistic regression.)
2. In **GitHub Desktop**, you'll see the change in the **Changes** tab. Give it a summary
   like `Reword the bot's persona` and click **Commit to main**.
3. Click **Push origin**.

> **Heads-up:** normally you'd do this on a *branch* and let the red check warn you
> *before* merging. We're committing straight to `main` here so you can watch CI react on
> `main` and have something to practice **rolling back**. (More on preventing this in the
> wrap-up.)

4. Switch to your browser and open the **Actions** tab (or click the little status mark
   next to your newest commit). The run starts 🟡… and turns **❌ red**.
5. Click into the failed run, open the **Run the tests** step, and read the bottom. You'll
   see something like:

   ```
   FAILED test_chatbot.py::test_system_prompt_mentions_the_course
   assert 'ARTI 409' in '...teaching assistant for your course...'
   ```

✅ **Checkpoint:** You made a change, CI went red, and you found the exact test and line
that failed. **This is CI doing its job** — flagging a problem the moment it lands.

---

## Part 4 — Roll it back (≈25 min)

Your `main` is "broken" (red). Let's get back to a known-good, green state — the safe way.

### 4a. Revert in GitHub Desktop (you do this)

1. In GitHub Desktop, click the **History** tab (top-left, next to **Changes**).
2. Find your **`Reword the bot's persona`** commit. **Right-click it** and choose
   **Revert Changes in Commit**.
3. GitHub Desktop creates a *new* commit named **`Revert "Reword the bot's persona"`**
   that puts the old wording back. Your `ARTI 409` text is restored — go check
   `chatbot.py` if you like.
4. Click **Push origin**.
5. Back on the **Actions** tab, watch the new run go 🟡 → **✅ green**. You're back to a
   healthy `main`.

> **Why *revert* instead of just deleting the commit?** A revert *adds* a new commit that
> undoes the old one. Nothing disappears from history, and anyone else who already pulled
> the bad commit stays in sync. It's the safe, team-friendly undo. (The scarier
> history-rewriting undos — `reset`, force-push — are a command-line topic for another
> day. You don't need them here.)

### 4b. The team version, on the website (good to know)

You don't need to do this now — just so you've seen it: when a bad change arrives through
a **merged pull request**, GitHub shows a **Revert** button right on that PR. Clicking it
opens a *new* revert PR for your team to review and merge. Same safe idea as 4a, built for
collaboration.

✅ **Checkpoint:** `main` is green again, and your **History** shows both the breaking
commit *and* the revert sitting on top of it — proof that the fix is recorded, not hidden.

---

## Part 5 — Wrap-up & reflect (≈10 min)

You just lived the core loop of **keeping software alive**:

> **add a check → push → read the result → break something → catch it → roll back.**

Think about how this maps to running a real AI system (like the monitoring work you've
done with MLflow and Evidently):

1. **CI is an early-warning system.** A test going red is the cheapest place to catch a
   problem — long before a user does.
2. **Revert is your recovery plan.** When something does slip through, the goal isn't
   panic, it's *getting back to a known-good version quickly and calmly.*
3. **One question to take with you:** in Part 3 you were *able* to push a broken commit
   straight to `main`. How could a team stop that from happening? (Peek ahead:
   GitHub → **Settings → Branches → Branch protection rules** can *require* the ✅ check to
   pass before anyone is allowed to merge. That turns CI from a *warning* into a *gate*.)

### ✅ Proof of completion (optional submission)

Take **two screenshots** and submit them:

1. Your **green ✅ CI run** on the Actions tab.
2. Your **History** in GitHub Desktop showing the `Revert "…"` commit on top.

---

## 🆘 Common hiccups

- **"My `Actions` tab says workflows are disabled."** Go to **Settings → Actions →
  General**, choose **Allow all actions**, and save. (Repos made from a template
  sometimes start with Actions off.)
- **"The run is red but I didn't change any code."** It's almost always **YAML spacing**
  in `ci.yml`. Re-paste the snippet from Part 2b exactly — spaces, not tabs.
- **"The log says `ModuleNotFoundError: No module named 'chatbot'`."** Your
  `test_chatbot.py` must sit in the **top folder** of the repo, right next to
  `chatbot.py` — not inside a subfolder.
- **"The log says it can't find `anthropic`."** The **Install dependencies** step didn't
  run or was edited. Check that line reads `pip install -r requirements.txt pytest`.
- **"GitHub Desktop won't let me push — it says *pull first*."** Someone (maybe you, on
  the website) pushed new commits. Click **Pull origin**, then **Push origin** again.
  (Same fix as Lab 1.)
- **"I pulled but don't see the new files."** Make sure you merged the PR *and* you're on
  `main` in Desktop before **Fetch/Pull**.
- **"I reverted the wrong commit."** No harm done — reverts are safe and themselves
  revertible. Just revert again, or revert your revert.

---

## ✅ You've learned the maintenance workflow

**Add CI with GitHub Actions → read a status check → catch a regression → roll it back
with Revert.** That's the heartbeat of keeping any project — especially a live AI system —
healthy over time. Everything fancier (required checks, more tests, automatic
deployments) is just more of this same rhythm.
