# clever_client.DistrictsApi

All URIs are relative to *https://api.clever.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_district**](DistrictsApi.md#get_district) | **GET** /districts/{id} | 
[**get_districts**](DistrictsApi.md#get_districts) | **GET** /districts | 


# **get_district**
> DistrictResponse get_district(id)



Returns a specific district

### Example
```python
from __future__ import print_function
import time
import clever_client
from clever_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = clever_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = clever_client.DistrictsApi(clever_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_district(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictsApi->get_district: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DistrictResponse**](DistrictResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_districts**
> DistrictsResponse get_districts(count=count)



Returns a list of districts

### Example
```python
from __future__ import print_function
import time
import clever_client
from clever_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = clever_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = clever_client.DistrictsApi(clever_client.ApiClient(configuration))
count = 'count_example' # str |  (optional)

try:
    api_response = api_instance.get_districts(count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistrictsApi->get_districts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **str**|  | [optional] 

### Return type

[**DistrictsResponse**](DistrictsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

