from aws_cdk import (
    aws_cloudfront as cf,
    aws_s3 as s3,
    core
)


class StaticSiteStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, domain: str, **kwargs) -> None:
        self.domain = domain
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "sitebucket", bucket_name=domain, public_read_access=True, website_index_document="index.html")
        core.CfnOutput(self, "siteBucketName", value=bucket.bucket_name)
        core.CfnOutput(self, "siteBucketWebsite", value=bucket.bucket_website_url)

        source_config = cf.SourceConfiguration(
            s3_origin_source = cf.S3OriginConfig(
                s3_bucket_source=bucket,
            ),
            behaviors = [cf.Behavior(is_default_behavior=True)]
        )

        dist = cf.CloudFrontWebDistribution(
            self,
            "staticSiteDist",
            origin_configs = [source_config]
        )
        core.CfnOutput(self, 'static_site_dist_id', value=dist.distribution_id)
        core.CfnOutput(self, 'static_site_cloudfront_domain', value=dist.domain_name)
