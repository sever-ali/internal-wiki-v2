variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "region" {
  description = "AWS region"
  default     = "eu-west-2"
}

variable "key_name" {
  description = "SSH key pair name"
  default     = "devops-key-v2"
}