from pydantic import BaseModel
from typing import List, Dict, Any

class ToolCall(BaseModel):
    id: str
    function: Dict[str, Any]

class MCPRequest(BaseModel):
    tool_calls: List[ToolCall]