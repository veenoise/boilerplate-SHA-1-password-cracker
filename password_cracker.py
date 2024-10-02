import hashlib

def crack_sha1_hash(hash, use_salts = False):
    with open("top-10000-passwords.txt") as passwords:
        lines_password = [line.strip() for line in passwords]

        if not use_salts:
            for i in lines_password:
                if hashlib.sha1(i.encode()).hexdigest() == hash:
                    return i
            
        else:
            with open("known-salts.txt") as salts:
                lines_salt = [line.strip() for line in salts]
                for i in lines_password:
                    for j in lines_salt:
                        if hashlib.sha1(f"{i}{j}".encode()).hexdigest() == hash:
                            return i
                        elif hashlib.sha1(f"{j}{i}".encode()).hexdigest() == hash:
                            return i

    return "PASSWORD NOT IN DATABASE"