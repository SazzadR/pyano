import random


class EC2Monitor(object):
    MAX_CPU_USAGE_PERCENTAGE = 80

    def __init__(self, autoscaling_handler, email_notifier):
        self.autoscaling_handler = autoscaling_handler
        self.email_notifier = email_notifier

    def monitor(self):
        current_cpu_usage = round(self.current_cpu_usage(), 2)
        if current_cpu_usage > self.MAX_CPU_USAGE_PERCENTAGE:
            self.autoscaling_handler.scaleup()
            self.email_notifier.send_email()
        else:
            print("System looks cool, current CPU usage is {}%".format(current_cpu_usage))

    def current_cpu_usage(self):
        return random.random() * 100
