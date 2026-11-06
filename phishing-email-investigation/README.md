# Phishing Email Investigation

**Project status: Completed**

## Objective and method
Parse a synthetic email, inspect reported authentication results, extract a URL, and compare sender and URL domains.

## Tools
Python 3, email, urllib.parse, re, terminal. GitHub and Markdown are used for portfolio documentation.

## Supporting demonstration
The accompanying script and output are recreated demonstrations of the project methodology, prepared with AI assistance. The recorded output is from the hosted verification run on 2026-11-06.

## Demonstration results
The demonstration identifies three reported authentication failures and a domain mismatch. Headers are synthetic; no independent DNS or reputation checks are performed.

## Run
Requires Python 3; no external packages or network access. The Linux permissions demonstration requires Linux or WSL.

```bash
python3 run.py
```

On Windows, use `python run.py` for the email and telemetry exercises.

## Files
- [run.py](run.py): procedure, test inputs, and verification assertions.
- [sample-output.txt](sample-output.txt): captured demonstration results.

## Completion checks for this demonstration
Execution exits with code 0 and prints PASS after its assertions succeed. These checks passed in the recorded run.

## Lessons
Validate inputs and expected results, record the reasoning behind decisions, and keep conclusions within the scope of the tested environment.
