# no-quorum-024-04

Reject acknowledgments when the leader cannot reach a majority.

Input scale: 24; deterministic random seed: 228.
Run `python scripts/demo.py --case workloads/no-quorum-024-04.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
