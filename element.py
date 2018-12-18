class Element():
    def __init__(self, name, followup=None):
        self.name = name.lower()
        self.followup = followup
        
    def check_phrase(self, noun_phrases):
        for phrase in noun_phrases:
            if phrase.lower() == self.name:
                return True
        return False
    
    def has_followup(self):
        return self.followup is not None