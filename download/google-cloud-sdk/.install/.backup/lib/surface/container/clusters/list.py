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
"""List clusters command."""
from googlecloudsdk.api_lib.container import util
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from surface.container import UPGRADE_TEXT
from googlecloudsdk.third_party.apitools.base.py import exceptions as apitools_exceptions
from googlecloudsdk.third_party.py27 import py27_collections as collections


class List(base.Command):
  """List existing clusters for running containers."""

  @staticmethod
  def Args(parser):
    """Register flags for this command.

    Args:
      parser: An argparse.ArgumentParser-like object. It is mocked out in order
          to capture some information, but behaves like an ArgumentParser.
    """
    pass

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      Some value that we want to have printed later.
    """
    adapter = self.context['api_adapter']

    project = properties.VALUES.core.project.Get(required=True)
    zone = None
    if args.zone:
      zone = adapter.registry.Parse(args.zone, collection='compute.zones').zone

    try:
      clusters = adapter.ListClusters(project, zone)

      upgrade_available = False
      text = None
      list_info = collections.namedtuple('list_info', ['clusters', 'text'])

      for c in clusters.clusters:
        if c.currentNodeVersion != c.currentMasterVersion:
          c.currentNodeVersion += ' *'
          upgrade_available = True
      if upgrade_available:
        text = UPGRADE_TEXT.format(name='NAME')
      return list_info(clusters, text)
    except apitools_exceptions.HttpError as error:
      raise exceptions.HttpException(util.GetError(error))

  def Display(self, args, result):
    """This method is called to print the result of the Run() method.

    Args:
      args: The arguments that command was run with.
      result: The value returned from the Run() method.
    """
    self.context['api_adapter'].PrintClusters(result.clusters.clusters)
    if result.text:
      log.status.Print(result.text)
