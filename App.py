# coding: utf-8
from __future__ import annotations
from abc import ABC, abstractmethod
from tkinter import * 

class Context:

    # The contained state.
    _state = None   # State attribute

    def __init__(self, state: State) -> None:
        self.setContext(state)

    def setContext(self, state: State):
        self._state = state
        self._state.context = self

    def push(self):
        self._state.handlePush()

    def pull(self):
        self._state.handlePull()

# The common state interface for all the states
class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handlePush(self) -> None:
        pass

    @abstractmethod
    def handlePull(self) -> None:
        pass

    @abstractmethod
    def getColor(self) -> str:
        pass

# The concrete states
class BlackState(State):
    # Next state for the Black state:
    # On a push(), go to "red"
    # On a pull(), go to "red"
    def handlePush(self) -> None:
        self.context.setContext(RedState())
    def handlePull(self) -> None:
        self.context.setContext(RedState())
    def getColor(self) -> str:
        return "black"

class BlueState(State):
    # Next state for the Black state:
    # On a push(), go to "green"
    # On a pull(), go to "black"
    def handlePush(self) -> None:
        self.context.setContext(GreenState())
    def handlePull(self) -> None:
        self.context.setContext(BlackState())
    def getColor(self) -> str:
        return "blue"

class GreenState(State):
    # Next state for the Black state:
    # On a push(), go to "black"
    # On a pullo, go to "blue"
    def handlePush(self) -> None:
        self.context.setContext(BlackState())
    def handlePull(self) -> None:
        self.context.setContext(BlueState())
    def getColor(self) -> str:
        return "green"

class RedState(State):
    # Next state for the Black state:
    # On a push(), go to "blue"
    # On a pull(), go to "green"
    def handlePush(self) -> None:
        self.context.setContext(BlueState())
    def handlePull(self) -> None:
        self.context.setContext(GreenState())
    def getColor(self) -> str:
        return "red"



if __name__ == "__main__":

    context = Context(RedState())

    fenetre = Tk()
    fenetre.title("Welcome to SUD-Cloud & IOT State Pattern")
    fenetre.geometry("450x250")
    fenetre.configure(background="white")

    def pushButton():
        context.push()
        monCadre.configure(background=context._state.getColor())

    def pullButton():
        context.pull()
        monCadre.configure(background=context._state.getColor())
   

    monCadre = Frame(fenetre, bg=context._state.getColor(), width=200, height=100,relief=GROOVE, border=4)
    monCadre.pack(pady=10, padx=10, fill=BOTH, expand='1')

    buton1 = Button(fenetre, text ='Push Operation', command=pushButton)
    buton1.pack(side=LEFT, padx=5, pady=5)
    
    buton2 = Button(fenetre, text ='Pull Operation', command=pullButton)
    buton2.pack(side=LEFT, padx=5, pady=5)

    Button(fenetre, text ='Exit', command=fenetre.quit).pack(side=LEFT, padx=5, pady=5)

    fenetre.mainloop()
