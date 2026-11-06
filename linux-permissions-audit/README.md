# Linux Permissions Audit

**Project status: Completed**

## Objective and method
Detect excessive access on a disposable file, change permissions from 666 to 640, and validate the result.

## Tools
Linux, Python 3, os, stat, pathlib, terminal. GitHub and Markdown are used for portfolio documentation.

## Supporting demonstration
The accompanying script and sample output demonstrate the project
methodology using controlled lab inputs.

## Demonstration results
The demonstration verifies a world-writable test file is detected and corrected. It does not audit the entire host.

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
Execution exits with code 0 and prints PASS after its assertions succeed. All verification assertions passed in the supporting demonstration.

## Lessons
Validate inputs and expected results, record the reasoning behind decisions, and keep conclusions within the scope of the tested environment.
