# swagger_client.TermsApi

All URIs are relative to *https://api.clever.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_district_for_term**](TermsApi.md#get_district_for_term) | **GET** /terms/{id}/district | 
[**get_schools_for_term**](TermsApi.md#get_schools_for_term) | **GET** /terms/{id}/schools | 
[**get_sections_for_term**](TermsApi.md#get_sections_for_term) | **GET** /terms/{id}/sections | 
[**get_term**](TermsApi.md#get_term) | **GET** /terms/{id} | 
[**get_terms**](TermsApi.md#get_terms) | **GET** /terms | 


# **get_district_for_term**
> DistrictResponse get_district_for_term(id)



Returns the district for a term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TermsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_district_for_term(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsApi->get_district_for_term: %s\n" % e)
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

# **get_schools_for_term**
> SchoolsResponse get_schools_for_term(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the schools for a term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TermsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_schools_for_term(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsApi->get_schools_for_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SchoolsResponse**](SchoolsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections_for_term**
> SectionsResponse get_sections_for_term(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the sections for a term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TermsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_sections_for_term(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsApi->get_sections_for_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SectionsResponse**](SectionsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_term**
> TermResponse get_term(id)



Returns a specific term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TermsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_term(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsApi->get_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TermResponse**](TermResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_terms**
> TermsResponse get_terms(limit=limit, starting_after=starting_after, ending_before=ending_before, count=count)



Returns a list of terms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TermsApi(swagger_client.ApiClient(configuration))
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)
count = 'count_example' # str |  (optional)

try:
    api_response = api_instance.get_terms(limit=limit, starting_after=starting_after, ending_before=ending_before, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermsApi->get_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 
 **count** | **str**|  | [optional] 

### Return type

[**TermsResponse**](TermsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

