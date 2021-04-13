from aws_cdk import aws_lambda, aws_lambda_python, aws_logs, aws_s3, core


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
        )

        aws_logs.LogGroup(
            self,
            id=f"{identifier}-link-fetcher-log-group",
            log_group_name=f"/aws/lambda/{putter.function_name}",
            removal_policy=core.RemovalPolicy.DESTROY,
            retention=aws_logs.RetentionDays.ONE_DAY,
        )

        bucket.grant_read_write(putter)
