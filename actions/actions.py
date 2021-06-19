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

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Tracker 
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
class PaintingFormValidation(FormValidationAction):
    """Example of a form validation action."""

    def name(self) -> Text:
        return "validate_painting_form"

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "model": [self.from_entity(entity='art_type', intent='art_type_entry')],
            "frame_size": [self.from_entity(entity='size', intent='size_entry')],
            "frame_type": [self.from_entity(entity='frame', intent='frame_entry')],
            "frame_finishing": [self.from_entity(entity='finishing', intent='finishing_entry')],
            "frame_orientation": [self.from_entity(entity='orientation', intent='orientation_entry')]
        }

    @staticmethod
    def art_type_db() -> List[Text]:
        """Database of supported cuisines."""

        return [
            "graphite",
            "charcoal",
            "sketching",
            "oilPainting",
            "colored pencil"
        ]

    @staticmethod
    def size_db() -> List[Text]:
        """Database of supported sizes"""

        return [
            "a1",
            "a2",
            "a3",
            "a4"
        ]

    @staticmethod
    def frame_db() -> List[Text]:
        """Database of supported frame types"""

        return [
            "no frame",
            "standard",
            "designer"
            ]

    @staticmethod
    def finishing_db() -> List[Text]:
        """Database of supported finishing"""

        return [
            "maple",
            "wood",
            "metal",
            "glass",
            "walnut"
        ]

    @staticmethod
    def orientation_db() -> List[Text]:
        """Database of supported orientations."""

        return [
            "landscape",
            "potrait",
            "designer choice"
            ]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_model(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate art type value."""

        if value.lower() in self.art_type_db():
            # validation succeeded, set the value of the "art_type" slot to value
            return {"model": value}
        else:
            dispatcher.utter_message(response="utter_wrong_art_type")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"model": None}

    def validate_frame_size(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate size value."""

        if value.lower() in self.size_db():
            # validation succeeded, set the value of the "size" slot to value
            return {"frame_size": value}
        else:
            dispatcher.utter_message(response="utter_wrong_size_type")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"frame_size": None}

    def validate_frame_type(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate frame type value."""

        if value.lower() in self.frame_db():
            # validation succeeded, set the value of the "frame" slot to value
            return {"frame_type": value}
        else:
            dispatcher.utter_message(response="utter_wrong_frame_type")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"frame_type": None}

    def validate_frame_finishing(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate finishing value."""

        if value.lower() in self.finishing_db():
            # validation succeeded, set the value of the "finishing" slot to value
            return {"frame_finishing": value}
        else:
            dispatcher.utter_message(response="utter_wrong_finishing_type")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"frame_finishing": None}

    def validate_orientation(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate orientation value."""

        if value.lower() in self.orientation_db():
            # validation succeeded, set the value of the "orientation" slot to value
            return {"frame_orientation": value}
        else:
            dispatcher.utter_message(response="utter_wrong_orientation_type")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"frame_orientation": None}

    def submit(
        self,
        dispatcher:CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
     ) -> List[Dict]:

        dispatcher.utter_message(template="utter_submit")
     
        return []

# Class function to validate the input from the user, print the results and store in response