#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk import (
    # Duration,
    Environment
    
    # aws_sqs as sqs,
)

from second_cdk_project.second_cdk_project_stack import MyAritfactBucketStack


app = cdk.App()

env_us = Environment(account=app.node.try_get_context('Kavya')['account'],region=app.node.try_get_context('Kavya')['region'])


MyAritfactBucketStack(app, "MyDevStack", env=env_us)
MyAritfactBucketStack(app, "MyProdStack", is_prod=True, env=env_us
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
