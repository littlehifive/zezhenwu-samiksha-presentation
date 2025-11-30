# zezhenwu-samiksha-presentation

## Manim demo quick start

1. Activate your virtual environment (Manim already installed per project notes).
2. Install repo-specific dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Render the sample scene, which pulls the first few bullet points from `context/open-questions.md`:
   ```
   manim -pql scenes/open_questions.py OpenQuestionsScene
   ```
   The movie is written to `media/videos/scenes/open_questions/` and should open automatically because of `-p`.

Adjust `scenes/open_questions.py` to experiment with different sections or visual treatments for the presentation. The Manim configuration lives in `manim.cfg`. 