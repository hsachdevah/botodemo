import boto.ec2
conn = boto.ec2.connect_to_region("us-east-1", aws_access_key_id='AKIAIH6WXO2W3Y2YTI7A', aws_secret_access_key='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')


conn.terminate_instances('i-08fa86c9baded6e1b')
