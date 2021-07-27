# swagger_client.CoursesApi

All URIs are relative to *https://api.clever.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_course**](CoursesApi.md#get_course) | **GET** /courses/{id} | 
[**get_courses**](CoursesApi.md#get_courses) | **GET** /courses | 
[**get_district_for_course**](CoursesApi.md#get_district_for_course) | **GET** /courses/{id}/district | 
[**get_resources_for_course**](CoursesApi.md#get_resources_for_course) | **GET** /courses/{id}/resources | 
[**get_schools_for_course**](CoursesApi.md#get_schools_for_course) | **GET** /courses/{id}/schools | 
[**get_sections_for_course**](CoursesApi.md#get_sections_for_course) | **GET** /courses/{id}/sections | 


# **get_course**
> CourseResponse get_course(id)



Returns a specific course

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
api_instance = swagger_client.CoursesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_course(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->get_course: %s\n" % e)
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

# **get_courses**
> CoursesResponse get_courses(limit=limit, starting_after=starting_after, ending_before=ending_before, count=count)



Returns a list of courses

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
api_instance = swagger_client.CoursesApi(swagger_client.ApiClient(configuration))
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)
count = 'count_example' # str |  (optional)

try:
    api_response = api_instance.get_courses(limit=limit, starting_after=starting_after, ending_before=ending_before, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->get_courses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 
 **count** | **str**|  | [optional] 

### Return type

[**CoursesResponse**](CoursesResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_district_for_course**
> DistrictResponse get_district_for_course(id)



Returns the district for a course

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
api_instance = swagger_client.CoursesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_district_for_course(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->get_district_for_course: %s\n" % e)
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

# **get_resources_for_course**
> ResourcesResponse get_resources_for_course(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the resources for a course

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
api_instance = swagger_client.CoursesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_resources_for_course(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->get_resources_for_course: %s\n" % e)
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

# **get_schools_for_course**
> SchoolsResponse get_schools_for_course(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the schools for a course

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
api_instance = swagger_client.CoursesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_schools_for_course(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->get_schools_for_course: %s\n" % e)
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

# **get_sections_for_course**
> SectionsResponse get_sections_for_course(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the sections for a course

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
api_instance = swagger_client.CoursesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_sections_for_course(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->get_sections_for_course: %s\n" % e)
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

