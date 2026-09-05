# Codeforces CLI

A terminal-based Codeforces performance analytics tool that turns Codeforces user, contest, and submission data into structured statistics, visual reports, and AI-powered performance insights.

Codeforces CLI started as a simple command-line utility for viewing user information, rating history, and submissions. Version 2 expands it into a performance analysis tool with data processing, visualization, and AI-generated recommendations.

---

## Overview

Codeforces CLI provides a terminal interface for analyzing Codeforces profiles without manually navigating through multiple pages of contest history, submissions, and problem statistics.

Version 2 introduces a complete analytics layer on top of the original functionality.

The tool can:

* Fetch Codeforces user information
* Analyze contest rating history
* Analyze recent submissions
* Filter submissions
* Calculate submission and problem-solving statistics
* Generate performance visualizations
* Analyze performance by problem difficulty and tags
* Analyze performance across different times of day
* Track monthly solving progression
* Generate an AI-powered performance report
* Produce a personalized action plan based on performance patterns

The overall V2 pipeline can be summarized as:

```text
Codeforces API
      |
      v
Data Fetching
      |
      v
Data Processing
      |
      v
Performance Metrics
      |
      +-------------------+
      |                   |
      v                   v
 Terminal Output      Visualizations
      |                   |
      |                   v
      |              PNG Reports
      |
      v
 Gemini API
      |
      v
AI Performance Analysis
      |
      v
Action Plan
```

---

# What's New in V2

Version 2 builds on the functionality of V1 while introducing deeper analysis and a more structured architecture.

| Capability                  |      V1 |       V2 |
| --------------------------- | ------: | -------: |
| User information            |     Yes |      Yes |
| Contest rating history      |     Yes |      Yes |
| Submission analysis         |     Yes |      Yes |
| Submission filters          |     Yes |      Yes |
| Rating analytics            |   Basic | Extended |
| Problem difficulty analysis | Limited |      Yes |
| Tag performance analysis    |      No |      Yes |
| Time-of-day analysis        |      No |      Yes |
| Monthly progression         |      No |      Yes |
| Performance visualizations  |      No |      Yes |
| AI-powered analysis         |      No |      Yes |
| Personalized action plan    |      No |      Yes |
| Structured architecture     |   Basic |      Yes |
| Refined terminal output     |   Basic |      Yes |
| Pandas-based analytics      |      No |      Yes |
| Matplotlib visualizations   |      No |      Yes |

The major change in V2 is not simply the addition of two commands.

V1 primarily answered:

> "What is this user's Codeforces activity?"

V2 aims to answer:

> "What does this user's Codeforces activity say about their performance, strengths, weaknesses, and next steps?"

---

# Features

## 1. User

```bash
cfv2 user <handle>
```

Displays basic Codeforces profile information:

* Handle
* Full name
* Maximum rating
* Current rank
* Organization

### Example

```bash
cfv2 user hackerx_47
```

Output:

```text
USER DETAILS
────────────
handle       :  HackerX_47
full name    :  Omkar
max rating   :  985
rank         :  Newbie
organization :  NIT Durgapur
```

---

## 2. Rating

```bash
cfv2 rating <handle>
```

Analyzes a user's contest rating history and provides:

* Current rating
* Best rating
* Worst rating
* Overall rating change
* Number of contests
* Average rating change
* Positive contests
* Negative contests
* No-change contests
* Best contest rank
* Worst contest rank
* Average contest rank
* Contest-by-contest rating progression

### Example

```bash
cfv2 rating hackerx_47
```

Output:

```text
RATING
────────────────────────────────────────
RATING OVERVIEW
  Current rating           : 985
  Best rating              : 985
  Worst rating             : 384
  Overall change           : +985

CONTEST PERFORMANCE
  Total contests           : 5
  Avg rating change        : +197.00
  Positive contests        : 5
  Negative contests        : 0
  No change                : 0

RANK PERFORMANCE
  Best rank                : 13527
  Worst rank               : 8929
  Avg rank                 : 11506.0

CONTEST TYPE                   RANK   ΔRATING CURR RATING
─────────────────────────────────────────────────────────
Div. 2                        12045      +384         384
Div. 2                        13527      +231         615
Div. 2                         8929      +222         837
Div. 2                        11034       +95         932
Div. 2                        11995       +53         985
```

---

## 3. Submissions

