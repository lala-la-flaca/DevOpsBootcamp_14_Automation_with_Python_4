import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="us-east-1")
ec2_resource = boto3.resource('ec2',region_name="us-east-1")

instance_id = "i-01bbd5b3855bba8b1"

#Getting Volumes Attached to instance iD
available_volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

instance_volume = available_volumes["Volumes"][0]
instance_volume_id = instance_volume["VolumeId"]
print(instance_volume)


available_snapshots = ec2_client.describe_snapshots(
        OwnerIds=["self"],
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [instance_volume_id]
            }
        ]
    )
snapshots =  available_snapshots['Snapshots']
sorted_snapshots_by_date = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)
latest_snapshot = sorted_snapshots_by_date[0]
latest_snapshot_id = latest_snapshot['SnapshotId']

#Creating a New Volume
new_volume = ec2_client.create_volume(
    SnapshotId = latest_snapshot_id,
    AvailabilityZone = "us-east-1a",
    TagSpecifications=[
        {
            'ResourceType':'volume',
            'Tags':[
                    {
                        'Key':'Name',
                        'Value':'prod'
                    }
            ]
        }
    ]
)

while True:
   vol =  ec2_resource.Volume(new_volume['VolumeId'])
   print(vol.state)
   if vol.state == 'available':
       ec2_resource.Instance(instance_id).attach_volume(
           VolumeId=new_volume['VolumeId'],
           Device='/dev/xvdb'
       )
       break