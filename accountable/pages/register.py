import reflex as rx

from accountable.state import State


class RegisterState(State):
    username: str
    password: str

    def register(self) -> rx.event.EventSpec:
        return rx.redirect("/login")


def register() -> rx.Component:
    return rx.fragment(
        rx.center(
            rx.vstack(
                rx.heading("Sign Up", font_size="2em"),
                rx.input(on_change=RegisterState.set_username, placeholder="Username"),
                rx.input(
                    on_change=RegisterState.set_password,
                    placeholder="Password",
                    type_="password",
                ),
                rx.button("Sign Up", on_click=RegisterState.register),
                spacing="1em",
                font_size="2em",
                padding_top="10%",
                max_width="50%",
            )
        ),
    )
