
# core/working_memory.py
"""
Working Memory for the First-Aid KBS.

Responsibilities:
- Store temporary facts during inference
- Track inferred facts to avoid repeated reasoning
- Provide methods to add, check, and clear facts
"""

class WorkingMemory:
    def __init__(self):
        self.facts = set()

    def add_fact(self, fact: str):
        """
        Add a new fact to working memory
        """
        self.facts.add(fact)

    def has_fact(self, fact: str) -> bool:
        """
        Check if a fact is already in working memory
        """
        return fact in self.facts

    def get_all_facts(self):
        """
        Return a list of all current facts
        """
        return list(self.facts)

    def clear(self):
        """
        Clear working memory for a new inference session
        """
        self.facts.clear()
