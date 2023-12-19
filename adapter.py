
class MailList:
    mails : list = []

    def add_mail(self, mail):
        self.mails.append(mail)
        return True
    def remove_last(self, mail):
        try:    
            self.mails.pop()
        except Exception as e:
            print("Log: {str(e)}")
            return False
        return True
    
    def send_all(self, mail):
        for mail in mails:
            mail.send()


class Mail:
    
    def send(self):
        return ""

class SomeOtherMail():

    def some_other_send():
        return "Some other send"
    
class MailAdapter():

    def __init__(self, other_mail):
        self.adaptee = other_mail

    def send(self):
        return self.adaptee.send()