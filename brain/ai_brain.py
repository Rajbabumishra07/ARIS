"""
ARIS P2.1 CENTRAL AI BRAIN
Author : Raj Babu Mishra

Central orchestration layer for ARIS.

Design:
    Voice / Text
        ↓
    core.brain
        ↓
    AIBrain
        ├─ deterministic conversation
        ├─ personal memory
        ├─ existing Engine / command system
        ├─ existing chat fallback
        └─ future LLM provider

This layer does NOT replace ARIS's existing subsystems.
It coordinates them.
"""

from __future__ import annotations

from typing import Optional


_UNKNOWN_ENGINE_PREFIXES = (
    "Sir, I didn't understand that.",
    "सर, मैं आपकी बात पूरी तरह नहीं समझ पाया।",
)


class AIBrain:
    """Single central decision/orchestration layer for ARIS."""

    def __init__(self) -> None:
        self.last_input = ""
        self.last_response = ""
        self.turn_count = 0

    # =========================================================
    # NORMALIZATION / STATE
    # =========================================================

    def normalize(self, text: str) -> str:
        if text is None:
            return ""

        return str(text).strip()

    def remember_turn(
        self,
        command: str,
        response: Optional[str] = None
    ) -> None:

        self.last_input = command

        if response is not None:
            self.last_response = str(response)

        self.turn_count += 1

    def _save_conversation(
        self,
        command: str,
        response: Optional[str]
    ) -> None:

        """Best-effort persistent conversation history."""

        if not response:
            return

        try:

            from core.memory import memory

            memory.add_conversation(
                command,
                str(response)
            )

        except Exception:

            # Conversation persistence must never
            # break a command.
            pass

    # =========================================================
    # DETERMINISTIC CONVERSATION
    # =========================================================

    def deterministic(
        self,
        command: str
    ) -> Optional[str]:

        text = command.lower().strip()

        # -----------------------------------------------------
        # IDENTITY
        # -----------------------------------------------------

        if text in {
            "who are you",
            "what is your name",
            "whats your name",
            "what's your name",
        }:

            return (
                "Hello Sir.\n"
                "My name is ARIS."
            )

        # -----------------------------------------------------
        # CREATOR
        # -----------------------------------------------------

        if text in {
            "who made you",
            "who created you",
            "who is your creator",
            "who is your owner",
            "who built you",
            "who developed you",
            "who programmed you",
            "who is your maker",
        }:

            return (
                "I was created by "
                "Raj Babu Mishra."
            )

        # -----------------------------------------------------
        # GENERAL CONVERSATION
        # -----------------------------------------------------

        if text in {
            "how are you",
            "how are you doing",
        }:

            return (
                "I am doing great, Sir. "
                "Ready to help."
            )

        # -----------------------------------------------------
        # THANKS
        # -----------------------------------------------------

        if text in {
            "thank you",
            "thanks",
            "thankyou",
        }:

            return (
                "You're welcome, Sir."
            )

        return None

    # =========================================================
    # PERSONAL AI / MEMORY
    # =========================================================

    def personal(
        self,
        command: str
    ) -> Optional[str]:

        try:

            from ai.personal_ai import personal_ai

            return personal_ai(command)

        except Exception:

            return None

    # =========================================================
    # EXISTING CORE ENGINE
    # =========================================================

    def engine(
        self,
        command: str
    ) -> Optional[str]:

        """
        Delegate all established ARIS functionality
        to the existing deterministic Engine.

        Import is lazy to avoid startup cycles.
        """

        try:

            from core.engine import engine

            return engine.process(command)

        except Exception as error:

            print(
                f"⚠ AI Brain engine error: {error}"
            )

            return None

    # =========================================================
    # BASIC CHAT FALLBACK
    # =========================================================

    def chat(
        self,
        command: str
    ) -> Optional[str]:

        try:

            from ai.chat import chat

            return chat(command)

        except Exception:

            return None

    # =========================================================
    # FUTURE LLM PROVIDER
    # =========================================================

    def llm(
        self,
        command: str
    ) -> Optional[str]:

        """
        Reserved provider boundary.

        A real LLM can be connected here later without
        changing the voice listener, core engine,
        memory, or command router.
        """

        return None

    # =========================================================
    # ENGINE RESULT QUALITY
    # =========================================================

    def _is_generic_unknown(
        self,
        response: Optional[str]
    ) -> bool:

        if not response:
            return True

        value = str(response).strip()

        return any(
            value.startswith(prefix)
            for prefix in _UNKNOWN_ENGINE_PREFIXES
        )

    # =========================================================
    # THINK
    # =========================================================

    def think(
        self,
        command: str
    ) -> Optional[str]:

        command = self.normalize(command)

        if not command:
            return None

        # =====================================================
        # 1. GUARANTEED IDENTITY / BASIC CONVERSATION
        # =====================================================

        result = self.deterministic(command)

        if result:

            self.remember_turn(
                command,
                result
            )

            self._save_conversation(
                command,
                result
            )

            return result

        # =====================================================
        # 2. PERSONAL MEMORY / PROFILE
        # =====================================================

        result = self.personal(command)

        if result:

            self.remember_turn(
                command,
                result
            )

            self._save_conversation(
                command,
                result
            )

            return result

        # =====================================================
        # 3. EXISTING ARIS ENGINE
        #
        # IMPORTANT:
        #
        # Existing capabilities remain active:
        #
        # time
        # date
        # weather
        # search
        # open
        # close
        # files
        # folders
        # system
        # automation
        # etc.
        # =====================================================

        result = self.engine(command)

        if (
            result
            and not self._is_generic_unknown(result)
        ):

            self.remember_turn(
                command,
                result
            )

            self._save_conversation(
                command,
                result
            )

            return result

        # =====================================================
        # 4. EXISTING BASIC CHAT
        # =====================================================

        result = self.chat(command)

        if result:

            self.remember_turn(
                command,
                result
            )

            self._save_conversation(
                command,
                result
            )

            return result

        # =====================================================
        # 5. FUTURE LLM
        # =====================================================

        result = self.llm(command)

        if result:

            self.remember_turn(
                command,
                result
            )

            self._save_conversation(
                command,
                result
            )

            return result

        # =====================================================
        # NOTHING UNDERSTOOD
        # =====================================================

        self.remember_turn(
            command,
            None
        )

        return None

    # =========================================================
    # PUBLIC API
    # =========================================================

    def process(
        self,
        command: str
    ) -> Optional[str]:

        return self.think(command)

    def ask(
        self,
        command: str
    ) -> Optional[str]:

        return self.think(command)

    def reply(
        self,
        command: str
    ) -> Optional[str]:

        return self.think(command)


# =============================================================
# SINGLETON
# =============================================================

ai_brain = AIBrain()

brain = ai_brain