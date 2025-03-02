# steady-seventeen

Commit seventeen ordered writes.

An odd-sized longer log preserves the full acknowledged prefix.

Family: steady. Size: 17. Deterministic seed: 910710.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case steady-seventeen
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| attempted | equals 17 |
| acknowledged | equals 17 |
| rejected | equals 0 |
| committed_keys | equals 17 |
| committed_prefix_safe | equals true |
| joint_quorum_rule | equals true |
| leader_term | min 1 |

Scope: Deterministic in-process cluster and joint-quorum predicate.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
