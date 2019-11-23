from .observer import EC2Observer


class EmailNotifier(EC2Observer):
    def handle(self):
        self.send_email()

    def send_email(self):
        print("Sending notification email to DevOps...")
