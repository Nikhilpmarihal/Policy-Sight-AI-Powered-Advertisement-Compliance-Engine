import os           # Access environment variables (like API keys)
import logging      # Python's built-in logging system
from azure.monitor.opentelemetry import configure_azure_monitor  


# ========== CREATE A DEDICATED LOGGER ==========
logger = logging.getLogger("policy-sight-tracer")


def setup_telemetry():
    """
    Initializes Azure Monitor OpenTelemetry.
    """

    # ========== STEP 1: RETRIEVE CONNECTION STRING ==========
    connection_string = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")
    
    # ========== STEP 2: CHECK IF CONFIGURED ==========
    if not connection_string:
        logger.warning("No Instrumentation Key found. Telemetry is DISABLED.")
        return  

    # ========== STEP 3: CONFIGURE AZURE MONITOR ==========
    try:
        configure_azure_monitor(
            connection_string=connection_string,
            logger_name="policy-sight-tracer"
        )
        
        logger.info(" Azure Monitor Tracking Enabled & Connected!")
        
    except Exception as e:
        logger.error(f"Failed to initialize Azure Monitor: {e}")
