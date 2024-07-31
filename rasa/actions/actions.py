# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
from rasa_sdk.events import SlotSet
import json

"""
class ActionControlLights(Action):
    def name(self) -> Text:
        return "action_control_lights"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        to_do = tracker.get_slot("to_do")
        room = tracker.get_slot("room")
        time = tracker.get_slot("time")

        output = {
            "what": "lights",
            "to_do": to_do,
            "when": time
        }

        # Save the output as a JSON file
        with open("output.json", "w") as f:
            json.dump(output, f)

        # Respond to the user
        response = f"Certainly! I'll {to_do} the lights in the {room} at {time}."
        dispatcher.utter_message(text=response)

        return []
"""
class ActionOnCommand(Action):
    def name(self) -> Text:
        return "action_make_sure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        action = tracker.get_slot("action")
        thing = tracker.get_slot("thing")
        place = tracker.get_slot("place")
        time = tracker.get_slot("time")
        amount = tracker.get_slot("amount")
        number = tracker.get_slot("number")

        if action is None or thing is None:
            response = f"sorry, i did not understand your request."
            dispatcher.utter_message(text=response)
            return []
        
        events = []

        if place is None:
            place = 'current room'
            events.append(SlotSet('place', place))
        if time is None:
            time = 'now'
            events.append(SlotSet('time', time))

        response = f"do you want to {action} the {thing} in {place} at {time}? "
        dispatcher.utter_message(text=response)

        return events

class ActionOnCommand(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [Restarted()]
    
class ActionOnCommand(Action):
    def name(self) -> Text:
        return "action_doing"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        action = tracker.get_slot("action")
        thing = tracker.get_slot("thing")
        place = tracker.get_slot("place")
        time = tracker.get_slot("time")
        amount = tracker.get_slot("amount")
        number = tracker.get_slot("number")

        if action is None or thing is None:
            response = f"sorry, i did not understand your request"
            dispatcher.utter_message(text=response)
        else:
            output = {
                "action": action,
                "thing": thing,
                "place": place, 
                "time": time,
                'amount': amount,
                'number': number
            }

            response = f"ok, doing your request!"
            dispatcher.utter_message(text=response, json_message=output)

        return [SlotSet('action', None), SlotSet('thing', None), SlotSet('place', None), SlotSet('time', None)]
