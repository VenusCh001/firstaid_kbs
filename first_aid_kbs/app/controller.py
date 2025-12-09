
# app/controller.py
"""
Controller for the First-Aid Knowledge-Based System.

Responsibilities:
- Accept user input from routes
- Preprocess and normalize input text
- Forward query to the inference engine
- Return both result and explanation trace
"""

import re


class FirstAidController:
    def __init__(self, engine):
        self.engine = engine

    # --------------------------------------
    # Normalize user input (very important)
    # --------------------------------------
    def _clean_input(self, text: str):
        """
        Basic text normalization:
        - lowercase
        - remove extra spaces
        - keep alphabetic words only
        """

        text = text.lower()
        text = re.sub(r"[^a-z\s]", "", text)
        tokens = text.split()

        return tokens

    # --------------------------------------
    # Main entry point for UI queries
    # --------------------------------------
    def diagnose(self, user_text: str):
        """
        1. Clean + tokenize user text
        2. Send tokens to inference engine
        3. Receive:
            - final recommendation
            - explanation details
        4. Return a clean response to UI
        """

        tokens = self._clean_input(user_text)

        result, explanation = self.engine.run(tokens)

        response = {
            "input": user_text,
            "tokens": tokens,
            "recommendation": result,
            "explanation": explanation
        }

        return response
