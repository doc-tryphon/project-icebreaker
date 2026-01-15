# Project Icebreaker: Metaheuristic Agent Simulation (PoC)

## Overview
This repository contains a Python simulation of a **Metaheuristic Malware Agent**. It explores the theoretical concepts of "Automated Adaptation" and "Polymorphism" in offensive security.

The script models an agent that does not rely on static attack vectors. Instead, it uses a primitive **Genetic Algorithm** approach to:
1.  **Sense its Environment:** Detect if it is being observed (Sandbox/VM detection).
2.  **Mutate Identity:** Generate unique SHA-256 signatures for every instance (Polymorphism).
3.  **Evolve Strategy:** Dynamically switch between stealth (Steganography) and aggression (Brute Force) based on environmental feedback.

## Conceptual Origins
This project serves as a practical study of concepts found in:
* **Adversarial Machine Learning:** How AI agents adapt to defensive countermeasures.
* **Practical Malware Analysis:** The mechanics of signature evasion.
* **Cybernetic Theory:** The concept of "Icebreakers" or self-optimizing code in hostile networks (inspired by *Serial Experiments Lain* and *Cyberpunk 2077*).

## Disclaimer
**EDUCATIONAL USE ONLY.**
This code is a **simulation**. It contains no weaponized payloads, exploits, or harmful functions. It is a logic model designed to demonstrate how polymorphic engines make decisions.

## Usage
Run the simulation to observe the agent's generational evolution:
```bash
python3 icebreaker_agent.py

## Logic Flow

if vm_or_sandbox_indicators():
    payload = select_from_low_risk_bucket()          # stego, fileless, living-off-the-land, LOLBAS-only
    delay_behaviour(very_long_jittered)
    use_heavy_obfuscation_on_strings_and_flow()
else:
    payload = select_from_high_impact_bucket()       # ransomware, wiper, infostealer, RAT
    try_fast_lateral_movement()
    try_credential_dumping()
    try_ransomware_encryption()

if failed_or_detected():
    drop_lightweight_implant_that_will_try_again_in_3–72_hours
    OR
    inject_into_legitimate_process_and_sleep
    OR
    self-delete_and_leave_only scheduled task / WMI event
