def claculate_tip(bill, service_quality):
    if service_quality == "poor":
        return 0.10 * bill
    if service_quality == "average":
        return 0.15 * bill
    if service_quality == "excellent":
        return 0.20 * bill
    if service_quality == "":
