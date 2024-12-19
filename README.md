# 🟢 **udacity-aws-mle-nano-course5**
**Udacity AWS Machine Learning Engineers Nanodegree** (ND189)    

<br><br><br>  

## **👉 Project 4 (Course 5) Writeup Submission**  

* **Step 1: Training and deployment on Sagemaker**  

  * Check [the screenshots](https://docs.google.com/document/d/1SJTQBwdd3jptwA0SDJCbmpsjjIWyN9h1s9LYEoFcw_U)   
    Check [the training and deployment notebook](https://github.com/nov05/udacity-aws-mle-nano-course5/blob/main/train_and_deploy-solution.ipynb)   

  * **Set up VPC**     
     
    Since my current AWS role doesn't have the permissions to create an `Internet Gateway`, `NAT Gateway`, or assign an `Elastic IP` address, I set up a SageMaker notebook instance in the default VPC's public subnet in one of the Availability Zones, using the launch-wizard-1 Security Group, which allows all inbound and outbound traffic. I enabled direct internet access for the instance so the notebook kernel can update Python libraries.

  * **Set up S3 bucket**  

    The dog images uploaded for Project 3 from an S3 bucket in another account was reused. To do this, I created an `S3 Gateway` endpoint within the VPC and updated the S3 bucket policy to enable **cross-account access**.

  * **Training**

    The `train_and_deploy-solution.ipynb` and `hpo.py` files were uploaded to the notebook instance and ran the notebook. The HPO job, which had 2 runs on an `ml.g4dn.xlarge` instance, took about 40 minutes. Afterward, using the 'best hyperparameters,' I ran a multi-instance training job on two `ml.g4dn.xlarge` instances.

    I chose the `ml.g4dn.xlarge` instance because it's one of the smaller GPU options, and it worked very well for the image classification task in Project 3 training.

  * **Deployment**

    The `inference2.py` file was uploaded to the notebook instance, deployed an inference endpoint, and tested it. Since the focus of this project is on ML operations, inference accuracy isn't the primary concern.

  * **Clean up resources**

    Afterwards, the model, endpoint, and notebook instance were deleted.  

<br>  

* **Step 2: EC2 Training**   

  * Check [the operation details and screenshots](https://docs.google.com/document/d/1rQNjzYOEKrZ3y9Jd0TLPLukJ3qLOw354xQA9wTCkTQ0)     
    Check [the demo training code](https://github.com/nov05/udacity-aws-mle-nano-course5/blob/main/ec2train1.py)   

  * Since the demo training code doesn't appear to use a GPU, we launched a `t2.xlarge` CPU EC2 instance for the training. Obviously, SageMaker is a fully managed service that saves the hassle of installing GPU drivers, CUDA, Python dependencies, and more. However, managing resources ourselves could potentially reduce costs.   

  * Image: Amazon Linux 2023 AMI   
    Intance type: `t2.xlarge` (w/o GPU)  
    Security group: launch-wizard-1 (all inbound/outbound traffic allowed)  
    Role name: udacity-p4-ec2 (permissions: `AmazonElasticMapReduceforEC2Role`, SageMaker execution role, and S3 full access)  
    Dependencies: `torch`, `torchvision`, `Pillow` (including `Numpy`), `tqdm`   

<br>

* **Step 3: Lambda function setup**  

<br>

* **Step 4: Security and testing**  

<br>

* **Step 5: Concurrency and auto-scaling**   
   
<br><br><br>

## **Course 5 Operationalizing Machine Learning on SageMaker**   

* Course notes  
  [Google Docs](https://docs.google.com/document/d/1B-k7xFlayJ00NrplcPeRvgP8dxsMggOmTabE135bCEw)  

* 2.15 Exercise: Lowering Costs with Spot Instances  
  🏷️ [my demo video](https://youtu.be/Em-MJqLuH74)  

* 3.5 Exercise: Multi-instance Distributed-data Training   
  [Overview](https://www.evernote.com/shard/s139/u/0/sh/904108fe-8c48-4ddc-bcd9-fbd28630d110/rNquyVO6wK0fK1BhUfqv7FZEdfCsv0wqHrl94n8oIcn1AX-qlKS3itkZ6w)   
  🏷️ [notebook](https://github.com/nov05/udacity-aws-mle-nano-course5/blob/main/exercise_3.5/multiinstancestarterfile.ipynb)  

* 3.13 Exercise: Manifest Files  
  🏷️ [notebook](https://nbviewer.org/github/nov05/udacity-aws-mle-nano-course5/blob/main/excercise_3.13/manifestfilestarter.ipynb)  

* 4.8 Exercise: Autoscaling   
  🏷️ [notebook](https://github.com/nov05/udacity-aws-mle-nano-course5/blob/main/exercise_4.8/simpleendpoint1.ipynb)    

* 4.16 Exercise: Feature Store   
  🏷️ [my demo video](https://www.youtube.com/watch?v=FT41tM9cDVc)  
  🏷️ [notebook](https://github.com/nov05/udacity-aws-mle-nano-course5/blob/main/exercise_4.16/New%20data%20flow%202024-12-11%2011_07_14%20PM.ipynb)  (The feature group data processing lacks the necessary ECR permissions.)   
  [notebook from Course 3 Lesson 4](https://github.com/nov05/udacity-nd009t-C2-Developing-ML-Workflow/blob/master/lesson4/exercises-solutions.ipynb) (The feature group data processing lacks the necessary Glue permissions.)  

* 6.1 Course Project   
  [Introduction](https://www.evernote.com/shard/s139/u/0/sh/1db5a63a-b7d4-4f4b-8f83-b6f68e86dbc2/supBQKkZk60tY8YA6uYPBsHIJKuX6N9771fFguFETNqIZwsYHa1Z0fTtlA)  

<br><br><br>    

## **Logs**     

2024-12-09 repo created   
