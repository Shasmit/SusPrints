class Config():
    SECRET_KEY = 'secret key'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/susprints"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    
    