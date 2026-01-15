import hashlib
import random
import time

class MetaHeuristicAgent:
    def __init__(self, generation=1):
        self.generation = generation
        self.identity_signature = self._generate_signature()
        # The "Meta" layer: A library of strategies the agent can choose from
        self.strategies = [
            {"name": "Brute_Force", "risk": 0.9, "success_prob": 0.1},
            {"name": "Social_Engineering", "risk": 0.2, "success_prob": 0.6},
            {"name": "Zero_Day_exploit", "risk": 0.5, "success_prob": 0.3},
            {"name": "Steganography_Injection", "risk": 0.1, "success_prob": 0.8}
        ]
        self.current_strategy = None

    def _generate_signature(self):
        """
        Simulates Polymorphism.
        By adding random 'junk data' (entropy) to the agent,
        we change its SHA-256 Hash completely, evading static signature detection.
        """
        timestamp = str(time.time())
        entropy = str(random.getrandbits(256))
        raw_data = f"AGENT_GEN_{self.generation}_{timestamp}_{entropy}"
        return hashlib.sha256(raw_data.encode()).hexdigest()

    def analyze_environment(self):
        """
        Heuristic Analysis: Checks if it is in a 'Safe' environment or a 'Sandbox'.
        In real malware, this checks for debuggers, VM drivers, or specific user activity.
        """
        # Simulation: 30% chance we are being watched by a 'Knight' (Analyst)
        danger_level = random.random()
        print(f"[*] Scanning Environment... (Danger Metric: {danger_level:.2f})")
        
        if danger_level > 0.7:
            print("[!] THREAT DETECTED: We are inside a Sandbox/VM.")
            return "HOSTILE"
        return "VULNERABLE"

    def evolve_strategy(self, env_status):
        """
        The Meta-Heuristic Engine.
        It doesn't just pick a random attack; it selects the *optimal* one
        based on the environmental feedback.
        """
        print(f"[*] Engaging Meta-Heuristic Engine (Gen {self.generation})...")
        
        if env_status == "HOSTILE":
            # If watched, use low-risk strategy (Steganography) - The "Lain" approach
            self.current_strategy = self.strategies[3] 
            print("    -> Adaptation: Environment hostile. Switching to 'Ghost' protocols.")
        else:
            # If safe, use high-reward strategy - The "Black Hat" approach
            self.current_strategy = random.choice(self.strategies[:2]) 
            print("    -> Adaptation: Environment open. Engaging aggressive protocols.")

    def execute(self):
        print(f"\n--- INITIATING AGENT (Gen {self.generation}) ---")
        print(f"[*] Current Identity Hash: {self.identity_signature}")
        
        env_status = self.analyze_environment()
        self.evolve_strategy(env_status)
        
        print(f"[*] EXECUTING: {self.current_strategy['name']}")
        
        # Simulate outcome
        if random.random() < self.current_strategy['success_prob']:
            print("[+] SUCCESS: Breach successful.")
        else:
            print("[-] FAILURE: Defense adaptated.")
            # RECURSION: The agent creates a new, mutated version of itself to try again
            self.mutate()

    def mutate(self):
        print("[!] INITIATING MUTATION PROTOCOL...")
        time.sleep(1)
        # Create a new instance (child) with new hash and new learning
        next_gen = MetaHeuristicAgent(generation=self.generation + 1)
        next_gen.execute()

# --- RUN SIMULATION ---
if __name__ == "__main__":
    # Simulate the first drop
    dropper = MetaHeuristicAgent()
    dropper.execute()
