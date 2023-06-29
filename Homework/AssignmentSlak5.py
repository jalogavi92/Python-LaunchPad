import requests
import sys
import getopt


def send_slack_message(message):
    payload = '{Text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
                             data=payload)
    print(response.text)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hm:", ["message="])

    except getopt.GetoptError:
        print("SlackMessage.py -m <message>")
        sys.exit(2)

    if len(opts) == 0:
        message = "Hello, My name is Joan. Can you all comment with your name and where you are coming from."

    for opt, arg in opts:
        if opt == '-h':
            print("SlackMessage.py -m <message>")
            sys.exit()
        elif opt in ("-m", "--message"):  # Corrected the option name here
            message = arg

        send_slack_message(message)


if __name__ == "__main__":
    main(sys.argv[2:])
