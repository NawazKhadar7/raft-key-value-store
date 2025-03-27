# Design

Never acknowledge an entry before majority commit. Do not truncate committed prefixes. Keep volatile commit state separate from persistent term, vote and log; a restarted follower learns commit from its leader.
