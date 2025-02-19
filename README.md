# Key-Value Store with Raft Consensus

A deterministic single-host Raft reference that makes election, replication and partition safety directly inspectable.

This is newly generated educational reference code based on a concept in the supplied PDF.
It has **165 non-empty source, test, configuration, workload and documentation files**.
It is a prototype for study and extension, not evidence of previous deployment or measured large-scale performance.

## Quick start

Requires Python 3.10+; the default path uses the standard library.

```sh
python scripts/demo.py
python scripts/run_tests.py
python scripts/benchmark.py
python scripts/serve.py --port 8080
```

Open http://127.0.0.1:8080 for the workload dashboard. `scripts/demo.py --case workloads/<id>.case.json`
executes one workload and checks its independent acceptance conditions. `benchmark.py` prints actual local timings.

## Implemented scope

Vote freshness, persistent term/vote/log state, matching-prefix append RPCs, conflict truncation, current-term majority commits, committed state-machine application, crash/partition simulation and a joint-quorum predicate.

## Limits and optional runtimes

The transport is in-process and deterministic, not a high-concurrency Go/C++ service. There are no real election timers, gRPC server, snapshots, linearizable reads or complete membership-change protocol. The membership workload checks the joint quorum rule only; configuration entries and transition finalization are not implemented. Crash simulation toggles availability, while persistent node restart is checked separately.

All bundled data are synthetic. No credentials, pretrained model weights, historical commits, or fabricated benchmark results are included.
See `docs/PROVENANCE.md`, `docs/TESTING.md`, and the bundle's validation report for evidence and omissions.
