# Limitations

The transport is in-process and deterministic, not a high-concurrency Go/C++ service. There are no real election timers, gRPC server, snapshots, linearizable reads or complete membership-change protocol. The membership workload checks the joint quorum rule only; configuration entries and transition finalization are not implemented. Crash simulation toggles availability, while persistent node restart is checked separately.
