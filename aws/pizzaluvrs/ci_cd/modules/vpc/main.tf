resource "aws_vpc" "pizzaluvrs" {
    cidr_block = "10.0.0.0/16"

    tags = {
        Name = "pizzaluvrs-vpc"
    }
}

resource "aws_internet_gateway" "pizzaluvrs-igw" {
    vpc_id = aws_vpc.pizzaluvrs.id

    tags = {
        Name = "pizzaluvrs-igw"
    }
}

resource "aws_route_table" "pizzaluvrs-public-rtb" {
    vpc_id = aws_vpc.pizzaluvrs.id

    tags = {
        Name = "pizzaluvrs-public-rtb"
    }

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.pizzaluvrs-igw.id
    }
}

resource "aws_route_table" "pizzaluvrs-private-rtb" {
    vpc_id = aws_vpc.pizzaluvrs.id

    tags = {
        Name = "pizzaluvrs-private-rtb"
    }
}

resource "aws_subnet" "pizzaluvrs-public-subnet-2a" {
    vpc_id = aws_vpc.pizzaluvrs.id
    availability_zone = "us-west-2a"
    cidr_block = "10.0.1.0/24"

    tags = {
        Name = "pizzaluvrs-public-subnet-2a"
    }
}

resource "aws_route_table_association" "public-subnet-2a" {
    route_table_id = aws_route_table.pizzaluvrs-public-rtb.id
    subnet_id = aws_subnet.pizzaluvrs-public-subnet-2a.id
}

resource "aws_subnet" "pizzaluvrs-public-subnet-2b" {
    vpc_id = aws_vpc.pizzaluvrs.id
    availability_zone = "us-west-2b"
    cidr_block = "10.0.2.0/24"

    tags = {
        Name = "pizzaluvrs-public-subnet-2b"
    }
}

resource "aws_route_table_association" "public-subnet-2b" {
    route_table_id = aws_route_table.pizzaluvrs-public-rtb.id
    subnet_id = aws_subnet.pizzaluvrs-public-subnet-2b.id
}

resource "aws_subnet" "pizzaluvrs-private-subnet-2a" {
    vpc_id = aws_vpc.pizzaluvrs.id
    availability_zone = "us-west-2a"
    cidr_block = "10.0.3.0/24"

    tags = {
        Name = "pizzaluvrs-private-subnet-2a"
    }
}

resource "aws_route_table_association" "private-subnet-2a" {
    route_table_id = aws_route_table.pizzaluvrs-private-rtb.id
    subnet_id = aws_subnet.pizzaluvrs-private-subnet-2a.id
}

resource "aws_subnet" "pizzaluvrs-private-subnet-2b" {
    vpc_id = aws_vpc.pizzaluvrs.id
    availability_zone = "us-west-2b"
    cidr_block = "10.0.4.0/24"

    tags = {
        Name = "pizzaluvrs-private-subnet-2b"
    }
}

resource "aws_route_table_association" "private-subnet-2b" {
    route_table_id = aws_route_table.pizzaluvrs-private-rtb.id
    subnet_id = aws_subnet.pizzaluvrs-private-subnet-2b.id
}

output "vpc_id" {
    value = aws_vpc.pizzaluvrs.id
}

output "public_subnet_2a_id" {
    value = aws_subnet.pizzaluvrs-public-subnet-2a.id
}

output "public_subnet_2b_id" {
    value = aws_subnet.pizzaluvrs-public-subnet-2b.id
}

output "private_subnet_2a_id" {
    value = aws_subnet.pizzaluvrs-private-subnet-2a.id
}

output "private_subnet_2b_id" {
    value = aws_subnet.pizzaluvrs-private-subnet-2b.id
}

