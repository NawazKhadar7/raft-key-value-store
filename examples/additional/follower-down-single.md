# follower-down-single

Commit one write with an unavailable follower.

The two remaining nodes form a majority.

Family: follower-crash. Size: 1. Deterministic seed: 910702.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case follower-down-single
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
