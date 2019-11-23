from core import EC2Monitor, AutoScalingHandler, EmailNotifier

ec2 = EC2Monitor()
ec2.attach(AutoScalingHandler())
ec2.attach(EmailNotifier())
ec2.monitor()
