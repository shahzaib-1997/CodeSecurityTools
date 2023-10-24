import pytest
from datetime import time, timedelta
from src_code.main import attendance_on_time_in, attendance_on_time_out

def test_attendance_on_time_in_present():
    time_in = "08:00"
    result = attendance_on_time_in(time_in)
    assert result == "present"

def test_attendance_on_time_in_late():
    time_in = "13:00"
    result = attendance_on_time_in(time_in)
    assert result == "late"

def test_attendance_on_time_out_half_day():
    time_in = "08:00"
    time_out = "12:30"
    result = attendance_on_time_out(time_in, time_out)
    assert result == "half day"

def test_attendance_on_time_out_short():
    time_in = "12:00"
    time_out = "18:00"
    result = attendance_on_time_out(time_in, time_out)
    assert result == "short"

def test_attendance_on_time_out_late_and_short():
    time_in = "13:00"
    time_out = "20:00"
    result = attendance_on_time_out(time_in, time_out)
    assert result == "late and short"
