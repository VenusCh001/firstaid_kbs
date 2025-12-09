# app/__init__.py
"""
Application Factory for the First-Aid Knowledge-Based System (KBS).

This module:
- Creates the Flask app
- Loads the rule base from data/rules.json
- Initializes core components (KB, Graph, WorkingMemory, Engine)
- Injects them into the Controller
- Registers routes + templates
"""

from flask import Flask
from pathlib import Path

# Core system imports
from core.knowledge_base import KnowledgeBase
from core.graph import KnowledgeGraph
from core.working_memory import WorkingMemory
from core.engine import InferenceEngine
from core.explanation import ExplanationGenerator

# Controller
from app.controller import FirstAidController

# Routes
from app.routes import ui_blueprint


def create_app():
    # -----------------------------
    # Create Flask app
    # -----------------------------
    app = Flask(
        __name__,
        template_folder="templates"
    )

    # -----------------------------
    # Load rule base (JSON)
    # -----------------------------
    rules_path = Path("data/rules.json")
    kb = KnowledgeBase(rules_path)

    # -----------------------------
    # Initialize core components
    # -----------------------------
    graph = KnowledgeGraph()
    wm = WorkingMemory()
    explanation = ExplanationGenerator()
    engine = InferenceEngine(kb, graph, wm, explanation)

    # -----------------------------
    # Create Controller
    # -----------------------------
    controller = FirstAidController(engine)

    # Expose controller inside app context
    app.config["CONTROLLER"] = controller

    # -----------------------------
    # Register Routes (UI)
    # -----------------------------
    app.register_blueprint(ui_blueprint)

    return app
