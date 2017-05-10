from json import loads
from .chat import Chat
from .user import User
from .messageentity import MessageEntity

class Message:

    # TODO: добавить все поля в соответствии с https://core.telegram.org/bots/api#message
    user = None
    forward_from = None
    forward_from_chat = None
    forward_from_message_id = None
    forward_date = None
    reply_to_message = None
    edit_date = None
    text = None
    entities = []

    def __init__(self, data):

        if type(data) == str:
            data = loads(data)

        self.id = data['message_id']
        self.date = data['date']
        self.chat = Chat(data['chat'])

        if 'from' in data:
            self.user = User(data['from'])
        if 'forward_from' in data:
            self.forward_from = User(data['forward_from'])
        if 'forward_from_chat' in data:
            self.forward_from_chat = Chat(data['forward_from_chat'])
        if 'forward_from_message_id' in data:
            self.forward_from_message_id = data['forward_from_message_id']
        if 'forward_date' in data:
            self.forward_date = data['forward_date']
        if 'reply_to_message' in data:
            self.reply_to_message = Message(data['reply_to_message'])
        if 'edit_date' in data:
            self.edit_date = data['edit_date']
        if 'text' in data:
            self.text = data['text']
        if 'entities' in data:
            for entity in data['entities']:
                self.entities.append(MessageEntity(entity))
