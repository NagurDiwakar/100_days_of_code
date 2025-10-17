# Provider configuration with separate profile
provider "aws" {
  region  = var.region
  profile = var.aws_profile  # Uses separate AWS profile
}

resource "aws_instance" "server_1" {
  ami           = "ami-0391075f6ae31e21f"  # Amazon Linux 2 AMI arm supported ami [t4 type is arm based graviton]
  instance_type = var.instance_type
}