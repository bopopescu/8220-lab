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

"""Common helper methods for Genomics commands."""

import json
import sys
from googlecloudsdk.api_lib import genomics as lib
from googlecloudsdk.api_lib.genomics.exceptions import GenomicsError
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core import resource_printer
from googlecloudsdk.third_party.apitools.base.py import exceptions as apitools_exceptions
from googlecloudsdk.third_party.apitools.base.py import extra_types


def ValidateLimitFlag(limit, flag_name='limit'):
  """Validates a limit flag value.

  Args:
    limit: the limit flag value to sanitize.
    flag_name: the name of the limit flag - defaults to limit
  Raises:
    GenomicsError: if the provided limit flag value is negative
  """
  if limit is None:
    return

  if limit < 0:
    raise GenomicsError(
        '--{0} must be a non-negative integer; received: {1}'
        .format(flag_name, limit))


def InfoValuesToAPI(values):
  """Converts a list of strings to the API JsonValue equivalent.

  Args:
    values: the string values to be converted
  Returns:
    An equivalent list of JsonValue strings
  """
  return [extra_types.JsonValue(string_value=v) for v in values]


def InfoValuesFromAPI(values):
  """Converts a list of strings to an API JsonValue equivalent.

  Args:
    values: the list of JsonValue strings to be converted
  Returns:
    An equivalent list of strings
  """
  return [v.string_value for v in values]


def PrettyPrint(resource, print_format='json'):
  """Prints the given resource."""
  resource_printer.Print(
      resources=[resource],
      print_format=print_format,
      out=log.out)


def GetError(error, verbose=False):
  """Returns a ready-to-print string representation from the http response.

  Args:
    error: A string representing the raw json of the Http error response.
    verbose: Whether or not to print verbose messages [default false]

  Returns:
    A ready-to-print string representation of the error.
  """
  data = json.loads(error.content)
  if verbose:
    PrettyPrint(data)
  code = data['error']['code']
  message = data['error']['message']
  return 'ResponseError: code={0}, message={1}'.format(code, message)


def GetErrorMessage(error):
  content_obj = json.loads(error.content)
  return content_obj.get('error', {}).get('message', '')


def ReraiseHttpExceptionPager(pager, rewrite_fn=None):
  """Wraps an HTTP paginator and converts errors to be gcloud-friendly.

  Args:
    pager: A list or generator of a response type.
    rewrite_fn: A function that rewrites the returned message.
        If 'None', no rewriting will occur.

  Returns:
    A generator which raises gcloud-friendly errors, if any.
  """

  try:
    for result in pager:
      yield result
  except apitools_exceptions.HttpError as error:
    msg = GetErrorMessage(error)
    if rewrite_fn:
      msg = rewrite_fn(msg)
    unused_type, unused_value, traceback = sys.exc_info()
    raise exceptions.HttpException, msg, traceback


def ReraiseHttpException(foo):
  def Func(*args, **kwargs):
    try:
      return foo(*args, **kwargs)
    except apitools_exceptions.HttpError as error:
      msg = GetErrorMessage(error)
      unused_type, unused_value, traceback = sys.exc_info()
      raise exceptions.HttpException, msg, traceback
  return Func


@ReraiseHttpException
def GetDataset(context, dataset_id):
  apitools_client = context[lib.GENOMICS_APITOOLS_CLIENT_KEY]
  genomics_messages = context[lib.GENOMICS_MESSAGES_MODULE_KEY]

  request = genomics_messages.GenomicsDatasetsGetRequest(
      datasetId=str(dataset_id),
  )

  return apitools_client.datasets.Get(request)


@ReraiseHttpException
def GetCallSet(context, call_set_id):
  apitools_client = context[lib.GENOMICS_APITOOLS_CLIENT_KEY]
  genomics_messages = context[lib.GENOMICS_MESSAGES_MODULE_KEY]

  request = genomics_messages.GenomicsCallsetsGetRequest(
      callSetId=str(call_set_id),
  )

  return apitools_client.callsets.Get(request)


def GetProjectId():
  return properties.VALUES.core.project.Get(required=True)
