import bcrypt


def gerar_hash_senha(senha):

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def verificar_senha(senha, hash):
    return bcrypt.checkpw(senha.encode('utf-8'), hash.encode('utf-8'))
