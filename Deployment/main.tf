terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.60.0"
    }
  }
}
variable "username" {
  description = "Administrator username"
  type        = string
  sensitive   = true
}

variable "password" {
  description = "Administrator password"
  type        = string
  sensitive   = true
}

provider "aws" {
  region     = "eu-central-1"
  access_key = var.username
  secret_key = var.password
}
resource "tls_private_key" "pk" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "kp" {
  key_name   = "myKey" # Create "myKey" to AWS!!
  public_key = tls_private_key.pk.public_key_openssh
}

resource "local_file" "private-key-file" {
  content  = tls_private_key.pk.private_key_pem
  filename = "${path.module}/my_priv_key.pem"
}

variable "win-ami" {
  description = "windows server 2022 with dockers ami"
  type        = string
  default     = "ami-0b616a6b3da8575d5"

}

#variable "ubuntu-ami" {
#  description = "ubuntu 20 lts"
#  type        = string
#  default     = "ami-05f7491af5eef733a"
#
#}

resource "aws_instance" "example" {
  count = 1

  ami                    = var.win-ami
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.kp.key_name
  vpc_security_group_ids = [aws_security_group.websg.id]
  get_password_data      = true

}

#resource "local_file" "windows-credentials" {
#  content  = "IP:${aws_instance.example[0].public_ip}  User:Administrator  Pass:${rsadecrypt(aws_instance.example[0].password_data, tls_private_key.pk.private_key_pem)}"
#  filename = "${path.module}/win_credentials.txt"
#}
resource "local_file" "windows-credentials" {
  content  = "IP:${aws_instance.example[0].public_ip}  User:root  Pass:${rsadecrypt(aws_instance.example[0].password_data, tls_private_key.pk.private_key_pem)}"
  filename = "${path.module}/win_credentials.txt"
}


#####################################################################


resource "aws_security_group" "websg" {
  name = "web-sg01"
  ingress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}
output "instance_ips" {
  value = aws_instance.example[0].public_ip
}
