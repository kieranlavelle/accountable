
import reflex as rx

from accountable.state import State

class LandingState(State):

    def get_started(self) -> rx.event.EventSpec:
        return rx.redirect("/signup")

def index() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading("Welcome to Accountable!", font_size="2em"),
            rx.box("The home of self improvement"),
            rx.button("Get Started", on_click=LandingState.get_started),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )