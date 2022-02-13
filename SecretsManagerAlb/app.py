from aws_cdk import App

from alb_secrets_stack import ALBSecretsStack

app = App()
env = {'region': 'us-east-1'}

ALBSecretsStack(app, "ALBSecretsStack", env=env, description="ALB Secrets")

app.synth()

