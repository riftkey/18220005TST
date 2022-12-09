from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated='auto')

class Hash():
    def bcrypt(password: str): #sekadar mengingatkan pwd_cxt itu sebenarnya adalah CryptContext yang sudah di pass in parameter skema crypt yaitu bcrypt
        return pwd_cxt.hash(password) #jadi pwd_cxt ini mempunyai method hash yang mana method hash ini menerima sebuah parameter berupa string yang dalam kasus ini adalah string password
        
    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)

