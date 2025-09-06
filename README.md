# 🐍Module 14 – Automation with Python
This exercise is part of Module 14: Automation with Python. Module 14 focuses on automating cloud operations with Python. The demos showcase how to interact with AWS services (EC2, EKS, snapshots), perform monitoring tasks, and implement recovery workflows. By the end of this module, you will have practical experience in scripting infrastructure automation, monitoring, and recovery solutions.

# 📦Demo 4 – Data Backup and Restore
# 📌 Objective
  Automate creation, cleanup, and restoration of EC2 snapshots using Python.

# 🚀 Technologies Used
* Python: programming language.
* IntelliJ-PyCharm: IDE used for development.
* AWS: Cloud provider.
* Boto3 AWS SDK for Python.
* Terraform

# 🎯 Features
✅ Automates EC2 volume backups.
🗑️ Cleans up old snapshots.
🔄 Restores volumes from snapshots

# Prerequisites
* AWS account
* Python and PyCharm installed.
* Terraform EKS demo.
  
# 🏗 Project Architecture

# ⚙️ Project Configuration
   
## Creating Snapshots
1. Deploy infrastructure with Terraform
   
2. Import boto3 module.
   ```bash
   import boto3
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_2/blob/main/Img/2.PNG" width=800 />
   
3. Import Schedule module
   ```bash
   import schedule
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/3.PNG" width=800 />
   
4. Initialize client
   ```bash
    ec2_client = boto3.client('ec2', region_name="us-east-1")
   ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/4.PNG" width=800 />
   
5. Filter Volumes based on tags
   ```bash
      #Filtering desired Volumes based on tags
      available_volumes = ec2_client.describe_volumes(
          Filters = [
              {
                  'Name': 'tag:Name',
                  'Values': ['prod']
              }
          ]
      )
   ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/5.PNG" width=800 />
   
6. Obtain available volumes
   ```bash
     #Available Volumes
    volumes = available_volumes["Volumes"]
   ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/6.PNG" width=800 />
   
7. Create Snapshots for the volumes
   ```bash
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
  
   ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/7.PNG" width=800 />
   
8. Schedule the task
    ```bash
          schedule.every(240).seconds.do(ebs_snapshot)
      
      while True:
          schedule.run_pending()
    ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/8.PNG" width=800 />

9. Snapshots on AWS
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/snapshots%20on%20aws.PNG" width=800/>
   
## Cleaning up Snapshots
1. Import the boto3 and operator module.
   ```bash
   import boto3
   from operator import itemgetter
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/c1.PNG" width=800 />
    
2. Initialize the EC2 client.
   ```bash
    #Getting EC2 Client
    ec2_client = boto3.client('ec2', region_name="us-east-1")
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/c_2.PNG" width=800 />
    
3. Filter volumes by tag.
   ```bash
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

   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/c3.PNG" width=800 />
    
4. Check available snapshots for each volume.
    ```bash
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

   ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/c4.PNG" width=800 />
   
5. Sort the snapshots.
    ```bash
        #Sorting the list by the StartTime item by default is ascending
        #To change behavior, use the reverse= True
        sorted_snapshots_by_date = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)
        print(f"Sorted: {sorted_snapshots_by_date}")
     ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/c5.PNG" width=800 />
      
6. Delete the old snapshots.
   ```bash
       for snapshot in sorted_snapshots_by_date[2:]:
        print("Deleting Snapshots")
        snapshot_id = snapshot["SnapshotId"]
        response = ec2_client.delete_snapshot(
            SnapshotId=snapshot_id
        )
        print("This is the response:")
        print(response)
   ```
  <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/c6.PNG" width=800 />

 
  
## Restore Snapshot
1. Import boto3 and operator modules.
   ```bash
    import boto3
    from operator import itemgetter
   ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/r1.PNG" width=800 />
    
2. Initialize EC2 client and resource.
   ```bash
   ec2_client = boto3.client('ec2', region_name="us-east-1")
   ec2_resource = boto3.resource('ec2',region_name="us-east-1")
   ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/r2.PNG" width=800 />
    
3. Hardcode instance ID.
   ```bash
   instance_id = "i-01bbd5b3855bba8b1"
   ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/r3.PNG" width=800 />
    
4. Get Volumes attached to the Instance ID.
   ```bash
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
   ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/r4.PNG" width=800 />
    
5. Verify Available snapshorts for Volume.
    ```bash
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
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/r5.PNG" width=800 />
   
6. Sort snapshorts.
    ```bash
      sorted_snapshots_by_date = sorted(snapshots, key=itemgetter('StartTime'), reverse=True)
      latest_snapshot = sorted_snapshots_by_date[0]
      latest_snapshot_id = latest_snapshot['SnapshotId']
     ```
    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/r6.PNG" width=800 />
    
7. Create a new volume to apply the latest snapshot.
    ```bash
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
    ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/r7.PNG" width=800 />
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/r8.PNG" width=800 />
   
    
8. New Volume:

   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_4/blob/main/Img/new%20volume%20avialable.PNG" width=800/>
