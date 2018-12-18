class Chatbot():
    def __init__(self, name, items):
        """Name is a given name for chatbot. Items are instances of Item()"""
        self.name = name
        self.items = items # things to ask
        self.told = {}
        
    def greet(self):
        return "Hello. My name is "+self.name+"."
        
    def process_input(self, noun_phrases):
        assert type(noun_phrases) == list 
        for i in self.items:
            for e in i.elements:
                if e.check_phrase(noun_phrases):
                    self.told[i.name] = e.name
                    if e.has_followup():
                        self.items.append(e.followup)
        
    def ask_question(self):
        to_ask = []
        for i in self.items:
            if i.name not in self.told:
                if i.question not in to_ask:
                    to_ask.append(i.question)
        if len(to_ask) == 0:
            return ''
        return to_ask.pop(0) 