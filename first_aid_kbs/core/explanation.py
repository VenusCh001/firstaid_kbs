# core/explanation.py
"""
Explanation Facility for the First-Aid KBS.

Responsibilities:
- Track rules fired during inference
- Record reasoning steps
- Provide explanation for UI or logging
"""

class ExplanationGenerator:
    def __init__(self):
        self.trace = []

    def add_rule_fired(self, rule, matched_tokens):
        """
        Record a rule that was fired along with which tokens matched
        """
        explanation = f"Rule fired: IF {rule['if']} THEN {rule['then']} | matched tokens: {matched_tokens}"
        self.trace.append(explanation)

    def add_fact_inferred(self, fact):
        """
        Record an inferred fact
        """
        self.trace.append(f"Inferred fact: {fact}")

    def get_trace(self):
        """
        Return full explanation trace
        """
        return self.trace.copy()

    def clear(self):
        """
        Clear explanation trace before a new inference session
        """
        self.trace.clear()

