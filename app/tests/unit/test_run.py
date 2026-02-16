# Copyright (c) 2022-2026 Contributors to the Eclipse Foundation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

# skip B101

from unittest import mock

import pytest
from google.protobuf.timestamp_pb2 import Timestamp
from vehicle import vehicle  # type: ignore
from velocitas_sdk.vdb.types import TypedDataPointResult  # type: ignore
from velocitas_sdk.vehicle_app import VehicleApp  # type: ignore

MOCKED_SPEED = 42.5


def test_dummy():
    pass


@pytest.mark.asyncio
async def test_for_get_speed():
    """Test getting wheel speed from VSS v5 datapoint."""
    result = TypedDataPointResult("foo", MOCKED_SPEED, Timestamp(seconds=10, nanos=0))

    with mock.patch.object(
        vehicle.Chassis.Axle.Row1.Wheel.Left.Speed,
        "get",
        new_callable=mock.AsyncMock,
        return_value=result,
    ):
        current_speed = (await vehicle.Chassis.Axle.Row1.Wheel.Left.Speed.get()).value
        print(f"Received wheel speed: {current_speed}")
        assert current_speed == MOCKED_SPEED


@pytest.mark.asyncio
async def test_for_publish_to_topic():
    """Test MQTT event publishing."""
    with mock.patch.object(
        VehicleApp, "publish_mqtt_event", new_callable=mock.AsyncMock, return_value=-1
    ):
        response = await VehicleApp.publish_mqtt_event(
            str("sampleTopic"),  # type: ignore
            get_sample_response_data(),
        )

        print(f"Received response: {response}")
        assert response == -1


def get_sample_response_data():
    return {
        "result": {
            "message": f"""Current Wheel Speed = {MOCKED_SPEED}""",
        },
    }
