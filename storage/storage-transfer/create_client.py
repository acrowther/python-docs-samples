#!/usr/bin/env python

import httplib2
import logging
from apiclient import discovery
from oauth2client.client import GoogleCredentials

CLOUD_SCOPES = 'https://www.googleapis.com/auth/cloud-platform'


def create_transfer_client(http=None):
    """Create a transfer client

    Create a transfer client using application default credentials. Currently
    uses a discovery doc but eventually should be discoverable.
    """
    logging.getLogger().setLevel(logging.DEBUG)
    with open('storagetransfer_v1.json', 'r') as discovery_doc_file:
            discover_doc = discovery_doc_file.read()
    credentials = GoogleCredentials.get_application_default()
    if credentials.create_scoped_required():
        credentials = credentials.create_scoped(CLOUD_SCOPES)
    if not http:
        http = httplib2.Http()
    credentials.authorize(http)
    return discovery.build_from_document(discover_doc, http=http)
