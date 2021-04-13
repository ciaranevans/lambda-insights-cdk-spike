#!/usr/bin/env python3
import os

from aws_cdk import core
from lambda_insights_stack import LambdaInsightsStack

app = core.App()

IDENTIFIER = os.environ["IDENTIFIER"]

stack = LambdaInsightsStack(
    app, f"lambda-insights-stack-{IDENTIFIER}", identifier=IDENTIFIER
)

for k, v in {
    "Project": "lambda-insights-spike",
    "Owner": "ciaran-developmentseed",
    "Client": "ciaran-developmentseed",
    "Stack": IDENTIFIER,
}.items():
    core.Tags.of(stack).add(k, v, apply_to_launched_instances=True)

app.synth()
