import argparse

from pinglib import *
from pushover import Client

parser = argparse.ArgumentParser(
    description="A small command-line application to send customized "
                "push notifications for general use.")

parser.add_argument(
    '--message',
    help='The contents of the push notification.',
    required=False,
    default=current_time())
parser.add_argument(
    '--title',
    help='The contents of the push notification.',
    required=False,
    default=None)

args = parser.parse_args()

user_key = get_environment_variable('pingme.user_key')
pingme_api_token = get_environment_variable('pingme.api_token')

client = Client(user_key, api_token=pingme_api_token)
client.send_message(format_string(args.message),
                    title=format_string(args.title))
