variable "app_name" {
  type = string
}

variable "domain_name" {
  type = string
}

variable "price_class" {
  type    = string
  default = "PriceClass_100"
}

variable "acm_certificate_arn" {
  type        = string
  description = "The ARN of the SSL certificate"
}

variable "hosted_zone_id" {
  type = string
}
