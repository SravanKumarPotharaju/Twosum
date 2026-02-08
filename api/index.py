from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TwoSumRequest(BaseModel):
    nums: list[int]
    target: int

class TwoSumResponse(BaseModel):
    indices: list[int]

@app.post("/two-sum", response_model=TwoSumResponse)
def two_sum(request: TwoSumRequest):
    lookup = {}
    for i, num in enumerate(request.nums):
        diff = request.target - num
        if diff in lookup:
            return {"indices": [lookup[diff], i]}
        lookup[num] = i
    return {"indices": []}
