# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# Class function just to print the input provided the user

# from typing import Any, Text, Dict, List
# 
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction
# 
# class ActionHelloWorld(FormAction):
# 
#     def name(self) -> Text:
#         return "painting_form"
# 
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         print("required_slots(tracker: Tracker)")
#         return["art_type", "size", "frame", "finishing", "orientation"]
# 
#     def submit(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict]:
# 
#         dispatcher.utter_message(template="utter_submit")
# 
#         return []

# Class function to validate the input from the user and print the results
