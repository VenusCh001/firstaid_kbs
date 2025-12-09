
# core/knowledge_base.py
"""
Knowledge Base for the First-Aid KBS.

Responsibilities:
- Load rules from JSON file (industry-style)
- Provide methods to access rules for inference engine
"""

import json
from pathlib import Path


class KnowledgeBase:
    def __init__(self, rules_file: Path):
        """
        Load rules from JSON file
        """
        if not rules_file.exists():
            raise FileNotFoundError(f"Rules file not found: {rules_file}")

        with open(rules_file, "r", encoding="utf-8") as f:
            self.rules = json.load(f)

    # -----------------------------
    # Accessor Methods
    # -----------------------------
    def get_all_rules(self):
        """
        Returns all rules as a list
        """
        return self.rules

    def find_matching_rules(self, tokens: list):
        """
        Returns rules where at least one condition matches the tokens
        """
        matched_rules = []
        for rule in self.rules:
            if any(cond in tokens for cond in rule.get("if", [])):
                matched_rules.append(rule)
        return matched_rules
