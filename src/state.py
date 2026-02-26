import operator
from typing import Annotated, List, Dict, Optional, Any
from typing_extensions import TypedDict


# 1. Define the Schema for a Single Compliance Result
class ComplianceIssue(TypedDict):
    category: str
    description: str
    severity: str
    timestamp: Optional[str]


# 2. Define the Global Graph State
class VideoAuditState(TypedDict):
    """
    Defines the data schema for the LangGraph execution context.
    """

    # --- Input Parameters ---
    video_url: str
    video_id: str

    # --- Ingestion & Extraction Data ---
    local_file_path: Optional[str]
    video_metadata: Dict[str, Any]
    transcript: Optional[str]
    ocr_text: List[str]

    # --- Analysis Output ---
    compliance_results: Annotated[List[ComplianceIssue], operator.add]

    # --- Final Deliverables ---
    final_status: str
    final_report: str

    # --- System Observability ---
    errors: Annotated[List[str], operator.add]
