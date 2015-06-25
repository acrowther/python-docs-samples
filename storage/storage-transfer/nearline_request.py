#!/usr/bin/env python

import create_client
import json
import logging


def main():
    """Create a daily transfer between GCS and nearline for old files"""
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
        "startTimeOfDay": {
            "hours": 1,
            "minutes": 1
        }
    },
    "transferSpec": {
        "gcsDataSource": {
            "bucketName": ""
        },
        "gcsDataSink": {
            "bucketName": ""
        },
        "objectConditions": {
            "minTimeElapsedSinceLastModification": "2592000s"
        },
        "transferOptions": {
            "deleteObjectsFromSourceAfterTransfer": true
        }
    }
}
'''
    result = transfer_service_client.transferJobs().create(
        body=json.loads(transfer_job)).execute()
    logging.info('Returned transferJob: %s', json.dumps(result, indent=4))

if __name__ == '__main__':
    main()
