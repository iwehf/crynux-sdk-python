from enum import Enum, IntEnum
from typing import List

from pydantic import BaseModel


class TaskType(IntEnum):
    SD = 0
    LLM = 1

class ChainTask(BaseModel):
    id: int
    task_type: TaskType
    creator: str
    task_hash: bytes
    data_hash: bytes
    vram_limit: int
    is_success: bool
    selected_nodes: List[str]
    commitments: List[bytes]
    nonces: List[bytes]
    commitment_submit_rounds: List[int]
    results: List[bytes]
    result_disclosed_rounds: List[int]
    result_node: str
    aborted: bool
    timeout: int