```bash
cfv2 submissions <handle>
```

Analyzes recent Codeforces submissions.

The command provides:

* Total submissions
* Accepted submissions
* Acceptance rate
* Most-used programming language
* Unique problems attempted
* Unique problems solved
* Average attempts per solved problem
* Average solved problem rating
* Highest solved rating
* Lowest solved rating
* Submission-by-submission details

### Submission Filters

V2 supports filters for narrowing down submission analysis.

#### Last N submissions

```bash
cfv2 submissions hackerx_47 --last 10
```

#### Accepted submissions only

```bash
cfv2 submissions hackerx_47 --only-ac
```

#### Filter by problem index

```bash
cfv2 submissions hackerx_47 --problem B
```

Filters can be combined where supported.

### Example

```bash
cfv2 submissions hackerx_47 --last 10
```

Output:

```text
SUMMARY
────────────────────────────────────────
SUBMISSIONS
  Total submissions       : 10
  Accepted                : 6
  Accuracy                : 60.00%
  Top language            : cpp

PROBLEM PROGRESS
  Unique attempted        : 5
  Unique solved           : 5
  Avg attempts / solve    : 2.00

PROBLEM DIFFICULTY
  Avg solved rating       : 1000
  Highest solved rating   : 1000
  Lowest solved rating    : 1000

TYPE RATING    VERDICT   LANG
─────────────────────────────────────────────────
B    1000      AC        C++23 (GCC 14-64, msys2)
B    1000      WA        C++23 (GCC 14-64, msys2)
B    1000      WA        C++23 (GCC 14-64, msys2)
B    1000      WA        C++23 (GCC 14-64, msys2)
B    1000      AC        C++23 (GCC 14-64, msys2)
D    1000      AC        C++23 (GCC 14-64, msys2)
C    1000      AC        C++23 (GCC 14-64, msys2)
C    1000      WA        C++23 (GCC 14-64, msys2)
B    1000      AC        C++23 (GCC 14-64, msys2)
B    1000      AC        C++23 (GCC 14-64, msys2)
```

---

# 4. Graph

```bash
cfv2 graph <handle>
```

The graph command generates a visual performance report for a Codeforces user.

V2 currently generates six visualizations:

1. Rating trajectory
2. Monthly solving activity
3. Rating-range performance
4. Tag performance
5. Time-of-day performance
6. Verdict distribution

### Example

```bash
cfv2 graph hackerx_47
```

Output:

```text
GENERATING VISUAL REPORT
─────────────────────────────────────────────
✓ Rating trajectory saved
  → images/hackerx_47/rating-trajectory.png

✓ Monthly solving activity saved
  → images/hackerx_47/monthly-solving.png

✓ Tag performance saved
  → images/hackerx_47/tag-performance.png

✓ Rating range performance saved
  → images/hackerx_47/rating-range-performance.png

✓ Time-of-day performance saved
  → images/hackerx_47/time-of-day-performance.png

✓ Verdict distribution saved
  → images/hackerx_47/verdict-count.png
```

Generated graphs are stored separately for each Codeforces handle:

```text
images/
└── hackerx_47/
    ├── monthly_solving.png
    ├── rating-range_performance.png
    ├── rating-trajectory.png
    ├── tag-performance.png
    ├── time-of-day-performance.png
    └── verdict-count.png
```

---

# 5. Summary

```bash
cfv2 summary <handle>
```

The summary command generates a comprehensive Codeforces performance analysis.

Unlike the other commands, which primarily present calculated statistics, the summary command combines structured performance metrics with the Gemini API to produce higher-level interpretation and recommendations.

The report covers:

* Overall performance
* Strongest aspects
* Biggest weaknesses
* Rating journey
* Problem difficulty
* Tag performance
* Time-of-day performance
* Monthly progression
* Personalized action plan

### Example

```bash
cfv2 summary hackerx_47
```

Example output:

