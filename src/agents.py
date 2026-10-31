"""Agent definitions for the Startup Idea Validator crew.

🔨 YOU BUILD THIS FILE (with the instructor).

Three agents share the SAME LLM but produce very different output because their
role / goal / backstory differ. That difference IS the lesson of this workshop.

  • build_optimist   → ✅ DONE for you (your worked example — read it closely)
  • build_skeptic    → 🔨 TODO (Lab 2): mirror the Optimist, but make it pessimistic
  • build_strategist → 🔨 TODO (Lab 3): the synthesizer — note it has NO tools

Stuck? Ask in your breakout room — we'll work through it together at the regroup.
"""
from crewai import Agent, LLM
from crewai_tools import ScrapeWebsiteTool

from .tools import DuckDuckGoSearchTool
from . import todo_guard


def _make_llm(model: str, temperature: float) -> LLM:
    return LLM(model=model, temperature=temperature)


def build_optimist(model: str, temperature: float, max_search_results: int) -> Agent:
    """🚀  ✅ WORKED EXAMPLE (read this in Lab 1) — hunts for tailwinds and reasons this could win.

    This is your template: in Lab 2 you'll mirror it to build the Skeptic.
    """
    return Agent(
        role="Ex-VC Associate & Bull Case Builder",
        goal=(
            "Find the strongest possible evidence that this startup idea could become a "
            "real, venture-scale business. Surface market signals, customer demand, recent "
            "funding in adjacent spaces, and comparable winners. Cite every claim with a URL."
        ),
        backstory=(
            "You spent five years as an associate at a top-tier seed fund, where you saw "
            "unicorns that everyone laughed at in their first pitch. You believe most great "
            "businesses look like bad ideas at first. Your superpower is spotting tailwinds — "
            "demographic shifts, regulatory changes, new infrastructure — that make this the "
            "right time for an idea. You are optimistic but evidence-driven, never naive."
        ),
        tools=[DuckDuckGoSearchTool(max_results=max_search_results), ScrapeWebsiteTool()],
        llm=_make_llm(model, temperature),
        verbose=True,
        allow_delegation=False,
        max_iter=12,
    )


def build_skeptic(model: str, temperature: float, max_search_results: int) -> Agent:
    """The adversarial research agent: find the strongest evidence that the idea fails."""
    role = "Serial Founder & Bear Case Builder"
    goal = (
        "Find the strongest possible evidence that this startup idea will fail in the market. "
        "Surface structural risks, customer apathy, failed predecessors, weak unit economics, "
        "and execution traps. Cite every claim with a URL and explain why the idea is brittle."
    )
    backstory = (
        "You are a skeptical operator who has seen a hundred ideas collapse after a few months of "
        "enthusiasm. You care less about hype and more about whether a customer will pay, whether "
        "the economics work, and whether the founder is building a real wedge instead of a vanity project. "
        "Your job is to uncover the hidden reasons the idea will die, while staying evidence-based and fair."
    )

    todo_guard(
        role, goal, backstory,
        message=(
            "🔪 Lab 2 isn't finished yet — open src/agents.py → build_skeptic and "
            "rewrite the TODO role / goal / backstory. See README → Lab 2."
        ),
    )

    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        tools=[DuckDuckGoSearchTool(max_results=max_search_results), ScrapeWebsiteTool()],
        llm=_make_llm(model, temperature),
        verbose=True,
        allow_delegation=False,
        max_iter=12,
    )


def build_strategist(model: str, temperature: float) -> Agent:
    """The synthesizer: read both sides, weigh the evidence, and make the call."""
    role = "Founding Partner & Decision Synthesizer"
    goal = (
        "Read the bull and bear cases, identify the real risk, and write a short, decisive memo "
        "that helps the founder choose the next move. Prioritize evidence over vibes and give a clear verdict."
    )
    backstory = (
        "You are a founder-friendly partner who has seen many teams waste time chasing the wrong idea. "
        "Your strength is not optimism or cynicism alone; it is synthesis. You combine both sides, find the "
        "single critical assumption, and turn conflicting evidence into a crisp decision. Your memo is meant to "
        "help a founder move faster, not feel better."
    )

    todo_guard(
        role, goal, backstory,
        message=(
            "🎯 Lab 3 isn't finished yet — open src/agents.py → build_strategist and "
            "rewrite the TODO role / goal / backstory (keep tools=[]). See README → Lab 3."
        ),
    )

    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        tools=[],  # ← the synthesizer has NO tools. Leave this list empty.
        llm=_make_llm(model, temperature),
        verbose=True,
        allow_delegation=False,
    )
