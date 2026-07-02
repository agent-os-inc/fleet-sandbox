"""Seed module for the AgentOS fleet build sandbox.

The fleet clones this repo, a brief modifies it on its own branch, and opens a PR.
Safe to delete and recreate.
"""

def add(a, b):
    return a + b

# Add tests for the add function
assert add(2, 3) == 5