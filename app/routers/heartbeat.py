from fastapi import APIRouter, Response, status
from pyModbusTCP.client import ModbusClient

from app.services.config import get_settings

router = APIRouter()
settings = get_settings()

primary_client = ModbusClient(
    host=settings.modbus_tcp_host,
    port=settings.modbus_tcp_port1,
    auto_open=True,
    auto_close=True,
)


secondary_client = ModbusClient(
    host=settings.modbus_tcp_host,
    port=settings.modbus_tcp_port2,
    auto_open=True,
    auto_close=True,
)


@router.get("/heartbeat")
async def heartbeat(id: int, phase: int, door_status: int, response: Response):
    device_id: int = id
    current_phase: int = 0 if phase == 0 else 65535
    door_status_id = door_status
    door_sensor = 0
    if door_status_id == 0:
        door_sensor = 0
    elif door_status_id == 1:
        door_sensor = 4369
    elif door_status_id == 2:
        door_sensor = 65535

    if device_id == 1:
        write_success = primary_client.write_multiple_registers(
            0, [current_phase, door_sensor]
        )
    elif device_id == 2:
        write_success = secondary_client.write_multiple_registers(
            0, [current_phase, door_sensor]
        )

    if write_success:
        response.status_code = status.HTTP_200_OK
        return {"message": "OK"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "PLC writing error"}