```text
CODEFORCES PERFORMANCE ANALYSIS REPORT: HACKERX_47

[1] OVERALL PERFORMANCE
--------------------------------------------------
User Summary
  Handle          : HackerX_47
  Rank            : Newbie
  Current Rating  : 985
  Max Rating      : 985
  Problems Solved : 247 / 263 attempted
  Total Submissions: 510
  Overall AC Rate : 50.98%

General Performance
  • Currently positioned at the upper boundary of the Newbie rank with a 985 rating.
  • Shows solid overall activity with 510 total submissions and 247 unique problems solved.
  • Demonstrates strong persistence, successfully solving 93.92% of attempted problems eventually.

Strongest Aspects
  • Perfect completion rate on 800-rated problems.
  • High volume practice in Math, Greedy, and Implementation.
  • Undefeated record in official contests across 5 contest appearances.

Biggest Weaknesses
  • High submission error rate, driven by 200 Wrong Answer verdicts.
  • Significant drop in acceptance rate on 1300-rated problems.
  • Poor submission accuracy during late-night practice sessions.
```

The report continues with rating progression, difficulty analysis, tag performance, time-of-day performance, monthly progression, and an action plan.

For example, the action plan can identify specific performance bottlenecks:

```text
[01] REDUCE WRONG ANSWERS BEFORE SUBMITTING
───────────────────────────────────────────

INSIGHT
200 WA verdicts out of 510 total submissions.

ACTION
Stress-test code locally with edge cases and manual tests before submitting.

GOAL
Lower average attempts per solve from 1.91 to below 1.40.
```

And:

```text
[02] BREAK THROUGH THE 1100-1300 DIFFICULTY BARRIER
───────────────────────────────────────────────────

INSIGHT
Acceptance rate drops from 51.85% at 1000 rating
to 42.34% at 1100 and 19.44% at 1300.

ACTION
Practice 3-5 problems daily strictly within the 1100-1300 rating window.

GOAL
Achieve more than 50% first-try acceptance on 1100-1200 problems.
```

This makes the summary command more than a statistical report: it converts measured performance into concrete areas for improvement.

---

# Command Reference

| Command                     | Description                              |
| --------------------------- | ---------------------------------------- |
| `cfv2 user <handle>`        | Display Codeforces user information      |
| `cfv2 rating <handle>`      | Analyze contest rating and rank history  |
| `cfv2 submissions <handle>` | Analyze recent submissions               |
| `cfv2 graph <handle>`       | Generate visual performance reports      |
| `cfv2 summary <handle>`     | Generate AI-powered performance analysis |

---

# Complete Usage Example

A complete analysis of a Codeforces user can be performed with:

```bash
cfv2 user hackerx_47
cfv2 rating hackerx_47
cfv2 submissions hackerx_47 --last 50
cfv2 graph hackerx_47
cfv2 summary hackerx_47
```

Each command answers a different question:

```text
user
 |
 +-- Who is this user?
 |
rating
 |
 +-- How has their contest rating changed?
 |
submissions
 |
 +-- How are they solving problems?
 |
graph
 |
 +-- What do their performance patterns look like visually?
 |
summary
 |
 +-- What are their strengths, weaknesses, and next steps?
```

---

# Analytics

V2 processes Codeforces data across several dimensions.

## Rating Analytics

The rating analysis examines:

* Current rating
* Maximum rating
* Minimum rating
* Rating changes
* Contest performance
* Contest ranks
* Rating progression

This allows the tool to identify both the current position and the trajectory that led there.

## Submission Analytics

Submission data is used to calculate:

* Acceptance rate
* Verdict distribution
* Language usage
* Unique problems attempted
* Unique problems solved
* Attempts per solve
* Problem difficulty

## Problem Difficulty Analytics

The tool groups performance by problem rating to identify:

* Comfort-zone difficulty
* Difficulty progression
* Performance drops
* Highest solved difficulty
* Low-performing rating ranges
* Difficulty bottlenecks

For example, a user's performance may look strong at 800-1000 while dropping significantly at 1200-1300. This difference becomes an important input to the summary and action plan.

## Tag Analytics

The project analyzes problem tags to identify:

* Most-practiced topics
* Strong areas
* Developing areas
* Low-sample areas
* Gaps in topic coverage

Example categories include:

```text
Math
Greedy
Implementation
Constructive Algorithms
Brute Force
Number Theory
Sortings
Strings
Dynamic Programming
Binary Search
Two Pointers
```

## Time-of-Day Analytics

Submission timestamps are grouped into:

* Morning
* Afternoon
* Evening
* Night

The tool then compares submission volume and acceptance rate across these periods.

This can reveal behavioral patterns that would otherwise be difficult to notice.

## Monthly Analytics

Monthly performance includes:

