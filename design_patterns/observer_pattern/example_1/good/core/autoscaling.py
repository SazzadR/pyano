from .observer import EC2Observer


class AutoScalingHandler(EC2Observer):
    def handle(self):
        self.scaleup()

    def scaleup(self):
        print("Scaling up EC2 instances...")
