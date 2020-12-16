import bcrypt


def check_pw(entry: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(entry.encode('utf8'), hashed)


def generate_pw_hash(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf8'), salt)
