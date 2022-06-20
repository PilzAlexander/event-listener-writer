from twitch_listener import listener
import argparse
import time
import numpy as np
import csv
from twitch_chat_irc import twitch_chat_irc


CHANNEL = 'MarineMammalRescue'
DRAGONRACE = "A dragon race is about to begin! If you have a Dragon Den dragon, and your dragon has what it takes, type !race NOW to join the race. You have 90 seconds to enter!"
HEIST = "Steven is preparing for a heist. You can boost his chances and join the heist by typing !heist within the next 90 seconds. Don't let him down!"
OTTERUP = "OtterUp"

connection = twitch_chat_irc.TwitchChatIRC(NICK, PASS)


def sendtochat(messages):
    print(messages)
    for key in messages.keys():
        if messages[key] == DRAGONRACE:
            messagetosend = "!race"
            connection.send(CHANNEL, messagetosend)
        elif messages[key] == HEIST:
            messagetosend = "!heist"
            connection.send(CHANNEL, messagetosend)
        elif messages[key] == OTTERUP:
            messagetosend = "LETSFREAKINGJOEY"
            connection.send(CHANNEL, messagetosend)


connection.listen(CHANNEL, on_message=sendtochat)

connection.close_connection()