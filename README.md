# Protected merge acceptance fixture

This small, fictional program is a disposable test of GitHub's protected
merge workflow. It is not a production application or a released Linear skill.
It contains no customer data, credentials, private task history, or product code.

The command converts confirmed orders into delivery and pickup CSV files.
The independent command-level test checks the output files, excludes canceled
orders, and verifies that a changed input replaces the previous output.

Run locally:

```sh
python3 -m unittest discover -s tests -v
```

The proposed remote test is: require the `end-to-end` check on `main`, submit
a deliberately incorrect implementation on a branch, observe the failed check
and blocked merge, repair the implementation, then merge only the passing
candidate and read back `main`. Protection must also apply to administrators.
This repository contains only this fictional acceptance fixture.
