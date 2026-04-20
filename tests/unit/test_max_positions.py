"""Bug 3 regression — StateController reads risk.max_open_positions."""

from scrooge_v3.core.state_controller import StateController


def test_state_controller_reads_nested_risk_config():
    sc = StateController(config={"risk": {"max_open_positions": 2}})
    assert sc.max_positions == 2


def test_state_controller_reads_flattened_config():
    """Current bootstrap passes config.section('risk') | section('runtime')
    merged into a flat dict — still must find max_open_positions."""
    sc = StateController(config={"max_open_positions": 3, "margin_utilization": 0.4})
    assert sc.max_positions == 3


def test_state_controller_default_is_2():
    sc = StateController(config={})
    assert sc.max_positions == 2


def test_state_controller_legacy_key_honored():
    sc = StateController(config={"max_concurrent_positions": 4})
    assert sc.max_positions == 4
