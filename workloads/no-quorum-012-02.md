# no-quorum-012-02

Reject acknowledgments when the leader cannot reach a majority.

Input scale: 12; deterministic random seed: 226.
Run `python scripts/demo.py --case workloads/no-quorum-012-02.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
