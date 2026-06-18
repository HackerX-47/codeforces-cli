# codeforces-cli

A command-line tool for pulling and analyzing your Codeforces profile, rating history, and submissions — straight from the terminal.

## Features

- **User lookup** — handle, full name, current/max rating, rank, organization.
- **Rating history** — contest-by-contest rating changes, with Div. 1/2/3 contest type parsing.
- **Submissions tracker** — recent submissions with verdict, problem rating, and language.
  - `--only-ac` — show only accepted submissions.
  - `--lang` — filter by programming language (e.g. `cpp`, `python`, `java`).
  - `--problem` — filter by problem index (e.g. `A`, `B1`).
  - Auto-generated summary: accuracy %, total submissions, most-used language.

## Demo

```bash
$ cfcli user tourist

user details
----------------------------
handle       :  tourist
full name    :  Gennady Korotkevich
rating       :  3979
max rating   :  4009
rank         :  Legendary grandmaster
organization :  ITMO University
```

```bash
$ cfcli submissions HackerX_47 --last 10 --only-ac --lang cpp

prob  rating     verdict    lang
----------------------------------------------------
A     800        AC         GNU C++17
B     1200       AC         GNU C++17

Summary
------------------
AC           :  2
Total        :  2
Accuracy     :  100.00%
Top Language :  cpp
```

## Installation

Requires Python 3.8+.

```bash
git clone https://github.com/HackerX-47/codeforces-cli.git
cd codeforces-cli
pip install -e .
```

This installs `cfcli` as a command available from any directory.

## Usage

```bash
# Look up a user's profile
cfcli user <handle>

# View rating history across contests
cfcli rating <handle>

# View recent submissions (default: last 20)
cfcli submissions <handle>

# Filter submissions
cfcli submissions <handle> --last 50
cfcli submissions <handle> --only-ac
cfcli submissions <handle> --lang python
cfcli submissions <handle> --problem B1
cfcli submissions <handle> --last 100 --only-ac --lang cpp --problem C
```

## Project Structure

```
cfcli/
├── main.py                 # CLI entrypoint, registers all commands
├── api.py                  # Codeforces API wrapper, error handling
├── functions.py            # Shared helpers (language normalization, summary)
├── imports.py              # Centralized third-party imports
└── commands/
    ├── user.py                 # `cfcli user`
    ├── rating.py               # `cfcli rating`
    └── submissions.py          # `cfcli submissions`
```

The API layer, formatting/aggregation logic, and CLI wiring are kept in separate modules so each piece can be tested or modified independently of the others.

## Motivation

Built to move past tutorials and apply core Python concepts — REST API consumption, error handling for real network failures, CLI design with Click, data aggregation, and Python packaging — against a live, public dataset (Codeforces' API) rather than toy exercises.

## Tech Stack

- [Click](https://click.palletsprojects.com/) — CLI framework
- [Requests](https://requests.readthedocs.io/) — HTTP client
- [Codeforces API](https://codeforces.com/apiHelp) — data source

## Possible Future Additions

- Combine filters with AND/OR logic (e.g. multiple `--lang` values)
- Add more filters by contest type or rating range
- Export submissions/rating history to CSV
- Compare stats between two handles

## Author

[HackerX-47](https://github.com/HackerX-47)
