from debate import run_agent_evaluation

def test_consensus_approval():
    safe_code = "def multiply(a, b): return a * b"
    summary = run_agent_evaluation(safe_code)
    assert summary.consensus_reached is True
    assert summary.final_score >= 7.5
    assert len(summary.remediation_actions) == 0

def test_consensus_rejection():
    vulnerable_code = "result = eval(payload)"
    summary = run_agent_evaluation(vulnerable_code)
    assert summary.consensus_reached is False
    assert "Fix security warnings" in summary.remediation_actions