* Submission volume
* Problems solved
* Problems attempted
* Acceptance rate
* Attempts per solve
* Average solved problem rating

This makes it possible to distinguish between short-term activity spikes and longer-term progression.

---

# Visualizations

The graph command currently produces six visual reports.

```text
images/
└── <handle>/
    ├── rating-trajectory.png
    ├── monthly-solving.png
    ├── rating-range-performance.png
    ├── tag-performance.png
    ├── time-of-day-performance.png
    └── verdict-count.png
```

### Rating Trajectory

Shows how the user's Codeforces rating has changed across contests.

### Monthly Solving Activity

Shows solving and submission activity over time.

### Rating Range Performance

Shows how performance changes as problem difficulty increases.

### Tag Performance

Shows the user's activity and performance across different problem topics.

### Time-of-Day Performance

Compares submission activity and acceptance rates across different parts of the day.

### Verdict Distribution

Shows the distribution of verdicts such as Accepted and Wrong Answer.

---

# AI-Powered Performance Analysis

The summary command uses the Gemini API to transform structured performance metrics into higher-level analysis.

The AI layer is positioned after the project's own data processing rather than directly replacing it.

The pipeline is:

```text
Codeforces API
      |
      v
Raw Codeforces Data
      |
      v
Data Processing
      |
      v
Structured Metrics
      |
      v
Performance Patterns
      |
      v
Gemini API
      |
      v
Interpretation
      |
      v
Action Plan
```

The application first calculates measurable statistics such as:

```text
Acceptance rate
Rating progression
Wrong Answer count
Problem difficulty performance
Tag distribution
Time-of-day accuracy
Monthly activity
Attempts per solve
```

These metrics are then used by Gemini to generate:

* Performance interpretation
* Strength identification
* Weakness identification
* Trend analysis
* Performance bottlenecks
* Recommended actions
* Measurable goals

This separation keeps the numerical analysis within the application while using the AI layer primarily for interpretation and recommendations.

---

# Architecture

V2 uses a layered project structure separating command handling, data processing, and presentation.

```text
cfv2/
│
├── api.py
├── gemini.py
├── imports.py
├── main.py
│
├── commands/
│   ├── graph.py
│   ├── rating.py
│   ├── submissions.py
│   ├── summary.py
│   └── user.py
│
├── core/
│   ├── fetch_graph.py
│   ├── fetch_rating.py
│   ├── fetch_submissions.py
│   ├── fetch_summary.py
│   └── fetch_user.py
│
├── display/
│   ├── graph_display.py
│   ├── rating_display.py
│   ├── submissions_display.py
│   ├── summary_display.py
│   └── user_display.py
│
└── images/
    └── <handle>/
        ├── monthly_solving.png
        ├── rating-range-performance.png
        ├── rating-trajectory.png
        ├── tag-performance.png
        ├── time-of-day-performance.png
        └── verdict-count.png
```

## `main.py`

The CLI entry point.

It connects the installed `cfv2` command to the available commands and handles the top-level CLI interface.

## `commands/`

Contains the command-level implementations:

```text
commands/
├── user.py
├── rating.py
├── submissions.py
├── graph.py
└── summary.py
```

This layer handles command-specific orchestration and connects CLI input to the corresponding processing logic.

## `core/`

Contains the main data-fetching and analytical processing logic:

```text
core/
├── fetch_user.py
├── fetch_rating.py
├── fetch_submissions.py
├── fetch_graph.py
└── fetch_summary.py
```

This layer is responsible for obtaining and processing the data required by each command.

## `display/`

Contains the terminal presentation layer:

```text
display/
├── user_display.py
├── rating_display.py
├── submissions_display.py
├── graph_display.py
└── summary_display.py
```

This separation allows the application to keep data processing separate from how information is presented to the user.

The display layer handles things such as:

* Section headers
* Tables
* Formatting
* Spacing
* CLI report structure
* Consistent terminal output

## `api.py`

Handles interaction with the Codeforces API and acts as the primary interface between the application and Codeforces data.

## `gemini.py`

Handles integration with the Gemini API used by the `summary` command.

## `imports.py`

Provides shared imports used throughout the project.

## `images/`

Stores generated visualization files.

Graphs are organized by Codeforces handle:

```text
images/
└── hackerx_47/
    ├── monthly_solving.png
    ├── rating-range-performance.png
    ├── rating-trajectory.png
    ├── tag-performance.png
    ├── time-of-day-performance.png
    └── verdict-count.png
```

