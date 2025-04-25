terraform {
  backend "s3" {
    bucket = "983510677257-misc"
    key    = "kinometer/main/terraform.tfstate"
    region = "us-east-1"
  }
}
