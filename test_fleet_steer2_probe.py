import sys
sys.path.insert(0, '.');
from fleet_steer2_probe import tag

def test_tag():
    assert tag() == 'IMPOSSIBLE_SENTINEL_XYZ'