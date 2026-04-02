def generate_alert(row):
    if row["oxygen"] < 4:
        return "⚠️ Low Oxygen - Marine life risk"
    elif row["temperature"] > 31:
        return "⚠️ High Temperature"
    elif row["ph"] < 7.5:
        return "⚠️ Acidic Water"
    else:
        return "✅ Safe"