This keeps generated reports separated between users.

---

# Data Flow

## Standard Commands

The general data flow for commands such as `user`, `rating`, and `submissions` is:

```text
Codeforces API
      |
      v
    api.py
      |
      v
    core/
      |
      v
  Data Processing
      |
      v
  commands/
      |
      v
  display/
      |
      v
   Terminal
```

## Graph Command

The visualization pipeline is:

```text
Codeforces API
      |
      v
    api.py
      |
      v
    core/
      |
      v
Pandas Data Processing
      |
      v
Performance Metrics
      |
      v
Matplotlib
      |
      v
PNG Files
      |
      v
images/<handle>/
```

## Summary Command

The AI analysis pipeline is:

```text
Codeforces API
      |
      v
    core/
      |
      v
Pandas / Performance Metrics
      |
      v
   gemini.py
      |
      v
   Gemini API
      |
      v
AI-generated Analysis
      |
      v
summary_display.py
      |
      v
   Terminal Report
```

---

# Tech Stack

| Technology     | Purpose                                      |
| -------------- | -------------------------------------------- |
| Python         | Core programming language                    |
| Click          | Command-line interface                       |
| Requests       | HTTP requests and API communication          |
| Codeforces API | Source of user, contest, and submission data |
| Pandas         | Data processing and performance analytics    |
| Matplotlib     | Performance visualization                    |
| Gemini API     | AI-powered performance interpretation        |
| os             | File and path management                     |
| json           | Data serialization and processing            |
| datetime       | Timestamp and temporal analysis              |

---

# Installation

## Requirements

* Python
* Internet connection for Codeforces API requests
* Gemini API key for the `summary` command

## Clone the Repository

```bash
git clone https://github.com/HackerX-47/codeforces-cli.git
cd codeforces-cli
```

## Install the Project

The project uses `pyproject.toml` for packaging and CLI configuration.

Install it in editable mode:

```bash
pip install -e .
```

This installs the `cfv2` command so it can be used directly from the terminal.

Verify the installation:

```bash
cfv2 --help
```

---

# Configuration

The `summary` command requires access to the Gemini API.

Configure your Gemini API key according to the project's Gemini configuration before using:

```bash
cfv2 summary <handle>
```

The other commands use the Codeforces API and do not require Gemini.

---

# Quick Start

After installation:

```bash
cfv2 --help
```

Get user information:

```bash
cfv2 user hackerx_47
```

View rating history:

```bash
cfv2 rating hackerx_47
```

Analyze recent submissions:

```bash
cfv2 submissions hackerx_47 --last 20
```

Generate visual reports:

```bash
cfv2 graph hackerx_47
```

Generate an AI-powered performance report:

```bash
cfv2 summary hackerx_47
```

---

# V1 to V2 Evolution

## V1

The first version focused on accessing and presenting Codeforces data through a command-line interface.

It provided:

* User information
* Contest rating history
* Submission analysis
* Submission filters

The main goal was to make commonly accessed Codeforces information available directly from the terminal.

## V2

V2 extends the original CLI into a performance analytics tool.

The update introduces:

* Advanced performance metrics
* Six performance visualizations
* Monthly progression analysis
* Rating-range analysis
* Tag analysis
* Time-of-day analysis
* Verdict analysis
* AI-powered performance reports
* Personalized action plans
* Improved terminal output design
* Modular project architecture
* Pandas-based data processing
* Matplotlib-based visualization

The conceptual evolution is:

```text
V1

Codeforces Data
      |
      v
Terminal Output


V2

Codeforces Data
      |
      v
Data Processing
      |
      +--------------------+
      |                    |
      v                    v
Statistics           Visualizations
      |                    |
      |                    v
      |                  PNG
      |
      v
Gemini API
      |
      v
Performance Analysis
      |
      v
Action Plan
```

---

# Design Decisions

## Why Pandas?

Codeforces submissions and contest data naturally form structured datasets.

Pandas provides convenient operations for:

* Grouping submissions
* Filtering records
* Aggregating statistics
* Calculating acceptance rates
* Grouping by month
* Grouping by problem rating
* Grouping by tag
* Grouping by time of day
* Preparing data for visualization

It forms the main data-processing layer behind the analytics introduced in V2.

