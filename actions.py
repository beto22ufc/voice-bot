# # drop this comment
# # This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionGetElement(Action):

    def name(self):
        return "action_get_element"

        def run(self, dispatcher, tracker, domain):
            element = tracker.get_slot('element')
            pint(element)
            return []

