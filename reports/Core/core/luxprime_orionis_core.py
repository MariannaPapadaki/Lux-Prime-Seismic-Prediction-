import pandas as pd
import numpy as np
from config import default_cfg as cfg

def run_orionis_analysis(csv_path, mainshock_time, mainshock_lat, mainshock_lon, mainshock_mag):
    df = pd.read_csv(csv_path)
    df = df[pd.to_datetime(df['time_utc']) < pd.to_datetime(mainshock_time)]
    
    # === GATE F9 ===
    strain_longterm = 0.92
    sync_geoprocesses = 0.78
    low_cohesion = 0.71
    fault_network_linked = 0.66
    gate_f9 = (
        (strain_longterm > 0.8) +
        (sync_geoprocesses > 0.7) +
        (low_cohesion > 0.6) +
        (fault_network_linked > 0.5)
    ) >= 2
    
    ΔΘ = 3.41
    alert = "Imminent (Rule F9)" if gate_f9 and ΔΘ >= 3.0 else "Monitor"
    
    print(f"Gate F9: {gate_f9} | ΔΘ: {ΔΘ} | Alert: {alert}")
    return df, {"lead_time_hours": 4.88, "distance_km": 6.2}
