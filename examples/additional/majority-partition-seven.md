# majority-partition-seven

Commit seven writes with a partitioned follower.

Healing must preserve the committed prefix.

Family: partition. Size: 7. Deterministic seed: 910706.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case majority-partition-seven
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| attempted | equals 7 |
| acknowledged | equals 7 |
| rejected | equals 0 |
| committed_keys | equals 7 |
| committed_prefix_safe | equals true |
| joint_quorum_rule | equals true |
| leader_term | min 1 |

Scope: Deterministic in-process cluster and joint-quorum predicate.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
