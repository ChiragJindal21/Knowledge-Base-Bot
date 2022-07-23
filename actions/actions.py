from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")

        # overwrite the representation function of the company object
        # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "company", lambda obj: obj["name"]
        )

        super().__init__(knowledge_base)
