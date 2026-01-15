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

## 🧠 Logic Flow
The following pseudocode demonstrates the decision-making engine behind the Icebreaker agent. It highlights the distinction between **Evasion Mode** (Sandbox detected) and **Execution Mode** (Target confirmed).

```python
if vm_or_sandbox_indicators():
    # --- EVASION PROTOCOL ---
    # Goal: Mimic benign behavior or go dormant to deceive the analyst.
    payload = select_from_low_risk_bucket()          # Steganography, LOLBAS (Living Off The Land)
    delay_behaviour(very_long_jittered)              # Sleep for 24h+ to outwait sandbox timeout
    use_heavy_obfuscation_on_strings_and_flow()      # Encrypt memory strings
else:
    # --- EXECUTION PROTOCOL ---
    # Goal: Maximum impact and propagation.
    payload = select_from_high_impact_bucket()       # Ransomware, Wiper, InfoStealer
    try_fast_lateral_movement()                      # Spread to other network nodes
    try_credential_dumping()                         # Steal Admin passwords (Mimikatz)
    try_ransomware_encryption()                      # Lock files

if failed_or_detected():
    # --- PERSISTENCE / CLEANUP ---
    drop_lightweight_implant_retry(hours=72)         # Try again later
    OR
    inject_into_legitimate_process_and_sleep()       # Hide inside 'explorer.exe'
    OR
    self_delete_and_leave_wmi_event()                # Go fileless (Registry only)
