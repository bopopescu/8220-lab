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

"""The command to restore a backup of a Cloud SDK installation."""

from googlecloudsdk.calliope import base


class Restore(base.Command):
  """Restore the Cloud SDK installation to its previous state.

  This is an undo operation, which restores the Cloud SDK installation on the
  local workstation to the state it was in just before the most recent
  `{parent_command} update` or `{parent_command} remove` command. Only the
  state before the most recent such state is remembered, so it is impossible
  to restore the state that existed before the two most recent `update`
  commands, for example. A `restore` command does not undo a previous `restore`
  command.
  """

  @staticmethod
  def Args(_):
    pass

  def Run(self, unused_args):
    """Runs the list command."""
    self.group.update_manager.Restore()
