import random
import os
import discord


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!help':
        return '`No one can help you now. Welcome to the Bone Army, Boneionairre!`'
    elif 'regis' in p_message:
        return '`YOU\'VE JUST BECOME A BONEIONAIRRE!!!`'
    else:
        pass


