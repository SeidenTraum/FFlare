import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Crypt:
    def __init__(self, password:bytes, salt:bytes, iterations:int) -> None:
        self.password   = password
        self.salt       = salt
        self.iterations = iterations
        return None

    def derive_key(self) -> None:
        """ Uses PBKDF2HMAC to generate a key from Password
        **DO NOT CALL OUTSIDE OF CLASS**
        Instead initialize the class and call encrypt/decrypt, they will automatically call the derive_key class.
        """
        # Some basic checks
        if not self.password:
            print("Error, no password was given")
            raise TypeError("Password must be of type string, none was given")

        if not self.salt:
            print(f"Salt must not be empty, using random salt.")
            self.salt = os.urandom(16)
        if not self.iterations:
            self.iterations = 960_000

        if not isinstance(self.salt, bytes):
            raise TypeError(f"Salt must be of type bytes, given type was {type(self.salt)}!")
        if not isinstance(self.iterations, int):
            raise TypeError(f"Iterations must be of type integer, given type was {type(self.iterations)}!")
            
        if self.iterations <= 100_000:
            raise ValueError(f"Iterations should be equal or higher than 100_000, given value was {self.iterations}!")

        if not isinstance(self.password, bytes):
            if isinstance(self.password, str):
                self.password = self.password.encode()
            else:
                raise TypeError(f"Password is not of type byte, nor of type string, therefore could not be encoded. Use a valid password (string or bytes).")

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=self.iterations
        )
        print("Key derived successfully")

        self.password = base64.urlsafe_b64encode(kdf.derive(self.password))
        return None

    def encrypt(self, data:bytes):
        """ Encrypts the data using Fernet """
        f: Fernet

        if isinstance(data, str):
            print("Data must be of type bytes, encoding it")
            data = data.encode()

        # Deriving key automatically
        self.derive_key()

        f = Fernet(self.password)
        #TODO: ADD ERROR HANDLING
        return f.encrypt(data)

    def decrypt(self, data:bytes):
        f: Fernet

        if isinstance(data, str):
            print("Data must be of type bytes, encoding it")
            data = data.encode()

        self.derive_key()

        f = Fernet(self.password)
        return f.decrypt(data)
