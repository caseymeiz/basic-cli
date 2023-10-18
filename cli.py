import argparse
from config import config


def main():
    commands = dict(
        hello=lambda: print(f'Hello {config.username}'),
        config=lambda: print(config)
    )
    parser = argparse.ArgumentParser()
    parser.add_argument('--command', choices=commands.keys(), required=True)
    parser.add_argument('--username')
    parser.add_argument('--email')

    args = parser.parse_args()

    config.username = args.username if args.username else config.username
    config.email = args.email if args.email else config.email

    commands.get(args.command)()


if __name__ == "__main__":
    main()
