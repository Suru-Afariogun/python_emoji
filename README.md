# python_emoji

Python practice

A simple Python script that prints emojis and optional messages from the command line.

## Setup

1. Create a virtual environment:

   ```bash
   python3 -m venv testenv
   source testenv/bin/activate
   ```

2. Install dependencies from requirements.txt:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. Verify installation:
   ```bash
   which python3  # should show .../python_emoji/testenv/bin/python3
   python3 --version
   ```

## Run

Run the script with an emoji name and optional message:

```bash
python3 make_emoji.py --name ':rocket:' --msg 'Lift off!'
```

**Example output:**
🚀 Lift off!

You can also use it with just an emoji:

```bash
python3 make_emoji.py --name ':sparkles:'
```

## Time it

Performance benchmark for emoji conversion:

```bash
python3 -m timeit -n 1000 -s "from emoji import emojize" "emojize(':rocket:')"
```

**Example result:**
1000 loops, best of 5: X.XX usec per loop
_(Replace X.XX with your actual timing results)_

## Test

Run the test suite using pytest:

```bash
pytest -q
```

This will run the smoke test to verify the script runs correctly and prints emojis.
