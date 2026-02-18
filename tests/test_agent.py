"""
Tests for MetaHeuristicAgent.

Phase 1: Basic structural tests — confirms the agent initializes and
         returns valid outputs. Expand heavily in Phase 2.
"""

from icebreaker.agent import MetaHeuristicAgent


def test_agent_initializes():
    agent = MetaHeuristicAgent()
    assert agent.generation == 1
    assert agent.identity_signature is not None
    assert len(agent.strategies) == 4


def test_signature_is_unique():
    a = MetaHeuristicAgent()
    b = MetaHeuristicAgent()
    assert a.identity_signature != b.identity_signature


def test_analyze_environment_returns_valid_status():
    agent = MetaHeuristicAgent()
    result = agent.analyze_environment()
    assert result in ("HOSTILE", "VULNERABLE")


def test_generation_increments_on_mutate():
    agent = MetaHeuristicAgent(generation=1)
    child = MetaHeuristicAgent(generation=agent.generation + 1)
    assert child.generation == 2


def test_max_generation_guard():
    from icebreaker.agent import MAX_GENERATIONS
    agent = MetaHeuristicAgent(generation=MAX_GENERATIONS)
    # Should not raise — mutation halts at the limit
    agent.mutate()
