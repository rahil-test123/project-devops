variable "aws_region" {
  default = "eu-west-3"
}

variable "key_name" {
  default = "devops-key"
}

variable "master_instance_type" {
  default = "t3.small"
}

variable "worker_instance_type" {
  default = "t3.small"
}