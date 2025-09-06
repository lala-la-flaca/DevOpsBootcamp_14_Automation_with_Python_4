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
✅ Automates EC2 volume backups
🗑️ Cleans up old snapshots
🔄 Restores volumes from snapshots

# Prerequisites
* AWS account
* Python and PyCharm installed.
* Terraform EKS demo.
  
# 🏗 Project Architecture

# ⚙️ Project Configuration
   
## Adding Tags to EC2 Instances
1. Deploy the EKS infrastructure using Terraform from the demo in the Terraform section.
   
2. Import boto3 module.
   ```bash
   import boto3
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_2/blob/main/Img/2.PNG" width=800 />
   

        
      <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_14_Automation_with_Python_3/blob/main/Img/5%20getting%20endpoint%20and%20version.png" width=800 />
      
   
