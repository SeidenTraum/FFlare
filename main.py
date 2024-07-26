from typing import List
import modfflare as flare
import base64

def main() -> None:
    file_data:bytes = b""
    lines:List[bytes]
    data:bytes = b""
    data_to_write:str = ""

    args = flare.parse_args()
    cryptography_object = flare.Crypt(
        password=args.password.encode(),
        salt=args.salt,
        iterations=args.iterations
    )

    with open(args.filepath, "rb") as file:
        file_data = file.read()
    if args.encrypt:
        data = cryptography_object.encrypt(file_data)
        data_to_write = f"{data.decode()}\n{base64.urlsafe_b64encode(cryptography_object.salt).decode()}" 
    elif args.decrypt:
        # Splitting file
        lines = file_data.splitlines()
        cryptography_object.salt = base64.urlsafe_b64decode(lines[1])
        data = cryptography_object.decrypt(file_data)
        data_to_write = data.decode()

    output = args.output or f"{args.filepath}.spx{'.enc' if args.encrypt else '.dec'}"

    with open(output, "w") as file:
        file.write(data_to_write)

    return None

if __name__ == "__main__":
    main()
