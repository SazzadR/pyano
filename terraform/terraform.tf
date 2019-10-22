provider "aws" {
    version = "~> 2.0"
    region = "us-west-2"
}

resource "aws_vpc" "pizzaluvrs" {
    cidr_block = "10.0.0.0/16"

    tags = {
        Name = "pizzaluvrs-vpc"
    }
}

resource "aws_internet_gateway" "pizzaluvrs-igw" {
    vpc_id = "${aws_vpc.pizzaluvrs.id}"

    tags = {
        Name = "pizzaluvrs-igw"
    }
}

resource "aws_route_table" "pizzaluvrs-public-rtb" {
    vpc_id = "${aws_vpc.pizzaluvrs.id}"

    tags = {
        Name = "pizzaluvrs-public-rtb"
    }

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = "${aws_internet_gateway.pizzaluvrs-igw.id}"
    }
}

resource "aws_route_table" "pizzaluvrs-private-rtb" {
    vpc_id = "${aws_vpc.pizzaluvrs.id}"

    tags = {
        Name = "pizzaluvrs-private-rtb"
    }
}

resource "aws_subnet" "pizzaluvrs-public-subnet-2a" {
    vpc_id = "${aws_vpc.pizzaluvrs.id}"
    availability_zone = "us-west-2a"
    cidr_block = "10.0.1.0/24"

    tags = {
        Name = "pizzaluvrs-public-subnet-2a"
    }
}

resource "aws_route_table_association" "public-subnet-2a" {
    route_table_id = "${aws_route_table.pizzaluvrs-public-rtb.id}"
    subnet_id = "${aws_subnet.pizzaluvrs-public-subnet-2a.id}"
}

resource "aws_subnet" "pizzaluvrs-public-subnet-2b" {
    vpc_id = "${aws_vpc.pizzaluvrs.id}"
    availability_zone = "us-west-2b"
    cidr_block = "10.0.2.0/24"

    tags = {
        Name = "pizzaluvrs-public-subnet-2b"
    }
}

resource "aws_route_table_association" "public-subnet-2b" {
    route_table_id = "${aws_route_table.pizzaluvrs-public-rtb.id}"
    subnet_id = "${aws_subnet.pizzaluvrs-public-subnet-2b.id}"
}

resource "aws_subnet" "pizzaluvrs-private-subnet-2a" {
    vpc_id = "${aws_vpc.pizzaluvrs.id}"
    availability_zone = "us-west-2a"
    cidr_block = "10.0.3.0/24"

    tags = {
        Name = "pizzaluvrs-private-subnet-2a"
    }
}

resource "aws_route_table_association" "private-subnet-2a" {
    route_table_id = "${aws_route_table.pizzaluvrs-private-rtb.id}"
    subnet_id = "${aws_subnet.pizzaluvrs-private-subnet-2a.id}"
}

resource "aws_subnet" "pizzaluvrs-private-subnet-2b" {
    vpc_id = "${aws_vpc.pizzaluvrs.id}"
    availability_zone = "us-west-2b"
    cidr_block = "10.0.4.0/24"

    tags = {
        Name = "pizzaluvrs-private-subnet-2b"
    }
}

resource "aws_route_table_association" "private-subnet-2b" {
    route_table_id = "${aws_route_table.pizzaluvrs-private-rtb.id}"
    subnet_id = "${aws_subnet.pizzaluvrs-private-subnet-2b.id}"
}

resource "aws_security_group" "pizzaluvrs-ec2-sg" {
    vpc_id = "${aws_vpc.pizzaluvrs.id}"
    name = "pizzaluvrs-ec2-sg"
    description = "Security group for pizzaluvrs EC2 instances"

    tags = {
        Name = "pizzaluvrs-ec2-sg"
    }

    ingress {
        from_port = 8000
        protocol = "tcp"
        to_port = 8000
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        from_port = 22
        protocol = "tcp"
        to_port = 22
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port = 0
        protocol = "-1"
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
}

data "aws_ami" "ubuntu" {
    most_recent = true

    filter {
        name = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-*"]
    }

    owners = ["099720109477"]
}

resource "aws_instance" "pizzaluvrs-ec2-og" {
    ami = "${data.aws_ami.ubuntu.id}"
    instance_type = "t2.micro"
    subnet_id = "${aws_subnet.pizzaluvrs-public-subnet-2a.id}"
    security_groups = ["${aws_security_group.pizzaluvrs-ec2-sg.id}"]
    key_name = "pizzaluvrs"

    tags = {
        Name = "pizzaluvrs-ec2-og"
    }
}

resource "aws_eip" "pizzaluvrs-eip" {
    instance = "${aws_instance.pizzaluvrs-ec2-og.id}"
    vpc = true

    tags = {
        Name = "pizzaluvrs-eip"
    }
}
