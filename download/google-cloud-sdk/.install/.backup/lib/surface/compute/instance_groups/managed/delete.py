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
"""Command for deleting managed instance group."""
from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.compute import managed_instance_groups_utils


class Delete(base_classes.ZonalDeleter):
  """Delete Google Compute Engine managed instance group."""

  @property
  def service(self):
    return self.compute.instanceGroupManagers

  @property
  def resource_type(self):
    return 'instanceGroupManagers'

  def _DeleteAutoscalersRequests(self, mig_requests):
    migs = [(request.instanceGroupManager, 'zone', request.zone)
            for request in mig_requests]
    zones = sorted(set(zip(*migs)[2]))
    autoscalers_to_delete = managed_instance_groups_utils.AutoscalersForMigs(
        migs=migs,
        autoscalers=managed_instance_groups_utils.AutoscalersForZones(
            zones=zones,
            project=self.project,
            compute=self.compute,
            http=self.http,
            batch_url=self.batch_url),
        project=self.project)
    requests = []
    for autoscaler in autoscalers_to_delete:
      as_ref = self.CreateZonalReference(autoscaler.name, autoscaler.zone)
      request = self.messages.ComputeAutoscalersDeleteRequest(
          project=self.project)
      request.zone = as_ref.zone
      request.autoscaler = as_ref.Name()
      requests.append(request)
    return requests

  def Run(self, args):
    # CreateRequests() propmpts user to confirm deletion so it should be a first
    # thing to be executed in this function.
    delete_managed_instance_groups_requests = self.CreateRequests(args)
    super(Delete, self).Run(
        args,
        request_protobufs=self._DeleteAutoscalersRequests(
            mig_requests=delete_managed_instance_groups_requests),
        service=self.compute.autoscalers)
    super(Delete, self).Run(
        args, request_protobufs=delete_managed_instance_groups_requests)


Delete.detailed_help = {
    'brief': 'Delete Google Compute Engine managed instance groups',
    'DESCRIPTION': """\
        *{command}* deletes one or more Google Compute Engine managed instance
groups.
        """,
}
