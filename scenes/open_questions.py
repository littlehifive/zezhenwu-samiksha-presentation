"""
Simple Manim scene that animates the first few open questions pulled from
`context/open-questions.md`. Run with:
    manim -pql scenes/open_questions.py OpenQuestionsScene
"""
from __future__ import annotations

from pathlib import Path

from manim import DOWN, LEFT, RIGHT, UP, FadeIn, LaggedStart, Scene, Text, VGroup

CONTEXT_MD = (
    Path(__file__).resolve().parents[1] / "context" / "open-questions.md"
)


def first_bullets(limit: int = 4) -> list[str]:
    """Return the first `limit` bullet items from the markdown doc."""
    bullets: list[str] = []
    for line in CONTEXT_MD.read_text(encoding="utf-8").splitlines():
        if line.startswith("* "):
            bullets.append(line[2:].strip())
        if len(bullets) == limit:
            break
    return bullets


class OpenQuestionsScene(Scene):
    """Minimal scene that fades in the first few open questions."""

    def construct(self) -> None:
        title = Text("Open Questions", font_size=50, weight="BOLD").to_edge(UP)
        self.play(FadeIn(title, shift=UP))

        items = VGroup(
            *[
                Text(f"• {text}", font_size=28).align_to(title, LEFT)
                for text in first_bullets()
            ]
        ).arrange(
            DOWN, aligned_edge=LEFT, buff=0.5
        ).next_to(title, DOWN, buff=0.75)

        self.play(
            LaggedStart(*[FadeIn(item, shift=RIGHT) for item in items], lag_ratio=0.4)
        )
        self.wait(2)

