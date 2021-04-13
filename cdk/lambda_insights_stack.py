from aws_cdk import aws_iam, aws_lambda, aws_lambda_python, aws_logs, aws_s3, core


class LambdaInsightsStack(core.Stack):
    def __init__(
        self, scope: core.Construct, construct_id: str, identifier: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = aws_s3.Bucket(
            self,
            id=f"test-bucket-{identifier}",
            auto_delete_objects=True,
            removal_policy=core.RemovalPolicy.DESTROY,
        )

        putter = aws_lambda_python.PythonFunction(
            self,
            id=f"putter-lambda-{identifier}",
            entry="lambda",
            memory_size=3072,
            timeout=core.Duration.minutes(15),
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            environment={"BUCKET": bucket.bucket_name},
            layers=[
                aws_lambda.LayerVersion.from_layer_version_arn(
                    self,
                    id=f"lambda-insights-extension-{identifier}",
                    layer_version_arn=(
                        "arn:aws:lambda:us-west-2:580247275435:"
                        "layer:LambdaInsightsExtension:14"
                    ),
                )
            ],
        )

        aws_logs.LogGroup(
            self,
            id=f"{identifier}-link-fetcher-log-group",
            log_group_name=f"/aws/lambda/{putter.function_name}",
            removal_policy=core.RemovalPolicy.DESTROY,
            retention=aws_logs.RetentionDays.ONE_DAY,
        )

        bucket.grant_read_write(putter)

        putter.role.add_managed_policy(
            aws_iam.ManagedPolicy.from_managed_policy_arn(
                self,
                id=f"cloudwatch-lambda-insights-policy-{identifier}",
                managed_policy_arn=(
                    "arn:aws:iam::aws:policy/"
                    "CloudWatchLambdaInsightsExecutionRolePolicy"
                ),
            )
        )
