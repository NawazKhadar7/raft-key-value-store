# membership-three

Check the joint-majority rule with three writes.

Both configurations must satisfy the joint-quorum predicate.

Family: membership. Size: 3. Deterministic seed: 910709.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case membership-three
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| attempted | equals 3 |
| acknowledged | equals 3 |
| rejected | equals 0 |
| committed_keys | equals 3 |
| committed_prefix_safe | equals true |
| joint_quorum_rule | equals true |
| leader_term | min 1 |

Scope: Deterministic in-process cluster and joint-quorum predicate.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
