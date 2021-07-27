# clever_client.SectionsApi

All URIs are relative to *https://api.clever.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_course_for_section**](SectionsApi.md#get_course_for_section) | **GET** /sections/{id}/course | 
[**get_district_for_section**](SectionsApi.md#get_district_for_section) | **GET** /sections/{id}/district | 
[**get_resources_for_section**](SectionsApi.md#get_resources_for_section) | **GET** /sections/{id}/resources | 
[**get_school_for_section**](SectionsApi.md#get_school_for_section) | **GET** /sections/{id}/school | 
[**get_section**](SectionsApi.md#get_section) | **GET** /sections/{id} | 
[**get_sections**](SectionsApi.md#get_sections) | **GET** /sections | 
[**get_term_for_section**](SectionsApi.md#get_term_for_section) | **GET** /sections/{id}/term | 
[**get_users_for_section**](SectionsApi.md#get_users_for_section) | **GET** /sections/{id}/users | 


# **get_course_for_section**
> CourseResponse get_course_for_section(id)



Returns the course for a section

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
api_instance = clever_client.SectionsApi(clever_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_course_for_section(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectionsApi->get_course_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CourseResponse**](CourseResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_for_section**
> DistrictResponse get_district_for_section(id)



Returns the district for a section

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
api_instance = clever_client.SectionsApi(clever_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_district_for_section(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectionsApi->get_district_for_section: %s\n" % e)
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

# **get_resources_for_section**
> ResourcesResponse get_resources_for_section(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the resources for a section

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
api_instance = clever_client.SectionsApi(clever_client.ApiClient(configuration))
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_resources_for_section(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectionsApi->get_resources_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**ResourcesResponse**](ResourcesResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_for_section**
> SchoolResponse get_school_for_section(id)



Returns the school for a section

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
api_instance = clever_client.SectionsApi(clever_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_school_for_section(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectionsApi->get_school_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SchoolResponse**](SchoolResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section**
> SectionResponse get_section(id)



Returns a specific section

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
api_instance = clever_client.SectionsApi(clever_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_section(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectionsApi->get_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SectionResponse**](SectionResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections**
> SectionsResponse get_sections(limit=limit, starting_after=starting_after, ending_before=ending_before, count=count)



Returns a list of sections

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
api_instance = clever_client.SectionsApi(clever_client.ApiClient(configuration))
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)
count = 'count_example' # str |  (optional)

try:
    api_response = api_instance.get_sections(limit=limit, starting_after=starting_after, ending_before=ending_before, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectionsApi->get_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 
 **count** | **str**|  | [optional] 

### Return type

[**SectionsResponse**](SectionsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_term_for_section**
> TermResponse get_term_for_section(id)



Returns the term for a section

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
api_instance = clever_client.SectionsApi(clever_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_term_for_section(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectionsApi->get_term_for_section: %s\n" % e)
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

# **get_users_for_section**
> UsersResponse get_users_for_section(id, role=role, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the student and/or teacher users for a section

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
api_instance = clever_client.SectionsApi(clever_client.ApiClient(configuration))
id = 'id_example' # str | 
role = 'role_example' # str |  (optional)
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_users_for_section(id, role=role, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectionsApi->get_users_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **role** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

