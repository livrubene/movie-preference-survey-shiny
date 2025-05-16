from shiny import ui

INPUTS = {
    "name": ui.input_text("name", "Your name"),
    "region": ui.input_select(
        "region",
        "Which part of the UK are you based in?",
        choices=["England", "Wales", "Scotland", "Northern Ireland"],
        selected=None,
    ),
    "age": ui.input_numeric("age", "Your age", value=None),
    "income": ui.input_numeric("income", "Your yearly income (£)", value=None),
    "anora": ui.input_slider("anora", "Anora", min=1, max=5, value=None),
    "brutalist": ui.input_slider("brutalist", "The Brutalist", min=1, max=5, value=None),
    "flow": ui.input_slider("flow", "Flow", min=1, max=5, value=None),
    "still_here": ui.input_slider("still_here", "I'm Still Here", min=1, max=5, value=None),
    "substance": ui.input_slider("substance", "The Substance", min=1, max=5, value=None),
    "feedback": ui.input_text_area("feedback", "Any other feedback?", rows=4),
}
