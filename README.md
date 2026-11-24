# Lab 11 - Intermediate Programming: Async and Sockets

This lab practises the first two topics of the intermediate unit: **asynchronous code**
(`asyncio` - overlapping work that's mostly *waiting*) and **sockets** (talking between
programs over the network). You'll write two async functions and a socket client, plus
an optional socket server.

**Time:** this lab is meant to be finished in the 80-minute session. If you don't
finish, you may keep working during the week and submit any time up to the **first 10
minutes of next week's lab**.  After 10 minutes, though, the lab will not be accepted,
to avoid a cascade effect. The **Lab 11 quiz on Canvas** closes at that moment - that is
where you hand this lab in, so read [How to Submit](#how-to-submit) before you start.

## Getting Started

Lab repositories are **templates**: you make your own copy with one click.

1. Open the **Lab 11 template** link in the Canvas lab quiz.
2. Click the green **Use this template** button, then **Create a new repository**.
3. Fill in the form:
   - **Owner:** Your own account
   - **Repository name:** `lab11-csci1030u`
   - **Visibility:** **Private**
4. Click **Create repository**.

Use **Use this template**, not **Fork** - a fork can never be made private, which would
show your solution to the whole class.  For the TA to see your work, you will need to add them as a collaborator.

Then clone it. On your new repo's page, click the green **Code** button and copy the URL.
In the folder where you keep your CSCI 1030U labs:

```
git clone https://github.com/CSCI1030U/lab11-your-username
cd lab11-your-username
```

## How to approach each problem

As before: **work out the outline first** - restate the problem, try a small example,
and sketch the steps - *then* turn it into code (you may use an AI assistant to help;
see **Using AI**). Each function has an `# Outline` comment to plan in.

## Problems

Edit **`lab11.py`** for Parts 1-3, and **`reverse_server.py`** for the stretch. Don't
rename the functions - the tests use these names.

### Part 1 - `gather_doubled(numbers)`  *(async)*

Write the `async` function `gather_doubled` so it runs one small async task per number -
each returning `n * 2` - **all at the same time** with `asyncio.gather`, and returns the
results as a list in the **same order** as `numbers`.

```python
import asyncio
asyncio.run(gather_doubled([1, 2, 3, 4]))   # returns [2, 4, 6, 8]
```

Hint: `asyncio.gather(*coros)` runs many coroutines concurrently and returns their
results in the order you passed them in.

### Part 2 - `fastest(jobs)`  *(async)*

`jobs` is a list of `(label, delay)` pairs. Start them **all at once** - each one just
does `await asyncio.sleep(delay)` - and return the **label of the first job to finish**.

```python
asyncio.run(fastest([("A", 0.06), ("B", 0.02), ("C", 0.04)]))   # returns "B"
```

Hint: `asyncio.as_completed(coros)` lets you loop over the results *as they finish*, so
the very first one you get back is the winner.

### Part 3 - `echo_once(host, port, message)`  *(sockets)*

Write a socket **client**: connect a TCP socket to `(host, port)`, send `message`,
receive the server's reply, and return it as a string. (An **echo** server sends back
exactly what it received, so against one, `echo_once` returns `message` unchanged.)

```python
echo_once("127.0.0.1", 50011, "hello")   # returns "hello"   (against an echo server)
```

Hint: `socket.socket(...)`, then `.connect((host, port))`, `.sendall(message.encode())`,
`data = .recv(1024)`, and `data.decode()`.

### Part 4 - `reverse_server.py`  *(stretch - optional, spot-checked)*

Finish `reverse_server.py` so that when a client sends a message, the server sends it
back **reversed** (`"hello"` -> `"olleh"`). The socket setup is written for you - fill
in the one `# TODO`.

**There's no automated test for the server** (a server is checked by running it). Test
it yourself: run the server in one terminal, and in another use the included client:

```
# terminal 1
python reverse_server.py

# terminal 2
python client.py hello        # prints: olleh
```

Show it to your lab instructor. This part is optional - the three above are the core.

## Verifying Correctness

Run the pre-written tests to check Parts 1-3:

```
pytest
```

The socket test starts its own little echo server on a spare port and connects your
`echo_once` to it, so you don't need to run anything by hand. (The tests don't cover
`reverse_server.py` - check that one with `client.py`.)

## Getting Help

There is a lab instructor present for the whole session. Ask them whenever you're
stuck.

*The instructor will usually help you find the problem rather than tell you how to
fix it - the goal is for you to get better at diagnosing and fixing your own bugs.*

## How to Submit

Handing in a lab is two steps: **push your work**, then **record it in the Canvas quiz**.
This is the same routine for every lab.

### Step 1 - Commit and push

Once your tests pass (or the session is ending):

```
git add --all
git commit -m "Lab 11 completed"
git push origin main
```

Then open your repository page on GitHub and check that your changed files are actually
there. That is your confirmation the push worked.

> **Check your own work with `pytest`, on your own machine.** Your repository has an
> autograder, but it does not run when you push - your instructor runs it during marking,
> against the commit hash you submit below. So `pytest` passing locally is the only
> pass/fail signal you get, and it is the one that counts. Don't submit without running it.

### Step 2 - Get the commit hash

Check that everything really is committed and pushed, then read the hash of that snapshot:

```
git status
git rev-parse HEAD
```

`git status` should say `nothing to commit, working tree clean` and that your branch is up
to date with `origin/main`. If it lists changes, go back to Step 1. Then `git rev-parse HEAD`
prints a 40-character hash, like `3f9a1c2e8b7d4056a1f2e3d4c5b6a7f8091a2b3c`.

### Step 3 - Submit the quiz

Open the **Lab 11 quiz on Canvas** and enter:

- your **repository URL**: `https://github.com/CSCI1030U/lab11-your-username`
- your **commit hash**, pasted exactly as `git rev-parse HEAD` printed it

Then answer the remaining questions and submit. **The Canvas submission time is your
submission time**, and the commit hash you give is the snapshot that gets marked - anything
you push afterwards is not seen. If you fix something important later, get the new hash and
resubmit if the quiz still allows it.

## Using AI

You **may use an AI assistant to help you write the code** for this lab. Build the habit
first, though: **work out the outline yourself before you involve the AI.** Async and
sockets have a lot of small moving parts, so it's especially worth understanding the
shape of the solution before generating it - restate the problem, sketch the steps,
*then* lean on the AI to fill in the API details.

Use a free model, and be ready to **explain and modify** any code you submit - the lab
instructor may ask you to walk through it or change how it works.
