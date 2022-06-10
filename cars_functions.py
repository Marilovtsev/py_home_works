def make_car(mark, model, **details_info):
    details_info['car_mark'] = mark
    details_info['car_model'] = model
    return details_info