from app.abstract_classes.abstract_button import AbstractButton

import streamlit as st


class ContentManager:
    def __init__(self, button_classes: set, default_button_class: 'AbstractButton'):
        self._button_classes = button_classes
        self._default_button_class = default_button_class

        self._button_validation()

        self._display_navigation()
        self._display_content()

    @property
    def _active_button(self) -> AbstractButton:
        active_buttons = [button for button in self._buttons if button.active]
        return active_buttons[0] if active_buttons else self._default_button

    def _button_validation(self):
        for button in self._button_classes:
            if not issubclass(button, AbstractButton):
                raise TypeError("ContentManager only accepts buttons")

        if self._default_button_class not in self._button_classes:
            raise ValueError("The specified default button must be one of the passed buttons")

    def _instantiate_buttons(self):
        self._buttons = list()
        for ButtonClass in self._button_classes:
            button = ButtonClass()
            self._buttons.append(button)

            if ButtonClass == self._default_button_class:
                self._default_button = button

    def _display_navigation(self):
        st.sidebar.markdown("## Navigation")
        self._instantiate_buttons()

    def _display_content(self):
        self._active_button.action()
