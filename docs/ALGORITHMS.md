# Algorithms

Raft election compares last term then log length. Followers accept AppendEntries only after a matching prefix. Leaders advance commit for entries in their current term with a majority. Reference: https://raft.github.io/raft.pdf .
