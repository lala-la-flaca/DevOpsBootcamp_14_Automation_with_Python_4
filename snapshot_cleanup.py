from operator import itemgetter
import boto3

#Getting EC2 Client
ec2_client = boto3.client('ec2', region_name="us-east-1")

# Filtering desired Volumes based on tags
available_volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['prod']
        }
    ]
)

volumes = available_volumes["Volumes"]
print(f"Available volumes: {available_volumes}")
snapshots = ""

for volume in volumes:
    volume_id = volume["VolumeId"]

    #Getting available Snapshots for desired volumeId
    available_snapshots = ec2_client.describe_snapshots(
        OwnerIds=["self"],
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [volume_id]
            }
        ]
    )
    snapshots =  available_snapshots['Snapshots']
    print("Snapshots available:")
    print(snapshots)

    #Sorting the list by the StartTime item by default is ascending
    #To change behavior use the reverse= True
    sorted_snapshots_by_date = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)
    print(f"Sorted: {sorted_snapshots_by_date}")

    for snapshot in sorted_snapshots_by_date[2:]:
        print("Deleting Snapshots")
        snapshot_id = snapshot["SnapshotId"]
        response = ec2_client.delete_snapshot(
            SnapshotId=snapshot_id
        )
        print("This is the response:")
        print(response)








