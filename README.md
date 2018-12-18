# start_stop_ec2_instances
## Start and stop ec2 instances on a schedule to save money

1. Create a lambda job for each start and stop script.
1. Create and assign the role to the lambda job, so it has permission to start/stop ec2 instances.
1. Run the respective job on a cron schedule, whenver you want to look for instances to stop or start.
..* i.e. Description: stops EC2 instances every day at night at 0 UTC Schedule expression: cron(0 0 * * ? *)
1. Tag intances with "Stop_at_night": True, to have the instances stopped when the stop script runs.
1. Tag intances with "Start_in_morning": True, to have the instances started when the start script runs.
