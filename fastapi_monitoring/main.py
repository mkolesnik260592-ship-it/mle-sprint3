import numpy as np
from fastapi import FastAPI
from prometheus_client import Histogram, Counter
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# main_app_predictions — объект метрики
main_app_predictions = Histogram(
    "main_app_predictions",
    "Histogram of predictions",
    buckets=(1, 2, 4, 5, 10),
)

main_app_counter = Counter(
    "main_app_counter",
    "Counter of prediction"
)

@app.get("/predict")
def predict(x: int, y: int):
    np.random.seed(x)
    prediction = x+y + np.random.normal(0,1)
    main_app_predictions.observe(prediction)
    if prediction > 0:
        main_app_counter.inc()
    return {'prediction': prediction}
