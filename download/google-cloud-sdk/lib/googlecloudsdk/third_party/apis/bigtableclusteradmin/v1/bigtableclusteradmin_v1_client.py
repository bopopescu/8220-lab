"""Generated client library for bigtableclusteradmin version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from googlecloudsdk.third_party.apitools.base.py import base_api
from googlecloudsdk.third_party.apis.bigtableclusteradmin.v1 import bigtableclusteradmin_v1_messages as messages


class BigtableclusteradminV1(base_api.BaseApiClient):
  """Generated client library for service bigtableclusteradmin version v1."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'bigtableclusteradmin'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-platform.read-only']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'BigtableclusteradminV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new bigtableclusteradmin handle."""
    url = url or u'https://bigtableclusteradmin.googleapis.com/v1/'
    super(BigtableclusteradminV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.operations = self.OperationsService(self)
    self.projects_aggregated_clusters = self.ProjectsAggregatedClustersService(self)
    self.projects_aggregated = self.ProjectsAggregatedService(self)
    self.projects_zones_clusters = self.ProjectsZonesClustersService(self)
    self.projects_zones = self.ProjectsZonesService(self)
    self.projects = self.ProjectsService(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(BigtableclusteradminV1.OperationsService, self).__init__(client)
      self._method_configs = {
          'Cancel': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'bigtableclusteradmin.operations.cancel',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'{+name}:cancel',
              request_field=u'cancelOperationRequest',
              request_type_name=u'BigtableclusteradminOperationsCancelRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'bigtableclusteradmin.operations.delete',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'{+name}',
              request_field='',
              request_type_name=u'BigtableclusteradminOperationsDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigtableclusteradmin.operations.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'{+name}',
              request_field='',
              request_type_name=u'BigtableclusteradminOperationsGetRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigtableclusteradmin.operations.list',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'filter', u'pageSize', u'pageToken'],
              relative_path=u'{name}',
              request_field='',
              request_type_name=u'BigtableclusteradminOperationsListRequest',
              response_type_name=u'ListOperationsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use [Operations.GetOperation][google.longrunning.Operations.GetOperation] or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation.

      Args:
        request: (BigtableclusteradminOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (BigtableclusteradminOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (BigtableclusteradminOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding below allows API services to override the binding to use different resource name schemes, such as `users/*/operations`.

      Args:
        request: (BigtableclusteradminOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsAggregatedClustersService(base_api.BaseApiService):
    """Service class for the projects_aggregated_clusters resource."""

    _NAME = u'projects_aggregated_clusters'

    def __init__(self, client):
      super(BigtableclusteradminV1.ProjectsAggregatedClustersService, self).__init__(client)
      self._method_configs = {
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigtableclusteradmin.projects.aggregated.clusters.list',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'{+name}/aggregated/clusters',
              request_field='',
              request_type_name=u'BigtableclusteradminProjectsAggregatedClustersListRequest',
              response_type_name=u'ListClustersResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists all clusters in the given project, along with any zones for which cluster information could not be retrieved.

      Args:
        request: (BigtableclusteradminProjectsAggregatedClustersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListClustersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsAggregatedService(base_api.BaseApiService):
    """Service class for the projects_aggregated resource."""

    _NAME = u'projects_aggregated'

    def __init__(self, client):
      super(BigtableclusteradminV1.ProjectsAggregatedService, self).__init__(client)
      self._method_configs = {
          }

      self._upload_configs = {
          }

  class ProjectsZonesClustersService(base_api.BaseApiService):
    """Service class for the projects_zones_clusters resource."""

    _NAME = u'projects_zones_clusters'

    def __init__(self, client):
      super(BigtableclusteradminV1.ProjectsZonesClustersService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'bigtableclusteradmin.projects.zones.clusters.create',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'{+name}/clusters',
              request_field='<request>',
              request_type_name=u'CreateClusterRequest',
              response_type_name=u'Cluster',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'bigtableclusteradmin.projects.zones.clusters.delete',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'{+name}',
              request_field='',
              request_type_name=u'BigtableclusteradminProjectsZonesClustersDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigtableclusteradmin.projects.zones.clusters.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'{+name}',
              request_field='',
              request_type_name=u'BigtableclusteradminProjectsZonesClustersGetRequest',
              response_type_name=u'Cluster',
              supports_download=False,
          ),
          'Patch': base_api.ApiMethodInfo(
              http_method=u'PATCH',
              method_id=u'bigtableclusteradmin.projects.zones.clusters.patch',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'{+name}',
              request_field='<request>',
              request_type_name=u'Cluster',
              response_type_name=u'Cluster',
              supports_download=False,
          ),
          'Undelete': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'bigtableclusteradmin.projects.zones.clusters.undelete',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'{+name}:undelete',
              request_field='',
              request_type_name=u'BigtableclusteradminProjectsZonesClustersUndeleteRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'bigtableclusteradmin.projects.zones.clusters.update',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'{+name}',
              request_field='<request>',
              request_type_name=u'Cluster',
              response_type_name=u'Cluster',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a cluster and begins preparing it to begin serving. The returned cluster embeds as its "current_operation" a long-running operation which can be used to track the progress of turning up the new cluster. Immediately upon completion of this request: * The cluster will be readable via the API, with all requested attributes but no allocated resources. Until completion of the embedded operation: * Cancelling the operation will render the cluster immediately unreadable via the API. * All other attempts to modify or delete the cluster will be rejected. Upon completion of the embedded operation: * Billing for all successfully-allocated resources will begin (some types may have lower than the requested levels). * New tables can be created in the cluster. * The cluster's allocated resource levels will be readable via the API. The embedded operation's "metadata" field type is [CreateClusterMetadata][google.bigtable.admin.cluster.v1.CreateClusterMetadata] The embedded operation's "response" field type is [Cluster][google.bigtable.admin.cluster.v1.Cluster], if successful.

      Args:
        request: (CreateClusterRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Cluster) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Marks a cluster and all of its tables for permanent deletion in 7 days. Immediately upon completion of the request: * Billing will cease for all of the cluster's reserved resources. * The cluster's "delete_time" field will be set 7 days in the future. Soon afterward: * All tables within the cluster will become unavailable. Prior to the cluster's "delete_time": * The cluster can be recovered with a call to UndeleteCluster. * All other attempts to modify or delete the cluster will be rejected. At the cluster's "delete_time": * The cluster and *all of its tables* will immediately and irrevocably disappear from the API, and their data will be permanently deleted.

      Args:
        request: (BigtableclusteradminProjectsZonesClustersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets information about a particular cluster.

      Args:
        request: (BigtableclusteradminProjectsZonesClustersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Cluster) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Patch(self, request, global_params=None):
      """Updates a cluster, and begins allocating or releasing resources as requested. The returned cluster embeds as its "current_operation" a long-running operation which can be used to track the progress of updating the cluster. Immediately upon completion of this request: * For resource types where a decrease in the cluster's allocation has been requested, billing will be based on the newly-requested level. Until completion of the embedded operation: * Cancelling the operation will set its metadata's "cancelled_at_time", and begin restoring resources to their pre-request values. The operation is guaranteed to succeed at undoing all resource changes, after which point it will terminate with a CANCELLED status. * All other attempts to modify or delete the cluster will be rejected. * Reading the cluster via the API will continue to give the pre-request resource levels. Upon completion of the embedded operation: * Billing will begin for all successfully-allocated resources (some types may have lower than the requested levels). * All newly-reserved resources will be available for serving the cluster's tables. * The cluster's new resource levels will be readable via the API. [UpdateClusterMetadata][google.bigtable.admin.cluster.v1.UpdateClusterMetadata] The embedded operation's "response" field type is [Cluster][google.bigtable.admin.cluster.v1.Cluster], if successful. This method supports patch semantics.

      Args:
        request: (Cluster) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Cluster) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Undelete(self, request, global_params=None):
      """Cancels the scheduled deletion of an cluster and begins preparing it to resume serving. The returned operation will also be embedded as the cluster's "current_operation". Immediately upon completion of this request: * The cluster's "delete_time" field will be unset, protecting it from automatic deletion. Until completion of the returned operation: * The operation cannot be cancelled. Upon completion of the returned operation: * Billing for the cluster's resources will resume. * All tables within the cluster will be available. [UndeleteClusterMetadata][google.bigtable.admin.cluster.v1.UndeleteClusterMetadata] The embedded operation's "response" field type is [Cluster][google.bigtable.admin.cluster.v1.Cluster], if successful.

      Args:
        request: (BigtableclusteradminProjectsZonesClustersUndeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Undelete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Updates a cluster, and begins allocating or releasing resources as requested. The returned cluster embeds as its "current_operation" a long-running operation which can be used to track the progress of updating the cluster. Immediately upon completion of this request: * For resource types where a decrease in the cluster's allocation has been requested, billing will be based on the newly-requested level. Until completion of the embedded operation: * Cancelling the operation will set its metadata's "cancelled_at_time", and begin restoring resources to their pre-request values. The operation is guaranteed to succeed at undoing all resource changes, after which point it will terminate with a CANCELLED status. * All other attempts to modify or delete the cluster will be rejected. * Reading the cluster via the API will continue to give the pre-request resource levels. Upon completion of the embedded operation: * Billing will begin for all successfully-allocated resources (some types may have lower than the requested levels). * All newly-reserved resources will be available for serving the cluster's tables. * The cluster's new resource levels will be readable via the API. [UpdateClusterMetadata][google.bigtable.admin.cluster.v1.UpdateClusterMetadata] The embedded operation's "response" field type is [Cluster][google.bigtable.admin.cluster.v1.Cluster], if successful.

      Args:
        request: (Cluster) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Cluster) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsZonesService(base_api.BaseApiService):
    """Service class for the projects_zones resource."""

    _NAME = u'projects_zones'

    def __init__(self, client):
      super(BigtableclusteradminV1.ProjectsZonesService, self).__init__(client)
      self._method_configs = {
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'bigtableclusteradmin.projects.zones.list',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'{+name}/zones',
              request_field='',
              request_type_name=u'BigtableclusteradminProjectsZonesListRequest',
              response_type_name=u'ListZonesResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists the supported zones for the given project.

      Args:
        request: (BigtableclusteradminProjectsZonesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListZonesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(BigtableclusteradminV1.ProjectsService, self).__init__(client)
      self._method_configs = {
          }

      self._upload_configs = {
          }
