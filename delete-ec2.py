import boto.ec2
conn = boto.ec2.connect_to_region("us-east-1", aws_access_key_id='', aws_secret_access_key='')


conn.terminate_instances('i-08fa86c9baded6e1b')
