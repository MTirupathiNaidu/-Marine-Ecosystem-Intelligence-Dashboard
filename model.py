from sklearn.ensemble import IsolationForest

def train_model(data):
    model = IsolationForest(contamination=0.2)
    model.fit(data)
    return model

def predict(model, data):
    preds = model.predict(data)
    return ["Normal" if p == 1 else "Anomaly" for p in preds]