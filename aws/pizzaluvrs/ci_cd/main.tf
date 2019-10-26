provider "aws" {
    version = "~> 2.0"
    region = "us-west-2"
}

module "vpc" {
    source = "./modules/vpc"
    vpc_id = module.vpc.vpc_id
    public_subnet_2a_id = module.vpc.public_subnet_2a_id
    public_subnet_2b_id = module.vpc.public_subnet_2b_id
    private_subnet_2a_id = module.vpc.private_subnet_2a_id
    private_subnet_2b_id = module.vpc.private_subnet_2b_id
}

data "aws_ami" "ubuntu" {
    most_recent = true

    filter {
        name = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-*"]
    }

    owners = ["099720109477"]
}

// Jenkins

resource "aws_security_group" "pizzaluvrs-ec2-jenkins-sg" {
    vpc_id = module.vpc.vpc_id
    name = "pizzaluvrs-ec2-jenkins-sg"
    description = "Security group for pizzaluvrs EC2 instances for jenkins"

    tags = {
        Name = "pizzaluvrs-ec2-jenkins-sg"
    }

    ingress {
        from_port = 0
        protocol = "-1"
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port = 0
        protocol = "-1"
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_instance" "pizzaluvrs-ec2-jenkins" {
    ami = data.aws_ami.ubuntu.id
    instance_type = "t2.micro"
    subnet_id = module.vpc.public_subnet_2a_id
    security_groups = [aws_security_group.pizzaluvrs-ec2-jenkins-sg.id]
    associate_public_ip_address = true
    key_name = "pizzaluvrs"

    tags = {
        Name = "pizzaluvrs-ec2-jenkins"
    }
}

resource "null_resource" "pizzaluvrs--jenkins-setup-provisioner" {
    triggers = {
        public_ip = aws_instance.pizzaluvrs-ec2-jenkins.public_ip
    }

    connection {
        type = "ssh"
        host = aws_instance.pizzaluvrs-ec2-jenkins.public_ip
        user = "ubuntu"
        port = 22
        private_key = file("pem/pizzaluvrs.pem")
        agent = false
    }

    provisioner "file" {
        source = "scripts/initialize-jenkins.sh"
        destination = "initialize-jenkins.sh"
    }

    provisioner "remote-exec" {
        inline = [
            "chmod +x /home/ubuntu/initialize-jenkins.sh",
            "/home/ubuntu/initialize-jenkins.sh",
            "sleep 1", # https://stackoverflow.com/a/36732953/4588206
        ]
    }
}

// Application

variable "rds_username" {}

variable "rds_password" {}

resource "aws_iam_role" "pizzaluvrs-ec2-s3-full-access-role" {
    name = "PizzaluvrsEC2S3FullAccess"

    assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
}

resource "aws_iam_policy" "pizzaluvrs-s3-full-access-policy" {
    name = "PizzaluvrsAmazonS3FullAccess"
    description = "Provides full access to all buckets via the AWS Management Console."

    policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "ec2:Describe*"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "pizzaluvrs-application-ec2-s3-access-attachment" {
    role = aws_iam_role.pizzaluvrs-ec2-s3-full-access-role.name
    policy_arn = aws_iam_policy.pizzaluvrs-s3-full-access-policy.arn
}

resource "aws_iam_instance_profile" "pizzaluvrs-application-ec2-iam-profile" {
    name = "pizzaluvrs-application-ec2-iam-profile"
    role = aws_iam_role.pizzaluvrs-ec2-s3-full-access-role.name
}

resource "aws_iam_role" "pizzaluvrs-codedeploy-role" {
    name = "PizzaluvrsCodeDeploy"

    assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "codedeploy.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
}

resource "aws_iam_policy" "pizzaluvrs-codedeploy-policy" {
    name = "PizzaluvrsAWSCodeDeployRole"
    description = "Provides CodeDeploy service access to expand tags and interact with Auto Scaling on your behalf."

    policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "autoscaling:CompleteLifecycleAction",
                "autoscaling:DeleteLifecycleHook",
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribeLifecycleHooks",
                "autoscaling:PutLifecycleHook",
                "autoscaling:RecordLifecycleActionHeartbeat",
                "autoscaling:CreateAutoScalingGroup",
                "autoscaling:UpdateAutoScalingGroup",
                "autoscaling:EnableMetricsCollection",
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribePolicies",
                "autoscaling:DescribeScheduledActions",
                "autoscaling:DescribeNotificationConfigurations",
                "autoscaling:DescribeLifecycleHooks",
                "autoscaling:SuspendProcesses",
                "autoscaling:ResumeProcesses",
                "autoscaling:AttachLoadBalancers",
                "autoscaling:PutScalingPolicy",
                "autoscaling:PutScheduledUpdateGroupAction",
                "autoscaling:PutNotificationConfiguration",
                "autoscaling:PutLifecycleHook",
                "autoscaling:DescribeScalingActivities",
                "autoscaling:DeleteAutoScalingGroup",
                "ec2:DescribeInstances",
                "ec2:DescribeInstanceStatus",
                "ec2:TerminateInstances",
                "tag:GetResources",
                "sns:Publish",
                "cloudwatch:DescribeAlarms",
                "cloudwatch:PutMetricAlarm",
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeInstanceHealth",
                "elasticloadbalancing:RegisterInstancesWithLoadBalancer",
                "elasticloadbalancing:DeregisterInstancesFromLoadBalancer",
                "elasticloadbalancing:DescribeTargetGroups",
                "elasticloadbalancing:DescribeTargetHealth",
                "elasticloadbalancing:RegisterTargets",
                "elasticloadbalancing:DeregisterTargets"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "pizzaluvrs-codedeploy-role-policy-attachment" {
    role = aws_iam_role.pizzaluvrs-codedeploy-role.name
    policy_arn = aws_iam_policy.pizzaluvrs-codedeploy-policy.arn
}

resource "aws_security_group" "pizzaluvrs-ec2-sg" {
    vpc_id = module.vpc.vpc_id
    name = "pizzaluvrs-ec2-sg"
    description = "Security group for pizzaluvrs EC2 instances"

    tags = {
        Name = "pizzaluvrs-ec2-sg"
    }

    ingress {
        from_port = 22
        protocol = "tcp"
        to_port = 22
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        from_port = 8000
        protocol = "tcp"
        to_port = 8000
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port = 0
        protocol = "-1"
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_instance" "pizzaluvrs-ec2-og" {
    ami = data.aws_ami.ubuntu.id
    instance_type = "t2.micro"
    subnet_id = module.vpc.public_subnet_2a_id
    iam_instance_profile = aws_iam_instance_profile.pizzaluvrs-application-ec2-iam-profile.name
    security_groups = [
        aws_security_group.pizzaluvrs-ec2-sg.id]
    key_name = "pizzaluvrs"

    tags = {
        Name = "pizzaluvrs-ec2-og"
    }
}

resource "aws_eip" "pizzaluvrs-eip" {
    vpc = true
    instance = aws_instance.pizzaluvrs-ec2-og.id
}

resource "aws_security_group" "pizzaluvrs-rds-sg" {
    vpc_id = module.vpc.vpc_id
    name = "pizzaluvrs-rds-sg"
    description = "Security group for pizzaluvrs RDS instances"

    tags = {
        Name = "pizzaluvrs-rds-sg"
    }

    ingress {
        from_port = 5432
        protocol = "tcp"
        to_port = 5432
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port = 0
        protocol = "-1"
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_db_subnet_group" "pizzaluvrs-rds-subnet-group" {
    name = "pizzaluvrs-rds-subnet-group"
    description = "pizzaluvrs-rds-subnet-group"
    subnet_ids = [
        module.vpc.private_subnet_2a_id,
        module.vpc.private_subnet_2b_id,
    ]
}

resource "aws_db_instance" "pizzaluvrs-rds" {
    engine = "postgres"
    engine_version = "10.10"
    identifier = "pizzaluvrs"
    username = var.rds_username
    password = var.rds_password
    instance_class = "db.t2.micro"
    storage_type = "gp2"
    allocated_storage = 5
    publicly_accessible = false
    port = 5432
    backup_retention_period = 0
    auto_minor_version_upgrade = true
    db_subnet_group_name = aws_db_subnet_group.pizzaluvrs-rds-subnet-group.name
    skip_final_snapshot = true
    vpc_security_group_ids = [
        aws_security_group.pizzaluvrs-rds-sg.id
    ]
}

resource "null_resource" "pizzaluvrs-setup-provisioner" {
    triggers = {
        public_ip = aws_instance.pizzaluvrs-ec2-og.public_ip
    }

    connection {
        type = "ssh"
        host = aws_eip.pizzaluvrs-eip.public_ip
        user = "ubuntu"
        port = 22
        private_key = file("pem/pizzaluvrs.pem")
        agent = false
    }

    provisioner "file" {
        source = "scripts/initialize-pizzaluvrs.sh"
        destination = "initialize-pizzaluvrs.sh"
    }

    provisioner "remote-exec" {
        inline = [
            "chmod +x /home/ubuntu/initialize-pizzaluvrs.sh",
            "/home/ubuntu/initialize-pizzaluvrs.sh ${aws_db_instance.pizzaluvrs-rds.address} ${aws_db_instance.pizzaluvrs-rds.username} ${aws_db_instance.pizzaluvrs-rds.password}",
            "sleep 1", # https://stackoverflow.com/a/36732953/4588206
        ]
    }
}
