#!/usr/bin/env python

import create_client
import json
import logging

# Edit these values with desired parameters
PROJECT_ID = ''
JOB_ID = ''


def main():
    """Check the status of a transfer job"""
    logging.getLogger().setLevel(logging.DEBUG)
    transfer_service_client = create_client.create_transfer_client()

    result = transfer_service_client.transferOperations().list(
        name="transferOperations",
        filter=('{"project_id": "%s", '
                '"job_id": ["%s"] '
                '}' % (PROJECT_ID, JOB_ID))).execute()
    logging.info('Result of transferOperations/list: %s',
                 json.dumps(result, indent=4, sort_keys=True))

if __name__ == '__main__':
    main()
