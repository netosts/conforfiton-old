# pylint: skip-file
from pydantic import BaseModel
from datetime import datetime


class NewNeuromuscular(BaseModel):
    
    pl_bench_press: int
    pl_direct_thread: int
    pl_pull_front: int
    pl_leg_press: int
    pl_knee_extension: int
    pl_knee_bending: int
    
    reps_bench_press: int
    reps_direct_thread: int
    reps_pull_front: int
    reps_leg_press: int
    reps_knee_extension: int
    reps_knee_bending: int
    
    rm_bench_press: float
    rm_direct_thread: float
    rm_pull_front: float
    rm_leg_press: float
    rm_knee_extension: float
    rm_knee_bending: float
    
    pontos_bench_press: int
    pontos_direct_thread: int
    pontos_pull_front: int
    pontos_leg_press: int
    pontos_knee_extension: int
    pontos_knee_bending: int
    
    total_pontos: int
    created_at: datetime
