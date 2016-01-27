# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Update cluster command."""
from googlecloudsdk.api_lib.container import api_adapter
from googlecloudsdk.api_lib.container import util
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.third_party.apitools.base.py import exceptions as apitools_exceptions


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Update(base.Command):
  """Update cluster settings for an existing container cluster."""

  @staticmethod
  def Args(parser):
    """Register flags for this command.

    Args:
      parser: An argparse.ArgumentParser-like object. It is mocked out in order
          to capture some information, but behaves like an ArgumentParser.
    """
    parser.add_argument(
        'name',
        metavar='NAME',
        help='The name of the cluster to update.')
    parser.add_argument(
        '--monitoring-service',
        dest='monitoring_service',
        required=True,
        help='The monitoring service to use for the cluster. Options '
        'are: "monitoring.googleapis.com" (the Google Cloud Monitoring '
        'service),  "none" (no metrics will be exported from the cluster)')
    parser.add_argument(
        '--wait',
        action='store_true',
        default=True,
        help='Poll the operation for completion after issuing an update '
        'request.')

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      Some value that we want to have printed later.
    """
    adapter = self.context['api_adapter']

    cluster_ref = adapter.ParseCluster(args.name)

    # Make sure it exists (will raise appropriate error if not)
    adapter.GetCluster(cluster_ref)

    options = api_adapter.UpdateClusterOptions(
        update_cluster=True,
        monitoring_service=args.monitoring_service)

    try:
      op_ref = adapter.UpdateCluster(cluster_ref, options)
    except apitools_exceptions.HttpError as error:
      raise exceptions.HttpException(util.GetError(error))

    if args.wait:
      adapter.WaitForOperation(
          op_ref, 'Updating {0}'.format(cluster_ref.clusterId))

      log.UpdatedResource(cluster_ref)
