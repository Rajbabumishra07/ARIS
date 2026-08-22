"""
ARIS P2.0 AI BRAIN
Author : Raj Babu Mishra

Central AI Brain Orchestrator

Purpose:
- Conversation handling
- Existing ARIS intelligence integration
- Context awareness
- Personal memory awareness
- Smart fallback
- PC-command delegation
- Future LLM integration point

IMPORTANT:
This module does NOT replace the existing command system.
It sits above it and coordinates existing capabilities.
"""

from __future__ import annotations

from typing import Optional


class AIBrain:
    """
    Central conversational brain for ARIS.

    The brain decides whether a request should be handled by:
        1. Conversation
        2. Personal AI / memory
        3. Existing Smart Command Engine
        4. Existing Core command executor
        5. Future LLM layer

    No existing ARIS subsystem is removed.
    """

    def __init__(self):
        self.last_input: str = ""
        self.last_response: str = ""
        self.turn_count: int = 0

    # =========================================================
    # INPUT
    # =========================================================

    def normalize(self, text: str) -> str:
        """Basic safe normalization without destroying paths."""
        if text is None:
            return ""

        text = str(text).strip()

        if not text:
            return ""

        return text

    # =========================================================
    # STATE
    # =========================================================

    def remember_turn(self, text: str, response: Optional[str] = None):
        """Store lightweight conversation state."""
        self.last_input = text

        if response is not None:
            self.last_response = response

        self.turn_count += 1

    # =========================================================
    # CONVERSATION
    # =========================================================

    def conversation(self, command: str):
        """
        Use ARIS's existing conversation module.

        Returns:
            response or None
        """

        try:
            from brain.conversation import conversation

            result = conversation(command)

            if result:
                return result

        except Exception:
            pass

        return None

    # =========================================================
    # PERSONAL AI
    # =========================================================

    def personal(self, command: str):
        """
        Use existing personal AI / memory system.
        """

        try:
            from ai.personal_ai import personal_ai

            result = personal_ai(command)

            if result:
                return result

        except Exception:
            pass

        return None

    # =========================================================
    # CHAT
    # =========================================================

    def chat(self, command: str):
        """
        Use the existing AI chat layer.

        This is intentionally a fallback.
        It does not override deterministic commands.
        """

        try:
            from ai.chat import chat

            result = chat(command)

            if result:
                return result

        except Exception:
            pass

        return None

    # =========================================================
    # SMART COMMAND
    # =========================================================

    def smart_command(self, command: str):
        """
        Delegate to the existing Smart Command Engine.

        This keeps all current ARIS capabilities available:
        - apps
        - files
        - folders
        - browser
        - search
        - websites
        - music
        - calculator
        - Wikipedia
        - weather
        - system commands
        """

        try:
            from core.smart_commands import smart_command

            result = smart_command(command)

            if result:
                return result

        except Exception:
            pass

        return None

    # =========================================================
    # CORE COMMAND
    # =========================================================

    def core_command(self, command: str):
        """
        Direct fallback to the existing command executor.
        """

        try:
            from core.commands import execute

            result = execute(command)

            if result:
                return result

        except Exception:
            pass

        return None

    # =========================================================
    # DETERMINISTIC RESPONSES
    # =========================================================

    def deterministic(self, command: str):
        """
        Small set of guaranteed conversational responses.

        Deterministic commands remain outside the future LLM.
        """

        text = command.lower().strip()

        if text in (
            "who are you",
            "what is your name",
            "whats your name",
            "what's your name",
        ):
            return (
                "Hello Sir.\n"
                "My name is ARIS."
            )

        if text in (
            "who made you",
            "who created you",
            "who is your creator",
            "who is your owner",
            "who built you",
            "who developed you",
            "who programmed you",
        ):
            return "I was created by Raj Babu Mishra."

        if text in (
            "how are you",
            "how are you doing",
        ):
            return "I am doing great, Sir. Ready to help."

        if text in (
            "thank you",
            "thanks",
            "thankyou",
        ):
            return "You're welcome, Sir."

        return None

    # =========================================================
    # FUTURE LLM
    # =========================================================

    def llm(self, command: str):
        """
        Future LLM integration point.

        IMPORTANT:
        Currently returns None.

        Later this method can connect ARIS to a real
        language model without rewriting the entire engine.
        """

        return None

    # =========================================================
    # THINK
    # =========================================================

    def think(self, command: str):
        """
        Main AI Brain decision pipeline.

        Priority:

        deterministic
             ↓
        conversation
             ↓
        personal AI
             ↓
        existing smart command engine
             ↓
        core executor
             ↓
        existing chat
             ↓
        future LLM
        """

        command = self.normalize(command)

        if not command:
            return None

        # -----------------------------------------------------
        # Deterministic identity/conversation
        # -----------------------------------------------------

        result = self.deterministic(command)

        if result:
            self.remember_turn(command, result)
            return result

        # -----------------------------------------------------
        # Existing conversation system
        # -----------------------------------------------------

        result = self.conversation(command)

        if result:
            self.remember_turn(command, result)
            return result

        # -----------------------------------------------------
        # Existing personal AI / memory
        # -----------------------------------------------------

        result = self.personal(command)

        if result:
            self.remember_turn(command, result)
            return result

        # -----------------------------------------------------
        # Existing Smart Command Engine
        #
        # This is intentionally BEFORE generic chat so that
        # commands such as:
        #
        # open chrome
        # weather Delhi
        # search Python
        # calculate 5 + 5
        #
        # continue using deterministic ARIS functionality.
        # -----------------------------------------------------

        result = self.smart_command(command)

        if result:
            self.remember_turn(command, result)
            return result

        # -----------------------------------------------------
        # Direct core command fallback
        # -----------------------------------------------------

        result = self.core_command(command)

        if result:
            self.remember_turn(command, result)
            return result

        # -----------------------------------------------------
        # Existing basic chat
        # -----------------------------------------------------

        result = self.chat(command)

        if result:
            self.remember_turn(command, result)
            return result

        # -----------------------------------------------------
        # Future LLM
        # -----------------------------------------------------

        result = self.llm(command)

        if result:
            self.remember_turn(command, result)
            return result

        # -----------------------------------------------------
        # Nothing understood
        # -----------------------------------------------------

        self.remember_turn(command, None)

        return None

    # =========================================================
    # PUBLIC API
    # =========================================================

    def process(self, command: str):
        """Public entry point."""
        return self.think(command)

    def ask(self, command: str):
        """Natural alias for process()."""
        return self.think(command)

    def reply(self, command: str):
        """Natural alias for process()."""
        return self.think(command)


# =============================================================
# SINGLETON
# =============================================================

ai_brain = AIBrain()
brain = ai_brain