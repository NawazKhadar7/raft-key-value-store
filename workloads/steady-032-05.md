# steady-032-05

Commit writes with all three voters available.

Input scale: 32; deterministic random seed: 105.
Run `python scripts/demo.py --case workloads/steady-032-05.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
