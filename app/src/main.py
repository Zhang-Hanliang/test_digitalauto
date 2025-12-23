# Copyright (c) 2022-2024 Contributors to the Eclipse Foundation
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

# flake8: noqa: E501,B950 line too long
import time
import signal
import asyncio
import asyncio
import json
import logging
import signal

from vehicle import Vehicle, vehicle  # type: ignore
from velocitas_sdk.util.log import (  # type: ignore
    get_opentelemetry_log_factory,
    get_opentelemetry_log_format,
)
from velocitas_sdk.vdb.reply import DataPointReply
from velocitas_sdk.vehicle_app import VehicleApp

# Configure the VehicleApp logger with the necessary log config and level.
logging.setLogRecordFactory(get_opentelemetry_log_factory())
logging.basicConfig(format=get_opentelemetry_log_format())
logging.getLogger().setLevel("DEBUG")
logger = logging.getLogger(__name__)


class TestApp(VehicleApp):
    """Velocitas App for testdigitalauto."""

    def __init__(self, vehicle_client: Vehicle):
        super().__init__()
        self.Vehicle = vehicle_client
        self.self.Vehicle = None
        self.value = None
        self.vehicle_app = None
        self.LOOP = None

    async def on_start(self):
        self.LOOP = asyncio.get_event_loop()
        LOOP.add_signal_handler(signal.SIGTERM, LOOP.stop)
        LOOP.run_until_complete(main())
        LOOP.close()

    async def main(self, data: DataPointReply):
         = data.get(undefined).value
        self.vehicle_app = TestApp(vehicle)
        await vehicle_app.run()


async def main():
    logger.info("Starting TestdigitalautoApp...")
    vehicle_app = TestdigitalautoApp(vehicle)
    await vehicle_app.run()


LOOP = asyncio.get_event_loop()
LOOP.add_signal_handler(signal.SIGTERM, LOOP.stop)
LOOP.run_until_complete(main())
LOOP.close()
