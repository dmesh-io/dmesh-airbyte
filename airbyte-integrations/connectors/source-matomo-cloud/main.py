#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_matomo_cloud import SourceMatomoCloud

if __name__ == "__main__":
    source = SourceMatomoCloud()
    launch(source, sys.argv[1:])
