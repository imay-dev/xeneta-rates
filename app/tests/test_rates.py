import pytest
from datetime import date, datetime


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_get_rates(test_app):
    response = test_app.get("/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main")
    assert response.status_code == 200
    
    if len(response.json()) > 0 :
        first_item = response.json()[0]
        
        assert 'day' in first_item
        assert type(datetime.strptime(first_item['day'], '%Y-%m-%d')) is datetime
        
        assert 'average_price' in first_item
        assert type(first_item['average_price']) is int



def test_get_rates_validation_error(test_app):
    response = test_app.get("/rates")
    assert response.status_code == 422
    
    assert response.json() == {'detail': [{'loc': ['query', 'date_from'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['query', 'date_to'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['query', 'origin'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['query', 'destination'], 'msg': 'field required', 'type': 'value_error.missing'}]}
