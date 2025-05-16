from pathlib import Path
import pandas as pd
from shiny import reactive
from shiny.express import input, ui

app_dir = Path(__file__).parent
ui.include_css(app_dir / "styles.css")

ui.page_opts(title="Movie Preference Survey")

with ui.layout_columns(col_widths=(6, 6)):
    with ui.card():
        ui.card_header("Demographics & Income")
        ui.input_text("name", "Your name")
        ui.input_select(
            "region",
            "Which part of the UK are you based in?",
            choices=["England", "Wales", "Scotland", "Northern Ireland"],
        )
        ui.input_numeric("age", "Your age", value=None)
        ui.input_numeric("income", "Your yearly income (£)", value=None)

    with ui.card():
        ui.card_header("Movie Ratings")
        ui.input_slider("anora", "'Anora'", min=1, max=5, value=None)
        ui.input_slider("brutalist", "'The Brutalist'", min=1, max=5, value=None)
        ui.input_slider("flow", "'Flow'", min=1, max=5, value=None)
        ui.input_slider("still_here", "'I'm Still Here'", min=1, max=5, value=None)
        ui.input_slider("substance", "'The Substance'", min=1, max=5, value=None)
        ui.input_text_area("feedback", "Any other feedback?", rows=4)

ui.div(
    ui.input_action_button("submit", "Submit", class_="btn btn-primary"),
    class_="d-flex justify-content-end mt-3"
)

@reactive.effect
@reactive.event(input.submit)
def save_to_csv():
    values = {
        "name": input.name(),
        "region": input.region(),
        "age": input.age(),
        "income": input.income(),
        "anora": input.anora(),
        "brutalist": input.brutalist(),
        "flow": input.flow(),
        "still_here": input.still_here(),
        "substance": input.substance(),
        "feedback": input.feedback(),
    }

    df = pd.DataFrame([values])
    csv_path = app_dir / "responses.csv"
    if not csv_path.exists():
        df.to_csv(csv_path, index=False)
    else:
        df.to_csv(csv_path, mode="a", index=False, header=False)

    ui.modal_show(ui.modal("Form submitted, thank you!"))
