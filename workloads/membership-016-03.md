# membership-016-03

Check both old and new majorities for a joint configuration.

Input scale: 16; deterministic random seed: 258.
Run `python scripts/demo.py --case workloads/membership-016-03.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
