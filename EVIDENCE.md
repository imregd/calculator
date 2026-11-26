# Coursework evidence

Use these headings to organise your own results and explanations. Replace
bracketed prompts and remove unused prompts. Supplied headings are permitted
reuse; the evidence and explanation must be your own. Refer to short saved
logs rather than pasting entire CI logs.

Staff will not open your private GitHub repository. Save PR pages and CI
runs as PDFs or screenshots, with short log excerpts, in `evidence/` and
give their paths below alongside the URLs.

Complete and commit this file with your other documentation before the final
release checks. Record the final release hash, CI run and fresh-checkout outcome
in the separately submitted `SUBMISSION.txt`, outside the repository, and
submit the final CI run as a separate PDF or screenshot.

## 1. Starting point and Git review

- Starting commit: 6e81effd9dafd47e23fb060f6e6e9a61fb790c82
- Reused lab files, tests and examples: calculator.py, test_calculator.py, check.sh, run.sh
- Feature branch and PR: devops-coursework, https://github.com/imregd/calculator/pull/3, "evidence\save_feature_branch_pr.png"
- Self-review: I reviewed the diff (files changed) and ensured the yaml file was correct, the tests covered valid and invalid test cases and that the functions matched what the brief requests. I did notice a file called -f that contained random git information, so I deleted it as it was not needed. After reviewing the diff I proceeded to merge the pull request into the main branch

## 2. Test failure, diagnosis and fix

Plan this before fixing the chosen missing requirement or defect. An initially
missing feature is acceptable; retain the test in the final suite.

- Requirement and retained test: [R number, test file/function]
- Expected result and actual failure: [your explanation]
- Before/fix commits: [hashes]
- Failing/passing local runs: [commands, outcomes and saved log paths]
- Failing/passing CI runs: [URLs, matching commit hashes and saved files in evidence/]
- CI diagnosis: [event, runner, job, failed step and useful log message]
- Cause and implementation fix: [explain what changed and why]

## 3. Repeatable checks and local hook

- Common check script: [path and invocation used locally and in CI]
- Prerequisites and hook installation: [commands or README reference]
- Blocked commit attempt: [short transcript, base commit and working-tree state]
- Permitted commit after the fix: [short transcript and resulting hash]
- Hook limitations and independent CI checks: [your explanation]

The hook may use the same failure case as section 2 or another case. A blocked
commit attempt has no new commit hash; identify its base commit and changes.

## 4. Native and container batch runs
 
- Native normal/mixed runs: I ran python3 batch_runner.py data/normal.csv results.csv on a Ubuntu Linux machine, giving 	6 succeeded, 0 failed, I then ran python3 batch_runner.py data/mixed.csv mixed-results.csv  which gave 8 records processed, 4 succeeded and 4 failed (DIVISION_BY_ZERO, UNKNOWN_OPERATION and two INVALID_NUMBER)
- Container build/run commands and image tag: [README reference or commands]
- Input/output transfer: [how files enter and leave the container]
- Mixed-run interpretation: [summary, one error and later successful records]
- Python version and Docker environment: [what you used]

## 5. Container checks in CI during development

- Checked-out source commit and CI run: [hash, URL and saved file in evidence/]
- Test gate, image build and smoke-test outcomes: [steps and results]
- Smoke fixture and expected-output check: [paths and what is asserted]
- Failure handling: [why failed tests stop the build and wrong output fails CI]

## 6. Reproduction notes

- Checkout tested during development: [commit]
- Documented setup and commands tried: [README reference]
- Outcome and any limitations: [your results]

The final fresh checkout must test the declared release commit. Record its
outcome in `SUBMISSION.txt` after the documentation is committed, CI passes
and the final commit is tagged. Do not create another commit just to insert
that commit's own hash or CI-run URL into this file.
