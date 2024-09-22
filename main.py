from fastapi import FastAPI, HTTPException
from itertools import combinations
from typing import List
from pydantic import BaseModel

app = FastAPI()

class RequestModel(BaseModel):
    cards: List[str]

def isValidSet(cards):
    for i in range(4):
        valuesSet = {card[i] for card in cards}
        if (len(valuesSet)) == 2:
            return False
    return True

def validateCards(cards):
    for card in cards:
        if (len(card) != 4 or any(attr not in {'1','2','3'} for attr in card)):
            return False
    return True

@app.get("/")
def hello():
    return {"message":"Up and running"}

@app.post("/find-sets")
def findSets(req: RequestModel):
    cards = req.cards
    if (len(cards) < 3):
        raise HTTPException(status_code=400, detail="At least 3 cards are required to form a set.")
    if not validateCards(cards):
        raise HTTPException(status_code=400, detail="Each card must have 4 attributes and the value must be 1, 2 or 3.")

    validSets = []

    for comb in combinations(cards, 3):
        if (isValidSet(comb)):
            validSets.append(comb)

    return {"valid_sets" : validSets}