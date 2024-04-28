# Custom Logger with Slack Integration

This Python program demonstrates a custom logger implementation with Slack integration. It allows you to log messages to both the console and a Slack channel simultaneously.

## Features

- CustomLogger class extends Python's logging.Logger class to provide additional functionality.
- SlackHandler class extends Python's logging.Handler class to send log messages to a Slack channel.
- Integration with Slack API to post log messages to a specified Slack channel.
- Allows customization of Slack message formatting and log levels.

## Requirements

- Python 3.x
- `slack_handler.py` file containing the SlackHandler class and any additional utility functions.

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed on your system.
3. Copy the `slack_handler.py` file into your project directory.

## Usage

1. Import the CustomLogger class into your Python script:

    ```python
    from custom_logger import CustomLogger
    ```

2. Create an instance of CustomLogger with desired configuration:

    ```python
    logger = CustomLogger(name='my_logger', level=logging.DEBUG, slack_channel='your_slack_channel', username='your_username', header='your_header', token='your_slack_token')
    ```

3. Use the logger to log messages:

    ```python
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    ```

4. Log messages will be displayed on the console and sent to the specified Slack channel.

## Configuration

- `name`: Name of the logger.
- `level`: Log level (e.g., logging.DEBUG, logging.INFO, etc.).
- `slack_channel`: Slack channel to which log messages will be sent.
- `username`: Username to display in Slack messages.
- `header`: Header to prepend to Slack messages.
- `token`: Slack API token for authentication.

## Customization

You can customize the log message format, Slack message format, and other aspects by modifying the `Formatter` classes in the `CustomLogger` and `SlackHandler` classes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

