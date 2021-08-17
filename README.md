## AWS Secrets Manager Rotation Examples

Contains **sample code** that can be used for **rotation** of **secrets** stored in **AWS Secrets Manager**.



### [Examples for other services](#OTHER-rotation-templates)

+ [Amazon CloudFront API Key header injection](#sar-template-cloudfront-apikey-header-injection)
+ [Amazon ALB API Key header check](#sar-template-alb-apikey-header-check)



## Examples for _other_ services<a name="OTHER-rotation-templates"></a>

_Where **other services** are those beyond the stereotypical, such as databases, with a simple username+password combo._

### Amazon CloudFront API Key header injection<a name="sar-template-cloudfront-apikey-header-injection"></a>
+ **Name:** SecretsManagerCloudFront
+ **Supported service:** CloudFront\. This Lambda function will add a header to to requests from CloudFront to the backend origin service\.
+ **Rotation strategy:** A secret contains a json string of 3 active key values\. The Lambda Function will pop the oldest key, push a new key, then update a CloudFront distribution to match\.
+ **Expected `SecretString` structure:** 

  ```
  {
    "key1": "<required:string>",
    "key2": "<required:string>",
    "key3": "<required:string>",
  }
  ```

+ **Source code:** [SecretsManagerCloudFront/](SecretsManagerCloudFront/)


### Amazon ALB API Key header check<a name="sar-template-alb-apikey-header-check"></a>
+ **Name:** SecretsManagerAlb
+ **Supported service:** Application Load Balancer\. This Lambda function will update the ALB Listener Rules to look for a static API key header\. Unless the header is found, the request will be returned an HTTP403 Access Denied response\.
+ **Rotation strategy:** A secret contains a json string of 3 active key values\. The Lambda Function will pop the oldest key, push a new key, then update ALB Listener Rules to match\.
+ **Expected `SecretString` structure:** 

  ```
  {
    "key1": "<required:string>",
    "key2": "<required:string>",
    "key3": "<required:string>",
  }
  ```

+ **Source code:** [SecretsManagerAlb/](SecretsManagerAlb/)




## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This sample code is made available under the MIT-0 License. See the [LICENSE](LICENSE) file.

