# Additional scenarios for raft-key-value-store

Ten runnable scenarios cover small inputs, odd sizes, and behavior boundaries in the existing reference implementation.

This directory contains 10 input JSON files, 10 metric-oracle JSON files, 10 scenario notes, this guide, and the runner (32 files).

Run from the project directory with Python 3.10 or later and the dependencies already listed in requirements.txt.

~~~powershell
python -B examples/additional/run_cases.py --list
python -B examples/additional/run_cases.py
python -B examples/additional/run_cases.py --case steady-single --json
~~~

The runner exits with zero only when all selected scenarios pass. --json includes metrics and output or a failure reason for each scenario.

Each .case.json is paired with a .expected.json containing equality checks or numeric bounds for the existing syslab.common.check helper.
Scenario notes explain the selected boundaries. Fixed seeds make inputs repeatable; expected files contain assertions rather than recorded timings.

| Scenario | Family | Size | Purpose |
| --- | --- | --- | --- |
| steady-single | steady | 1 | Commit one write with a healthy majority. |
| follower-down-single | follower-crash | 1 | Commit one write with an unavailable follower. |
| leader-down-single | leader-crash | 1 | Replace the leader before the only write. |
| leader-down-three | leader-crash | 3 | Replace the leader during three writes. |
| majority-partition-single | partition | 1 | Commit one write on the majority side. |
| majority-partition-seven | partition | 7 | Commit seven writes with a partitioned follower. |
| no-quorum-single | no-quorum | 1 | Attempt one write with an isolated leader. |
| no-quorum-seven | no-quorum | 7 | Attempt seven writes without quorum. |
| membership-three | membership | 3 | Check the joint-majority rule with three writes. |
| steady-seventeen | steady | 17 | Commit seventeen ordered writes. |

Scope: Deterministic in-process cluster and joint-quorum predicate.

Supplemental inputs have their own runner, so the existing workload discovery and its 36-case suite retain their current behavior.
Bytecode generation is disabled. Reports go to standard output; storage and model artifacts use the reference code's temporary directories.

See [limitations](../../docs/LIMITATIONS.md) and [running instructions](../../docs/RUNNING.md).
