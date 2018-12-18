import boto3
# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g., 'us-east-1'
region = 'us-east-1'

# Boto is the AWS SDK for Python
ec = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):

    # get a list of information about instances that match your filter
    # Only look for instances that have Start_in_morning True/true
    reservations = ec.describe_instances(
        Filters = [
        {'Name': 'tag:Start_in_morning', 'Values': ['True','true']}
    ]
    ).get(
        'Reservations', []
    )

    # get the intance information from the reservations
    instances = sum(
        [
            [i for i in r['Instances']]
            for r in reservations
        ], [])

    print "Found %d instance(s) that need to be started" % len(instances)
    
    # start the instances
    for instance in instances:
    	print "starting instance: " + (i[u'Value'] for i in instance[u'Tags'] if i[u'Key'] == 'Name').next() + " ---> " +  instance[u'InstanceId']
    	ec.start_instances(InstanceIds=[instance[u'InstanceId']])

