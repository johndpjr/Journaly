import base64
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from constants import ITERATIONS, LENGTH, SALT


class Crypto:
    """Encrypts and decrypts journal content using
    Password-Based Key Derivation Function 2 (PBKDF2).
    """

    def __init__(self, password: str):
        self._kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=LENGTH,
            salt=SALT,
            iterations=ITERATIONS
        )
        self._key = base64.urlsafe_b64encode(
            self._kdf.derive(password.encode('utf-8'))
        )
        self._fernet = Fernet(self._key)
    
    def encrypt(self, content: str) -> bytes:
        """Returns the encrypted bytes of the content."""
        return self._fernet.encrypt(content.encode('utf-8'))

    def decrypt(self, token: bytes) -> str:
        """Returns the decrypted content string."""
        return self._fernet.decrypt(token).decode('utf-8')