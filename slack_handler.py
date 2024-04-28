import logging
from slack_sdk.web import WebClient
from slack_sdk.errors import SlackApiError


class SlackHandler(logging.Handler):

    def __init__(self, slack_channel, username, token, header):
        super().__init__()
        self.username = username
        self.slack_channel = slack_channel
        self.token = token
        self.header = header

    def emit(self, record):
        try:
            print("running emit..")
            message = self.format(record)
            self.post_to_slack(message, slack_channel=self.slack_channel, username=self.username, token=self.token, header=self.header)
        except Exception as e:
            print(f"Error occurred while sending message to Slack: {e}")

    @staticmethod
    def post_to_slack(message, slack_channel, username, token, header):

        client = WebClient(token=token)
        print('posting to slack')

        blocks = [{"type": "section", "text": {"type": "mrkdwn", "text": header}}]

        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": message}})
        blocks.append({"type": "divider"})

        try:
            print(blocks)
            # client.chat_postMessage(channel=slack_channel,
            #                         username=username,
            #                         blocks=blocks)
            print("Message sent successfully")
        except SlackApiError as e:
            print(f"Got an error: {e.response['error']}")
            print(f"Received a response status_code: {e.response.status_code}")