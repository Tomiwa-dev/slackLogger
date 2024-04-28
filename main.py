import logging
from slack_handler import SlackHandler


class CustomLogger(logging.Logger):
    def __init__(self, name, slack_channel, username, token, level=logging.NOTSET):
        super().__init__(name, level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.slack_channel = slack_channel
        self.username = username
        self.token = token

        # Custom handler for Slack
        self.slack_handler = SlackHandler(slack_channel, username, token, header=self.name)
        self.slack_handler.setFormatter(formatter)
        self.addHandler(self.slack_handler)

    def error(self, message, *args, **kwargs):
        print("calling error..")
        super().error(message, *args, **kwargs)






