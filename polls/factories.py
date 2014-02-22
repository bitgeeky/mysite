from polls.models import *
import factory
import datetime

class PollFactory(factory.Factory):
    
    FACTORY_FOR = Poll

    question = "This is a temporary poll question"
    pub_date = timezone.now()

class ChoiceFactory(factory.Factory):

    FACTORY_FOR = Choice

    poll = factory.SubFactory(PollFactory)
    choice_text = "This is a temporary Choice for Poll"
    votes = 1
