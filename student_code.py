import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        'if fact is a Fact'
        if isinstance(fact, Fact):
            checker = False
            for fact1 in self.facts:
                if fact == fact1:
                    checker = True
                else:
                    pass
            if checker == False:
                'append to list' 
                self.facts.append(fact)
            else:
                pass
        else:
            pass   
        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        lob = ListOfBindings()
        for fact1 in self.facts:
            state1 = fact1.statement
            state2 = fact.statement
            checker = match(state1, state2)
            if checker != False:
                lob.add_bindings(checker)
            else:
                pass
        if len(lob) == 0:
            return False
        else:
            return lob
        print("Asking {!r}".format(fact))
