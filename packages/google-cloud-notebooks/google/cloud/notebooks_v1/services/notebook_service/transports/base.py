# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.notebooks_v1 import gapic_version as package_version
from google.cloud.notebooks_v1.types import (
    environment,
    execution,
    instance,
    schedule,
    service,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


class NotebookServiceTransport(abc.ABC):
    """Abstract transport class for NotebookService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "notebooks.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'notebooks.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )
        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_instances: gapic_v1.method.wrap_method(
                self.list_instances,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_instance: gapic_v1.method.wrap_method(
                self.get_instance,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_instance: gapic_v1.method.wrap_method(
                self.create_instance,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.register_instance: gapic_v1.method.wrap_method(
                self.register_instance,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.set_instance_accelerator: gapic_v1.method.wrap_method(
                self.set_instance_accelerator,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.set_instance_machine_type: gapic_v1.method.wrap_method(
                self.set_instance_machine_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_instance_config: gapic_v1.method.wrap_method(
                self.update_instance_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_shielded_instance_config: gapic_v1.method.wrap_method(
                self.update_shielded_instance_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.set_instance_labels: gapic_v1.method.wrap_method(
                self.set_instance_labels,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_instance_metadata_items: gapic_v1.method.wrap_method(
                self.update_instance_metadata_items,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_instance: gapic_v1.method.wrap_method(
                self.delete_instance,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.start_instance: gapic_v1.method.wrap_method(
                self.start_instance,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.stop_instance: gapic_v1.method.wrap_method(
                self.stop_instance,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.reset_instance: gapic_v1.method.wrap_method(
                self.reset_instance,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.report_instance_info: gapic_v1.method.wrap_method(
                self.report_instance_info,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.is_instance_upgradeable: gapic_v1.method.wrap_method(
                self.is_instance_upgradeable,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_instance_health: gapic_v1.method.wrap_method(
                self.get_instance_health,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.upgrade_instance: gapic_v1.method.wrap_method(
                self.upgrade_instance,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.rollback_instance: gapic_v1.method.wrap_method(
                self.rollback_instance,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.diagnose_instance: gapic_v1.method.wrap_method(
                self.diagnose_instance,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.upgrade_instance_internal: gapic_v1.method.wrap_method(
                self.upgrade_instance_internal,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_environments: gapic_v1.method.wrap_method(
                self.list_environments,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_environment: gapic_v1.method.wrap_method(
                self.get_environment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_environment: gapic_v1.method.wrap_method(
                self.create_environment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_environment: gapic_v1.method.wrap_method(
                self.delete_environment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_schedules: gapic_v1.method.wrap_method(
                self.list_schedules,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_schedule: gapic_v1.method.wrap_method(
                self.get_schedule,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_schedule: gapic_v1.method.wrap_method(
                self.delete_schedule,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_schedule: gapic_v1.method.wrap_method(
                self.create_schedule,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.trigger_schedule: gapic_v1.method.wrap_method(
                self.trigger_schedule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_executions: gapic_v1.method.wrap_method(
                self.list_executions,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_execution: gapic_v1.method.wrap_method(
                self.get_execution,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_execution: gapic_v1.method.wrap_method(
                self.delete_execution,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_execution: gapic_v1.method.wrap_method(
                self.create_execution,
                default_timeout=60.0,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_instances(
        self,
    ) -> Callable[
        [service.ListInstancesRequest],
        Union[service.ListInstancesResponse, Awaitable[service.ListInstancesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_instance(
        self,
    ) -> Callable[
        [service.GetInstanceRequest],
        Union[instance.Instance, Awaitable[instance.Instance]],
    ]:
        raise NotImplementedError()

    @property
    def create_instance(
        self,
    ) -> Callable[
        [service.CreateInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def register_instance(
        self,
    ) -> Callable[
        [service.RegisterInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_instance_accelerator(
        self,
    ) -> Callable[
        [service.SetInstanceAcceleratorRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_instance_machine_type(
        self,
    ) -> Callable[
        [service.SetInstanceMachineTypeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_instance_config(
        self,
    ) -> Callable[
        [service.UpdateInstanceConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_shielded_instance_config(
        self,
    ) -> Callable[
        [service.UpdateShieldedInstanceConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_instance_labels(
        self,
    ) -> Callable[
        [service.SetInstanceLabelsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_instance_metadata_items(
        self,
    ) -> Callable[
        [service.UpdateInstanceMetadataItemsRequest],
        Union[
            service.UpdateInstanceMetadataItemsResponse,
            Awaitable[service.UpdateInstanceMetadataItemsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_instance(
        self,
    ) -> Callable[
        [service.DeleteInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_instance(
        self,
    ) -> Callable[
        [service.StartInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def stop_instance(
        self,
    ) -> Callable[
        [service.StopInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def reset_instance(
        self,
    ) -> Callable[
        [service.ResetInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def report_instance_info(
        self,
    ) -> Callable[
        [service.ReportInstanceInfoRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def is_instance_upgradeable(
        self,
    ) -> Callable[
        [service.IsInstanceUpgradeableRequest],
        Union[
            service.IsInstanceUpgradeableResponse,
            Awaitable[service.IsInstanceUpgradeableResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_instance_health(
        self,
    ) -> Callable[
        [service.GetInstanceHealthRequest],
        Union[
            service.GetInstanceHealthResponse,
            Awaitable[service.GetInstanceHealthResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def upgrade_instance(
        self,
    ) -> Callable[
        [service.UpgradeInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def rollback_instance(
        self,
    ) -> Callable[
        [service.RollbackInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def diagnose_instance(
        self,
    ) -> Callable[
        [service.DiagnoseInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def upgrade_instance_internal(
        self,
    ) -> Callable[
        [service.UpgradeInstanceInternalRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_environments(
        self,
    ) -> Callable[
        [service.ListEnvironmentsRequest],
        Union[
            service.ListEnvironmentsResponse,
            Awaitable[service.ListEnvironmentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_environment(
        self,
    ) -> Callable[
        [service.GetEnvironmentRequest],
        Union[environment.Environment, Awaitable[environment.Environment]],
    ]:
        raise NotImplementedError()

    @property
    def create_environment(
        self,
    ) -> Callable[
        [service.CreateEnvironmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_environment(
        self,
    ) -> Callable[
        [service.DeleteEnvironmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_schedules(
        self,
    ) -> Callable[
        [service.ListSchedulesRequest],
        Union[service.ListSchedulesResponse, Awaitable[service.ListSchedulesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_schedule(
        self,
    ) -> Callable[
        [service.GetScheduleRequest],
        Union[schedule.Schedule, Awaitable[schedule.Schedule]],
    ]:
        raise NotImplementedError()

    @property
    def delete_schedule(
        self,
    ) -> Callable[
        [service.DeleteScheduleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_schedule(
        self,
    ) -> Callable[
        [service.CreateScheduleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def trigger_schedule(
        self,
    ) -> Callable[
        [service.TriggerScheduleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_executions(
        self,
    ) -> Callable[
        [service.ListExecutionsRequest],
        Union[
            service.ListExecutionsResponse, Awaitable[service.ListExecutionsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_execution(
        self,
    ) -> Callable[
        [service.GetExecutionRequest],
        Union[execution.Execution, Awaitable[execution.Execution]],
    ]:
        raise NotImplementedError()

    @property
    def delete_execution(
        self,
    ) -> Callable[
        [service.DeleteExecutionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_execution(
        self,
    ) -> Callable[
        [service.CreateExecutionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[
            operations_pb2.ListOperationsResponse,
            Awaitable[operations_pb2.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[[operations_pb2.CancelOperationRequest], None,]:
        raise NotImplementedError()

    @property
    def delete_operation(
        self,
    ) -> Callable[[operations_pb2.DeleteOperationRequest], None,]:
        raise NotImplementedError()

    @property
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Union[
            iam_policy_pb2.TestIamPermissionsResponse,
            Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("NotebookServiceTransport",)
