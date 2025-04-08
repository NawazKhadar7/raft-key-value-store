# Key-Value Store with Raft Consensus

A deterministic single-host Raft reference that makes election, replication and partition safety directly inspectable.

## 1. Overview

Replicated storage must preserve committed state when leaders change or network links fail. This deterministic single-host reference makes Raft voting and replication transitions inspectable without requiring a distributed cluster.

**Project type:** educational reference implementation. **Repository contents:** 165 non-empty source, test, configuration, workload and documentation files, including 36 synthetic workload scenarios.

## 2. Core Features — Why They Matter

- **Election safety:** Checks term and log freshness before granting votes.
- **Replication rules:** Implements matching-prefix append operations and conflicting-log truncation.
- **Commit and persistence:** Persists term, vote and log state, and applies committed entries to a key-value state machine.
- **Failure scenarios:** Exercises partitions, crashes and a joint-quorum predicate in reproducible workloads.

## 3. Tech Stack & Architecture

| Layer | Technology | Implementation status |
| --- | --- | --- |
| Execution | Python 3.10+ standard library | Deterministic single-host simulator |
| Transport and storage | In-process typed calls and local persistent node state | Runnable; no network cluster |
| Protocol design | Protocol Buffers schema | Design artifact; no live gRPC server |

### How the components fit together

A cluster simulator delivers typed method calls to Raft nodes. Each node maintains persistent term, vote and log state; majority replication allows committed entries to update its key-value state machine. Blocked links represent network partitions.

| Component | Responsibility |
| --- | --- |
| [src/syslab/raft_node.py](src/syslab/raft_node.py) | Voting, log replication and committed state-machine application. |
| [src/syslab/cluster.py](src/syslab/cluster.py) | Deterministic delivery and failure scenarios. |
| [src/syslab/storage.py](src/syslab/storage.py) | Persistent node state. |
| [src/syslab/membership.py](src/syslab/membership.py) | Joint-quorum predicate; not a complete membership protocol. |

See [Architecture](docs/ARCHITECTURE.md) and [Algorithms](docs/ALGORITHMS.md) for implementation notes.

### Scope and limitations

The transport is in-process and deterministic, not a high-concurrency Go/C++ service. There are no real election timers, gRPC server, snapshots, linearizable reads or complete membership-change protocol. The membership workload checks the joint quorum rule only; configuration entries and transition finalization are not implemented. Crash simulation toggles availability, while persistent node restart is checked separately.

## 4. Getting Started / Installation

**Prerequisites:** Python 3.10+. The default reference uses Python's standard library. No API keys or external services are needed for the default sample.

Download/extract this project or clone its repository, then open a terminal in the `raft-key-value-store` folder. Create an isolated environment:

```sh
python -m venv .venv
```

Activate it on Linux/macOS:

```sh
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the declared Python dependencies and run the demo:

```sh
python -m pip install -r requirements.txt
python scripts/demo.py
```

Check behavior and collect timings on your own machine:

```sh
python scripts/run_tests.py
python scripts/benchmark.py
```

The original bundle validation recorded **24 passing tests** for this project and **36 accepted workload scenarios**. These are local reference checks, not production or hardware benchmarks. See [Testing](docs/TESTING.md) and [Benchmark notes](docs/BENCHMARKS.md).

## 5. Usage Examples

### Run a reproducible workload

The bundled [sample request](examples/request.json) contains:

```json
{
  "family": "steady",
  "id": "steady-008-01",
  "seed": 101,
  "size": 8
}
```

Run the corresponding workload and check its independent acceptance conditions:

```sh
python scripts/demo.py --case workloads/steady-008-01.case.json
```

Expected `metrics` excerpt from the verified local run; the complete JSON also includes `output`:

```json
{
  "metrics": {
    "acknowledged": 8,
    "attempted": 8,
    "committed_keys": 8,
    "committed_prefix_safe": true,
    "joint_quorum_rule": true,
    "leader_term": 1,
    "rejected": 0
  }
}
```

The steady example acknowledges all eight writes and reports eight committed keys with safe committed prefixes. The default path uses in-process communication; it does not measure network-cluster throughput.

The complete example is in [examples/response.json](examples/response.json). Floating-point last digits can vary across numeric environments.

### Explore through the local dashboard

```sh
python scripts/serve.py --port 8080
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080), select a workload and choose **Run and check**. The server listens on loopback and is intended for local inspection.

With the server running, a second terminal can call its workload inspection API:

```sh
curl "http://127.0.0.1:8080/api/run?id=steady-008-01"
```

This endpoint executes the bundled workload; it is not a production domain API.

## 6. Your Contributions / Research Alignment

### Implementation evidence

The following work areas are present in this reference and can be reviewed directly:

| Work area in this reference | Repository evidence |
| --- | --- |
| Election safety | [src/syslab/raft_node.py](src/syslab/raft_node.py) |
| Correctness and edge cases | [tests/](tests/) and [acceptance workloads](workloads/) |
| Reproducible evaluation | [scripts/demo.py](scripts/demo.py), [scripts/benchmark.py](scripts/benchmark.py), [testing notes](docs/TESTING.md) |

### Research alignment

The project connects distributed algorithms, fault tolerance and persistence. Its strongest portfolio discussion concerns safety invariants, election rules and behavior under failed communication.

**A question to investigate:** Which failure schedules expose unsafe election or replication changes, and how can deterministic simulation check those invariants?

This question is a proposed extension, not a completed research result. Evaluate it with controlled inputs, independent correctness checks and measurements tied to a reproducible configuration.

### Personal contribution record

This reference was generated from the supplied project concept. Personal authorship or research contributions have not been verified. For an MS application, document only the modules you actually changed, the design choices you can explain, and experiments you ran; link those claims to commits or reproducible reports. See [Provenance](docs/PROVENANCE.md).

All bundled inputs are synthetic. The repository does not establish historical development dates, prior deployment or published research.
