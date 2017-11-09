from slackclient import SlackClient
import os


def run_bot(sc):
    """A text interface for my slackbot."""

    sent_message_count = 0
    while True:
        show_menu()
        action = raw_input("> ")

        if action == "1":
            print "\nThis is the latest message: "
            print sc.rtm_read()
            print "\n"

        elif action == "2":
            sent_message_count += 1
            message = "\nHi, this is the number I'm on: {}".format(sent_message_count)
            sc.rtm_send_message("general", message)

        else:
            print "The bot can't do that yet. Pick a number 1-2."


def show_menu():
    """Display options for the bot's CLI."""

    print "\nWhat do you want to do?"
    print "1: Get next message"
    print "2: Post a message"


if __name__ == "__main__":
    slack_token = os.environ.get("BOT_API_TOKEN")
    sc = SlackClient(slack_token)

    if sc.rtm_connect():
        run_bot(sc)
    else:
        print "Connection Failed"
