# majority-partition-single

Commit one write on the majority side.

The isolated minority cannot prevent the commit.

Family: partition. Size: 1. Deterministic seed: 910705.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case majority-partition-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| attempted | equals 1 |
| acknowledged | equals 1 |
| rejected | equals 0 |
| committed_keys | equals 1 |
| committed_prefix_safe | equals true |
| joint_quorum_rule | equals true |
| leader_term | min 1 |

Scope: Deterministic in-process cluster and joint-quorum predicate.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
