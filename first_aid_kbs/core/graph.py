# core/graph.py
"""
Knowledge Graph for the First-Aid KBS.

Responsibilities:
- Represent relationships between symptoms, injuries, and categories
- Provide methods to find related nodes (useful for inference engine)
"""

import networkx as nx


class KnowledgeGraph:
    def __init__(self):
        # Directed graph: nodes = symptoms/injuries, edges = relationships
        self.graph = nx.DiGraph()
        self._build_graph()

    def _build_graph(self):
        """
        Initialize graph with domain knowledge
        """
        edges = [
            ("bleeding", "first_aid"),
            ("cut", "bleeding"),
            ("burn", "first_aid"),
            ("sprain", "injury"),
            ("injury", "first_aid"),
            ("choking", "emergency"),
            ("emergency", "first_aid"),
            ("nosebleed", "bleeding")
        ]
        self.graph.add_edges_from(edges)

    # -----------------------------
    # Public API
    # -----------------------------
    def get_related_nodes(self, token: str):
        """
        Return all nodes directly connected to this token
        (successors + predecessors)
        """
        if token not in self.graph:
            return []
        successors = list(self.graph.successors(token))
        predecessors = list(self.graph.predecessors(token))
        return successors + predecessors

    def has_node(self, token: str):
        return token in self.graph

