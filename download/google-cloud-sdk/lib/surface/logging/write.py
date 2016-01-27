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

"""'logging write' command."""

import datetime
from googlecloudsdk.api_lib.logging import util
from googlecloudsdk.calliope import base
from googlecloudsdk.core import log
from googlecloudsdk.core import properties


class Write(base.Command):
  """Writes a log entry."""

  SEVERITY_ENUM = ('DEFAULT', 'DEBUG', 'INFO', 'NOTICE', 'WARNING',
                   'ERROR', 'CRITICAL', 'ALERT', 'EMERGENCY')

  PAYLOAD_TYPE = ('text', 'struct')

  @staticmethod
  def Args(parser):
    """Register flags for this command."""
    parser.add_argument(
        'log_name', help=('The name of the log where the log entry will '
                          'be written.'))
    parser.add_argument(
        'message', help=('The message to put in the log entry. It can be '
                         'JSON if you include --payload-type=struct.'))
    parser.add_argument(
        '--payload-type', help='Type of the log entry message: (text|struct).',
        choices=Write.PAYLOAD_TYPE, default='text')
    parser.add_argument(
        '--severity', required=False,
        help=('Severity level of the log entry: '
              '(DEFAULT|DEBUG|INFO|NOTICE|WARNING|ERROR|CRITICAL|'
              'ALERT|EMERGENCY).'),
        choices=Write.SEVERITY_ENUM, default='DEFAULT')

  @util.HandleHttpError
  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.
    """
    client = self.context['logging_client_v1beta3']
    messages = self.context['logging_messages_v1beta3']
    project = properties.VALUES.core.project.Get(required=True)

    severity_value = getattr(messages.LogEntryMetadata.SeverityValueValuesEnum,
                             args.severity.upper())

    labels = messages.LogEntryMetadata.LabelsValue()
    labels.additionalProperties = [
        messages.LogEntryMetadata.LabelsValue.AdditionalProperty(
            key='compute.googleapis.com/resource_type',
            value='instance'),
        messages.LogEntryMetadata.LabelsValue.AdditionalProperty(
            key='compute.googleapis.com/resource_id',
            value='sent with gcloud'),
    ]

    meta = messages.LogEntryMetadata(
        timestamp=util.FormatTimestamp(datetime.datetime.utcnow()),
        severity=severity_value,
        serviceName='compute.googleapis.com',
        labels=labels)
    entry = messages.LogEntry(metadata=meta)

    if args.payload_type == 'struct':
      json_object = util.ConvertToJsonObject(args.message)
      struct = messages.LogEntry.StructPayloadValue()
      # Protobufs in Python do strict type-checking. We have to change the
      # type from JsonObject.Property to StructPayloadValue.AdditionalProperty
      # even though both types have the same fields (key, value).
      struct.additionalProperties = [
          messages.LogEntry.StructPayloadValue.AdditionalProperty(
              key=json_property.key,
              value=json_property.value)
          for json_property in json_object.properties
      ]
      entry.structPayload = struct
    else:
      entry.textPayload = args.message

    request = messages.WriteLogEntriesRequest(entries=[entry])

    client.projects_logs_entries.Write(
        messages.LoggingProjectsLogsEntriesWriteRequest(
            projectsId=project, logsId=args.log_name,
            writeLogEntriesRequest=request))
    log.status.write('Created log entry.\n')


Write.detailed_help = {
    'DESCRIPTION': """\
        {index}
        If the destination log does not exist, it will be created.
        All log entries written with this command are considered to be from
        the "compute.googleapis.com" log service (Google Compute Engine).
        The log entries will be listed in the Logs Viewer under that service.
    """,
    'EXAMPLES': """\
        To create a log entry in a given log, run:

          $ {command} LOG_NAME "A simple entry"

        To create a high severity log entry, run:

          $ {command} LOG_NAME "Urgent message" --severity=alert

        To create a structured log, run:

          $ {command} LOG_NAME '{"key": "value"}' --payload-type=struct
    """,
}
