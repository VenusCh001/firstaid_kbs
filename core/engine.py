# core/engine.py
"""
Forward-Chaining Inference Engine for the First-Aid KBS.

Responsibilities:
- Reason over rules and knowledge graph
- Maintain working memory
- Generate explanation trace
- Return final recommendation
"""

class InferenceEngine:
    def __init__(self, kb, graph, working_memory, explanation_generator):
        self.kb = kb
        self.graph = graph
        self.wm = working_memory
        self.explainer = explanation_generator

    def run(self, tokens):
        """
        Main inference method.
        Input: list of cleaned tokens from user
        Output: recommendation string, explanation trace list
        """
        # Clear previous session
        self.wm.clear()
        self.explainer.clear()

        recommendations = []

        # -------------------------
        # 1. Rule-based reasoning
        # -------------------------
        matched_rules = self.kb.find_matching_rules(tokens)
        for rule in matched_rules:
            # Check if action already applied
            if not self.wm.has_fact(rule['then']):
                self.wm.add_fact(rule['then'])
                self.explainer.add_rule_fired(rule, tokens)
                recommendations.append(rule['then'])

        # -------------------------
        # 2. Graph-based reasoning
        # -------------------------
        for token in tokens:
            related_nodes = self.graph.get_related_nodes(token)
            for node in related_nodes:
                if node not in tokens and not self.wm.has_fact(node):
                    self.wm.add_fact(node)
                    self.explainer.add_fact_inferred(node)

        # -------------------------
        # 3. Compose final recommendation
        # -------------------------
        if recommendations:
            final_recommendation = " | ".join(recommendations)
        else:
            final_recommendation = "No direct rule matched. Please consult a medical professional."

        explanation_trace = self.explainer.get_trace()

        return final_recommendation, explanation_trace
