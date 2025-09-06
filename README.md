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
   ``
    <img src="" width=800 />
   
4. Initialize client
   ```bash
    ec2_client = boto3.client('ec2', region_name="us-east-1")
   ```
    <img src="" width=800 />
   
6. Filter Volumes based on tags
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
    <img src="" width=800 />
   
7. Obtain available volumes
   ```bash
     #Available Volumes
    volumes = available_volumes["Volumes"]
   ```
    <img src="" width=800 />
   
8. Create Snapshots for the volumes
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
    <img src="" width=800 />   
9. Schedule the task
    ```bash
          schedule.every(240).seconds.do(ebs_snapshot)
      
      while True:
          schedule.run_pending()
    ```
    <img src="" width=800 />       
   
