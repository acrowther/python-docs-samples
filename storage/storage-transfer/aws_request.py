#!/usr/bin/env python

import create_client
import json
import logging


def main():
    """Create a one-off transfer between AWS S3 and GCS"""
    logging.getLogger().setLevel(logging.DEBUG)
    transfer_service_client = create_client.create_transfer_client()

    # Edit this template with desired parameters
    # US Pacific Time Zone
    transfer_job = '''
{
    "jobDescription": "",
    "jobState": "ENABLED",
    "projectId": "",
    "schedule": {
        "scheduleStartDate": {
            "day": 1,
            "month": 1,
            "year": 2015
        },
        "scheduleEndDate": {
            "day": 1,
            "month": 1,
            "year": 2015
        },
        "startTimeOfDay": {
            "hours": 0,
            "minutes": 0
        }
    },
    "transferSpec": {
        "awsS3DataSource": {
            "bucketName": "",
            "awsAccessKey": {
                "accessKeyId": "",
                "secretAccessKey": ""
            }
        },
        "gcsDataSink": {
            "bucketName": ""
        }
    }
}
'''
    result = transfer_service_client.transferJobs().create(
        body=json.loads(transfer_job)).execute()
    logging.info('Returned transferJob: %s', json.dumps(result, indent=4))

if __name__ == '__main__':
    main()
