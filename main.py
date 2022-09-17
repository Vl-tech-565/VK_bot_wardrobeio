import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from toks import main_token

vk_session = vk_api.VkApi(token=main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def sender(sent_id, text):
    """
    :param sent_id: 
    :type text: object
    """
    vk_session.method('messages.send', {'user_id': sent_id, 'message': text,
                                        'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id

        if msg == 'привет':
            sender(user_id, 'привет, мой друг')
