import streamlit as st

from abc import ABC, abstractmethod


class AbstractButton(ABC):

    def __init__(self, sidebar: bool = True):
        self.active = st.sidebar.button(self.name) if sidebar else st.button(self.name)

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError()

    @abstractmethod
    def action(self):
        raise NotImplementedError()
