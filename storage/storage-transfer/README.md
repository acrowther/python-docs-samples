# Transfer Service sample using Python

This app creates two types of transfers using the Transfer Service tool.

## Prerequisites

1. Set up a project on Cloud Console.
  1. Go to the [Cloud Console](https://cloud.google.com/console) and create or select your project.
     You will need the project ID later.
1. Set up gcloud for application default credentials.
  1. `gcloud components update`
  1. `gcloud auth login`
  1. `gcloud config set project PROJECT_ID`

## Transfer from AWS S3

Creating a one-time transfer between Amazon AWS S3 and Google Cloud Storage.
1. Set up data sink.
  1. Go to the Cloud Console and create a bucket under Cloud Storage > Storage Browser.
1. Set up data source.
  1. Go to Amazon AWS S3 console and create a bucket.
  1. Under Security Credentials, create an IAM User with access to the bucket.
  1. Create an Access Key for the user. Note the Access Key ID and Secret Access Key.
1. In aws_request.py, fill in the Transfer Job json template with relevante values.
1. Run with `python aws_request.py`
  1. Note the job ID in the returned Transfer Job.

## Transfer to Nearline

Creating a daily transfer between a regular Cloud Storage bucket and a Nearline
Cloud Storage bucket for files untouched for 30 days.
1. Set up data sink.
  1. Go to the Cloud Console and create a bucket under Cloud Storage > Storage Browser.
  1. Select Nearline for Storage Class.
1. Set up data source.
  1. Go to the Cloud Console and create a bucket under Cloud Storage > Storage Browser.
1. In nearline_request.py, fill in the Transfer Job json template with relevante values.
1. Run with `python nearline_request.py`
  1. Note the job ID in the returned Transfer Job.

## Checking the status of a transfer

1. In transfer_check.py, fill in the Transfer Job json template with relevante values.
   Use the Job ID you recorded earlier.
1. Run with `python transfer_check.py`
