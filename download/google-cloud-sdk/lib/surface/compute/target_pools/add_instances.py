# Copyright 2014 Google Inc. All Rights Reserved.
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
"""Command for adding instances to target pools."""

from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.compute import utils
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import exceptions as calliope_exceptions


class AddInstances(base_classes.NoOutputAsyncMutator):
  """Add instances to a target pool."""

  @staticmethod
  def Args(parser):
    parser.add_argument(
        '--instances',
        type=arg_parsers.ArgList(min_length=1),
        action=arg_parsers.FloatingListValuesCatcher(),
        help='Specifies a list of instances to add to the target pool.',
        completion_resource='compute.instances',
        metavar='INSTANCE',
        required=True)

    utils.AddZoneFlag(
        parser,
        resource_type='instances',
        operation_type='add to the target pool')

    parser.add_argument(
        'name',
        completion_resource='compute.targetPools',
        help='The name of the target pool to which to add the instances.')

  @property
  def service(self):
    return self.compute.targetPools

  @property
  def method(self):
    return 'AddInstance'

  @property
  def resource_type(self):
    return 'targetPools'

  def CreateRequests(self, args):
    instance_refs = self.CreateZonalReferences(
        args.instances, args.zone, resource_type='instances')

    instances = [
        self.messages.InstanceReference(instance=instance_ref.SelfLink())
        for instance_ref in instance_refs]

    unique_regions = set(utils.ZoneNameToRegionName(instance_ref.zone)
                         for instance_ref in instance_refs)

    # Check that all regions are the same.
    if len(unique_regions) > 1:
      raise calliope_exceptions.ToolException(
          'Instances must all be in the same region as the target pool.')

    target_pool_ref = self.CreateRegionalReference(
        args.name, unique_regions.pop(),
        resource_type='targetPools')

    request = self.messages.ComputeTargetPoolsAddInstanceRequest(
        region=target_pool_ref.region,
        project=self.project,
        targetPool=target_pool_ref.Name(),
        targetPoolsAddInstanceRequest=(
            self.messages.TargetPoolsAddInstanceRequest(instances=instances)))
    return [request]


AddInstances.detailed_help = {
    'brief': 'Add instances to a target pool',
    'DESCRIPTION': """\
        *{command}* is used to add one or more instances to a target pool.
        For more information on health checks and load balancing, see
        link:https://cloud.google.com/compute/docs/load-balancing-and-autoscaling/[].
        """,
}
