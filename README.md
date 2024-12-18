# 🟢 **udacity-aws-mle-nano-course5**
**Udacity AWS Machine Learning Engineers Nanodegree** (ND189)    

## **👉 Project 4 Submission**  

* Step 1: Training and deployment on Sagemaker  

  * Check [the screenshots](https://docs.google.com/document/d/1SJTQBwdd3jptwA0SDJCbmpsjjIWyN9h1s9LYEoFcw_U)  

  * Set up VPC   
     
    Since my current role doesn't have the permissions to create an `Internet Gateway`, `NAT Gateway`, or assign an `Elastic IP` address, I set up a SageMaker notebook instance in the default VPC's public subnet in one of the Availability Zones. I enabled direct internet access for the instance so the notebook kernel can update Python libraries.

  * Set up S3 bucket  

    The dog images uploaded for Project 2 from an S3 bucket in another account was reused. To do this, I created an `S3 Gateway` endpoint within the VPC and updated the S3 bucket policy to enable cross-account access.

  * Training

    The `train_and_deploy-solution.ipynb` and `hpo.py` files were uploaded to the notebook instance and ran the notebook. The HPO job, which had 2 runs on an `ml.g4dn.xlarge` instance, took about 40 minutes. Afterward, using the 'best hyperparameters,' I ran a multi-instance training job on two `ml.g4dn.xlarge` instances.

    I chose the `ml.g4dn.xlarge` instance because it's one of the smaller GPU options, and it worked very well for the image classification task in Project 3 training.

  * Deployment

    The `inference2.py` file was uploaded to the notebook instance, deployed an inference endpoint, and tested it. Since the focus of this project is on ML operations, inference accuracy isn't the primary concern.

  * Clean up resources

    Afterwards, the model, endpoint, and notebook instance were deleted.  
    

   


## **Course 5** Operationalizing Machine Learning on SageMaker   

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

---  

## **Logs**     

2024-12-09 repo created   
