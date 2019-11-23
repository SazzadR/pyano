from core import EC2Monitor, AutoScalingHandler, EmailNotifier

ec2 = EC2Monitor(autoscaling_handler=AutoScalingHandler(), email_notifier=EmailNotifier())
ec2.monitor()
