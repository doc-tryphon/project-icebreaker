# Project Icebreaker — Roadmap

## Current Status: Phase 1 Complete ✅

---

## Phase 1 — Foundation (Complete)
**Goal:** Prove the core concept works.

- [x] `MetaHeuristicAgent` class architecture
- [x] Polymorphic SHA-256 signature generation
- [x] Environmental detection (hostile vs. vulnerable)
- [x] Strategy library with risk/reward values
- [x] Recursive mutation with generation tracking
- [x] Industry-standard project structure (`src/`, `tests/`)
- [x] 5 passing unit tests
- [x] Logging, type hints, recursion depth guard

---

## Phase 2 — Intelligence (Next Sprint)
**Goal:** Replace hardcoded strategy selection with learned behavior.

- [ ] Q-learning engine — agent learns optimal strategy per environment over time
- [ ] Epsilon-greedy exploration — balances trying new strategies vs. using known winners
- [ ] Execution telemetry — track decisions, outcomes, and Q-table evolution per run
- [ ] Expand test coverage to 70%+
- [ ] Inline docstrings on all methods

**Key dependency:** `numpy`

---

## Phase 3 — Advanced Behavior
**Goal:** Model the full adversarial co-evolution cycle.

- [ ] Adversarial simulation — defender adapts as attacker evolves, models red/blue team dynamics
- [ ] Metamorphic engine — mutate code structure between generations (instruction substitution, control flow randomization)
- [ ] Visualization tools — evolution trees, Q-table heatmaps, generation timelines
- [ ] Performance benchmarking suite

**Key dependencies:** `matplotlib`, `numpy`

---

## Phase 4 — Academic Deliverables
**Goal:** Formalize the research for WGU capstone defense.

- [ ] Academic paper (30–50 pages) — literature review, methodology, results, analysis
- [ ] Presentation deck with live demo
- [ ] Final validation and test suite
- [ ] Defense preparation

---

## Completion Estimate

| Phase | Status | Effort |
|-------|--------|--------|
| 1 — Foundation | ✅ Complete | 38 hrs |
| 2 — Intelligence | Pending | ~60 hrs |
| 3 — Advanced Behavior | Pending | ~80 hrs |
| 4 — Academic Deliverables | Pending | ~90 hrs |
| **Total** | **45%** | **~268 hrs** |

---

## Conceptual Origins
Inspired by the meta-heuristic ICE technology in *Cyberpunk 2077: Phantom Liberty* and the self-optimizing network agents in *Serial Experiments Lain*. Built as a practical extrapolation into real adversarial ML and malware behavior modeling.
