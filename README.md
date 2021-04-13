# lambda-insights-cdk-spike

'Quick' Spike to investigate using Lambda Insights within CloudWatch (Via CDK)

# Requirements

* NVM [Node Version Manager](https://github.com/nvm-sh/nvm) / Node 14
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) - There is a `package.json` in the repository, it's recommended to run `npm install` in the repository root and make use of `npx <command>` rather than globally installing AWS CDK
* Python 3.8.* / [pyenv](https://github.com/pyenv/pyenv)
* [poetry](https://github.com/python-poetry/poetry)
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

# Deployment

To deploy the infrastructure, you'll need to first install all dependencies:

```bash
$ make install
```

You will also need a `.env` file with the contents:

```bash
IDENTIFIER="<unique-identifier-for-your-deployment>"
AWS_DEFAULT_REGION="<region-name>"
AWS_DEFAULT_PROFILE="<name-of-your-aws-cli-profile>"
```

You can then deploy the stack with:

```bash
$ make deploy
```

And destroy it with:

```bash
$ make destroy
```

# Insights

Once deployed, the `putter` Lambda Function can be invoked, it will create and upload a 1GB file to S3 to the Bucket deployed.

You can navigate to CloudWatch and then go to `Metrics > All > LambdaInsights > <Function Name>` to find all the metrics that Lambda Insights provides.

If you want to see the total outbound network traffic in bytes, you can select and graph `tx_bytes`, you'll get something like:

![tx_bytes for `putter`](./images/tx_bytes_screenshot.png)

You'll notice my graph differs from `1.28G` to `477M`, that's because I played around with the numbers in `lambda/index.py`.
