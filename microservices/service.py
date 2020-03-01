import yagmail
from nameko.rpc import rpc, RpcProxy


class Mail(object):
    name = "mail"

    @rpc
    def send(self, to, subject, contents):
        # yag = yagmail.SMTP("", "")
        yag = yagmail.SMTP("sazzad.rahman.bd@gmail.com", "sazzad.8891#kgmail~")
        yag.send(to=to.encode("utf-8"), subject=subject.encode("utf-8"), contents=[contents.encode("utf-8")])


class Compute(object):
    name = "compute"
    mail = RpcProxy("mail")

    @rpc
    def compute(self, operation, value1, value2, email):
        operations = {
            "sum": lambda x, y: int(x) + int(y),
            "sub": lambda x, y: int(x) - int(y),
            "mul": lambda x, y: int(x) * int(y),
            "div": lambda x, y: int(x) / int(y),
        }

        try:
            result = operations[operation](value1, value2)
        except Exception as e:
            print("An error occurred", str(e))
            self.mail.send.call_async(email, "An error occurred", str(e))
        else:
            print("Operation complete")
            return result
