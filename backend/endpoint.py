# routes.py
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import JSONResponse  # Add this import
import shutil
import json
from fraction import get_fractions_FMI_parallel
from suitability import get_suitabilities_FMI_parallel

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/process")
async def upload_process(file: UploadFile = File(), timegranu: str = Form()):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    with open(file.filename, "r") as f:
        process_ = json.load(f)
    workable_fractions = get_fractions_FMI_parallel(
        process=process_, battery_capacity=1000, time_granularity_process=int(timegranu), time_granularity_wind=10, step_size=1000)

    return {"file_name": file.filename, "process": process_, "fractions": workable_fractions}


@router.post("/suitability")
async def check_suitability(
    totalEnergy: str = Form(),
    waitingTime: str = Form(),
    windTurbine: str = Form(),
    batteryCapacity: str = Form()
):
    try:
        # Convert the string inputs to their appropriate data types
        waitingTime = int(waitingTime)
        totalEnergy = float(totalEnergy)
        windTurbine = int(windTurbine)
        batteryCapacity = float(batteryCapacity)

        # Perform your suitability calculation using the converted input values
        suitability_result = get_suitabilities_FMI_parallel(
            waitingTime,
            batteryCapacity,
            totalEnergy, windTurbine
        )

        return {"max waiting time": waitingTime, "suitability": suitability_result}
    except Exception as e:
        return {"error": str(e)}
