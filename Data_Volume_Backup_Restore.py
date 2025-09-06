import boto3
import schedule

def ebs_snapshot():
    ec2_client = boto3.client('ec2', region_name="us-east-1")

    #Filtering desired Volumes based on tags
    available_volumes = ec2_client.describe_volumes(
        Filters = [
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )

    #Available Volumes
    volumes = available_volumes["Volumes"]

    #Creating Snapshot
    for volume in volumes:
        try:
            volume_id = volume["VolumeId"]
            snapshot_response = ec2_client.create_snapshot(
                VolumeId=volume_id
            )
            print(snapshot_response)
        except:
            print(" shuttingDown")


schedule.every(240).seconds.do(ebs_snapshot)

while True:
    schedule.run_pending()