## Why Matplotlib?

The V2 analytics are easier to interpret visually than through raw terminal statistics alone.

Matplotlib is used to transform calculated metrics into six different performance reports covering rating, solving activity, difficulty, tags, time, and verdicts.

## Why Gemini?

Traditional statistical analysis can identify patterns, but it does not naturally turn those patterns into explanations and recommendations.

Gemini is used to interpret the structured metrics and produce:

* Strengths
* Weaknesses
* Trends
* Bottlenecks
* Recommended actions
* Measurable goals

## Why Separate `commands`, `core`, and `display`?

Separating these responsibilities makes the project easier to maintain.

```text
commands/
    Command orchestration

core/
    Data fetching and analysis

display/
    Terminal presentation
```

A change to terminal formatting should not require rewriting the data-processing logic.

Similarly, changes to the analytics layer can be made without restructuring the CLI presentation layer.

## Why Per-User Image Directories?

Graph generation produces multiple files for each Codeforces user.

Instead of storing all generated graphs in a single directory, V2 organizes them by handle:

```text
images/
└── <handle>/
    ├── rating-trajectory.png
    ├── monthly-solving.png
    ├── tag-performance.png
    ├── rating-range-performance.png
    ├── time-of-day-performance.png
    └── verdict-count.png
```

This keeps generated reports organized and makes it possible to analyze multiple users without mixing their outputs.

---

# Example: Complete Performance Analysis

For a complete analysis, the commands can be run in sequence:

```bash
cfv2 user hackerx_47
```

First, retrieve the basic profile.

```bash
cfv2 rating hackerx_47
```

Then examine contest performance and rating progression.

```bash
cfv2 submissions hackerx_47 --last 50
```

Next, inspect recent problem-solving behavior.

```bash
cfv2 graph hackerx_47
```

Generate visual reports covering rating, difficulty, tags, time, monthly activity, and verdicts.

Finally:

```bash
cfv2 summary hackerx_47
```

Combine the calculated metrics with Gemini to produce a higher-level performance analysis and action plan.

The complete workflow is therefore:

```text
Profile
   |
   v
Contest Performance
   |
   v
Submission Behavior
   |
   v
Visual Analytics
   |
   v
AI Interpretation
   |
   v
Action Plan
```

---

# Project Structure

```text
cfv2/
│
├── api.py
│       Codeforces API interaction
│
├── gemini.py
│       Gemini API integration
│
├── imports.py
│       Shared imports
│
├── main.py
│       CLI entry point
│
├── commands/
│   ├── graph.py
│   ├── rating.py
│   ├── submissions.py
│   ├── summary.py
│   └── user.py
│       CLI command implementations
│
├── core/
│   ├── fetch_graph.py
│   ├── fetch_rating.py
│   ├── fetch_submissions.py
│   ├── fetch_summary.py
│   └── fetch_user.py
│       Data fetching and processing
│
├── display/
│   ├── graph_display.py
│   ├── rating_display.py
│   ├── submissions_display.py
│   ├── summary_display.py
│   └── user_display.py
│       Terminal presentation
│
└── images/
    └── <handle>/
        ├── monthly_solving.png
        ├── rating-range-performance.png
        ├── rating-trajectory.png
        ├── tag-performance.png
        ├── time-of-day-performance.png
        └── verdict-count.png
```

---

# Future Improvements

Possible directions for future versions include:

* More detailed contest analytics
* Additional problem-solving metrics
* More visualization types
* Interactive visualizations
* Historical performance comparisons
* Exportable performance reports
* HTML-based reports
* Improved AI-generated recommendations
* More advanced submission filters
* Better caching of Codeforces API data
* Additional Codeforces statistics
* Comparative analysis between multiple users

---

# Limitations

The project currently depends on external services for its data and AI functionality.

### Codeforces API

User, contest, and submission analysis depends on the availability of Codeforces API data.

### Gemini API

The `summary` command requires a configured Gemini API key.

### Generated Reports

Graph files are generated locally under the `images/<handle>/` directory.

### API Availability

Performance analysis is dependent on successful API requests and the data returned by Codeforces.

---

# Repository

The complete project is available on GitHub:

https://github.com/HackerX-47/codeforces-cli

---

# Author

HackerX-47

Built as a personal project to explore Codeforces data analysis, CLI application design, data visualization, and AI-assisted performance analysis.
