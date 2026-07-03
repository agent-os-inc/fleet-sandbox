"""Seed module for the AgentOS fleet build sandbox.

The fleet clones this repo, a brief modifies it on its own branch, and opens a PR.
Safe to delete and recreate.
"""
import sys
sys.path.insert(0, '.')
from fleet_steer_probe import tag
assert tag() == 'v1'