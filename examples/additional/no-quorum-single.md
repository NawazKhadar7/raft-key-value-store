# no-quorum-single

Attempt one write with an isolated leader.

No write may be acknowledged or committed without a majority.

Family: no-quorum. Size: 1. Deterministic seed: 910707.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case no-quorum-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| attempted | equals 1 |
| acknowledged | equals 0 |
| rejected | equals 1 |
| committed_keys | equals 0 |
| committed_prefix_safe | equals true |
| joint_quorum_rule | equals true |
| leader_term | min 1 |

Scope: Deterministic in-process cluster and joint-quorum predicate.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
