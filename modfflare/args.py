import argparse

def parse_args() -> argparse.Namespace:
    args = argparse.ArgumentParser(
        prog="FFlare",
        description="Encrypt files under Fernet"
    )

    args.add_argument(
        'filepath',
        type=str,
    )

    args.add_argument(
        '-p', '--password',
        required=True,
        type=str,
        metavar="String",
    )

    args.add_argument(
        '-o', '--output',
        type=str,
        metavar="Path"
    )

    operation = args.add_mutually_exclusive_group(required=True)

    operation.add_argument(
        '-e', '--encrypt',
        action='store_true',
    )

    operation.add_argument(
        '-d', '--decrypt',
        action='store_true',
    )

    kdf = args.add_argument_group(description="Optional arguments related to the Key derivation function, do not change unless you know what you're doing")

    kdf.add_argument(
        '-ii', '--iterations',
        type=int,
        metavar="Number"
    )

    kdf.add_argument(
        '-ss', '--salt',
        metavar="Byte"
        # Type not declared because my LSP gives an error
        # Just remember to check it for the correct type
    )

    return args.parse_args()

