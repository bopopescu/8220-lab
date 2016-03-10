# Copyright 2013 Google Inc. All Rights Reserved.
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

"""Command to unset properties."""

from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions as c_exc
from googlecloudsdk.core import log
from googlecloudsdk.core import properties


DETAILED_HELP = {
    'DESCRIPTION': '{description}',
    'EXAMPLES': """\
        To unset the project property in the core section, run:

          $ {command} project

        To unset the zone property in the compute section, run:

          $ {command} compute/zone
        """,
    '+AVAILABLE PROPERTIES': properties.VALUES.GetHelpString(),
}


class Unset(base.Command):
  """Erase Google Cloud SDK properties.

  Unset a property to be as if it were never defined in the first place. You
  may optionally use the --scope flag to specify a configuration file to update.
  """

  detailed_help = DETAILED_HELP

  @staticmethod
  def Args(parser):
    """Adds args for this command."""
    property_arg = parser.add_argument(
        'property',
        metavar='SECTION/PROPERTY',
        help='The property to be unset. Note that SECTION/ is optional while '
        'referring to properties in the core section.')
    property_arg.completer = Unset.group_class.PropertiesCompleter

    scope_args = parser.add_mutually_exclusive_group()
    Unset.group_class.DEPRECATED_SCOPE_FLAG.AddToParser(scope_args)
    Unset.group_class.INSTALLATION_FLAG.AddToParser(scope_args)

  def Run(self, args):
    """Runs this command."""
    if args.scope:
      log.err.Print('The `--scope` flag is deprecated.  Please run `gcloud '
                    'help topic configurations` and `gcloud help config '
                    'unset` for more information.')

    prop = properties.FromString(args.property)
    if not prop:
      raise c_exc.InvalidArgumentException(
          'property', 'Must be in the form: [SECTION/]PROPERTY')
    properties.PersistProperty(
        prop, None, scope=Unset.group_class.RequestedScope(args))
