variable "region" {
  type        = string
  description = "Region where the instance is created and also for s3 bucket"
  default     = "us-east-1"
}

variable "common_tags" {
  description = "the common tags like name, owner, purpose.."
  type        = map(any)
}



# variable "aws_access_key" {
#   default = "ASIAXWDRTCCOFDKP3OAH"
# }
# variable "aws_secret_key" {
#   default = "fWMgMoL2FNUHwcmzZOw+6NMUD242CewZsdtOdtJ+"
# }
