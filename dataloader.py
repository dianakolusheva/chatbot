from element import Element
from item import Item
from chatbot import Chatbot

class DataLoader():
    def __init__(self):
        self.elems = {}
        self.items = {}

    def make_element(self,  name):
        self.elems[name] = Element(name)

    def make_item(self, name, element_names, question):
        elements =  [self.elems[n] for n in element_names]
        self.items[name] = Item(name, elements, question)

    def set_followups(self, elem_name, item_name):
        self.elems[elem_name].followup = self.items[item_name]

    def make_bot(self, name, item_names):
        return Chatbot(name, [self.items[n] for n in item_names])