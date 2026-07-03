"""Seed module for the AgentOS fleet build sandbox.

The fleet clones this repo, a brief modifies it on its own branch, and opens a PR.
Safe to delete and recreate.
"""
import sys; sys.path.insert(0, '.'); from fleet_sandbox_strings import shout

def test_shout():
    assert shout('hi') == 'HI!'
    print('Test passed: shout("hi") returns', shout('hi'))

test_shout()
