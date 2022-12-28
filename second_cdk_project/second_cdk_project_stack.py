from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
    
    # aws_sqs as sqs,
)
from constructs import Construct

class MyAritfactBucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        if is_prod:
             artifactBucket = s3.Bucket(self,
                                       "myProdArtifactBucketId",
                                       versioned=True,
                                       encryption=s3.BucketEncryption.S3_MANAGED,
                                       removal_policy=RemovalPolicy.RETAIN
                                      )
        else:
            artifactBucket = s3.Bucket(self,
                                       "myDevArtifactBucketId")
            
            

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "MySecondProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
