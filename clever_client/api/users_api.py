# coding: utf-8

"""
    Clever Data API

    Serves the Clever Data API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from clever_client.api_client import ApiClient


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_contacts_for_user(self, id, **kwargs):  # noqa: E501
        """get_contacts_for_user  # noqa: E501

        Returns the contact users for a student user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contacts_for_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_contacts_for_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_contacts_for_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_contacts_for_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_contacts_for_user  # noqa: E501

        Returns the contact users for a student user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_contacts_for_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'starting_after', 'ending_before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contacts_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_contacts_for_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'starting_after' in params:
            query_params.append(('starting_after', params['starting_after']))  # noqa: E501
        if 'ending_before' in params:
            query_params.append(('ending_before', params['ending_before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/mycontacts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UsersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_district_for_user(self, id, **kwargs):  # noqa: E501
        """get_district_for_user  # noqa: E501

        Returns the district for a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_district_for_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: DistrictResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_district_for_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_district_for_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_district_for_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_district_for_user  # noqa: E501

        Returns the district for a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_district_for_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: DistrictResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_district_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_district_for_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/district', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DistrictResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_resources_for_user(self, id, **kwargs):  # noqa: E501
        """get_resources_for_user  # noqa: E501

        Returns the resources for a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resources_for_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: ResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_resources_for_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_resources_for_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_resources_for_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_resources_for_user  # noqa: E501

        Returns the resources for a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resources_for_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: ResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'starting_after', 'ending_before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resources_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_resources_for_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'starting_after' in params:
            query_params.append(('starting_after', params['starting_after']))  # noqa: E501
        if 'ending_before' in params:
            query_params.append(('ending_before', params['ending_before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_schools_for_user(self, id, **kwargs):  # noqa: E501
        """get_schools_for_user  # noqa: E501

        Returns the schools for a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schools_for_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str primary:
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: SchoolsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_schools_for_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_schools_for_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_schools_for_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_schools_for_user  # noqa: E501

        Returns the schools for a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schools_for_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str primary:
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: SchoolsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'primary', 'limit', 'starting_after', 'ending_before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_schools_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_schools_for_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'primary' in params:
            query_params.append(('primary', params['primary']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'starting_after' in params:
            query_params.append(('starting_after', params['starting_after']))  # noqa: E501
        if 'ending_before' in params:
            query_params.append(('ending_before', params['ending_before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/schools', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SchoolsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sections_for_user(self, id, **kwargs):  # noqa: E501
        """get_sections_for_user  # noqa: E501

        Returns the sections for a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sections_for_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: SectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sections_for_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sections_for_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_sections_for_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_sections_for_user  # noqa: E501

        Returns the sections for a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sections_for_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: SectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'starting_after', 'ending_before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sections_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_sections_for_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'starting_after' in params:
            query_params.append(('starting_after', params['starting_after']))  # noqa: E501
        if 'ending_before' in params:
            query_params.append(('ending_before', params['ending_before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/sections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SectionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_students_for_user(self, id, **kwargs):  # noqa: E501
        """get_students_for_user  # noqa: E501

        Returns the student users for a teacher or contact user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_students_for_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_students_for_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_students_for_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_students_for_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_students_for_user  # noqa: E501

        Returns the student users for a teacher or contact user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_students_for_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'starting_after', 'ending_before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_students_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_students_for_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'starting_after' in params:
            query_params.append(('starting_after', params['starting_after']))  # noqa: E501
        if 'ending_before' in params:
            query_params.append(('ending_before', params['ending_before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/mystudents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UsersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_teachers_for_user(self, id, **kwargs):  # noqa: E501
        """get_teachers_for_user  # noqa: E501

        Returns the teacher users for a student user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_teachers_for_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_teachers_for_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_teachers_for_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_teachers_for_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_teachers_for_user  # noqa: E501

        Returns the teacher users for a student user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_teachers_for_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'starting_after', 'ending_before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_teachers_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_teachers_for_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'starting_after' in params:
            query_params.append(('starting_after', params['starting_after']))  # noqa: E501
        if 'ending_before' in params:
            query_params.append(('ending_before', params['ending_before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/myteachers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UsersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user(self, id, **kwargs):  # noqa: E501
        """get_user  # noqa: E501

        Returns a specific user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: UserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_user_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_user  # noqa: E501

        Returns a specific user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: UserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_users(self, **kwargs):  # noqa: E501
        """get_users  # noqa: E501

        Returns a list of contact, district admin, staff, student, and/or teacher users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param str role:
        :param str starting_after:
        :param str ending_before:
        :param str count:
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_users_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_users_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_users_with_http_info(self, **kwargs):  # noqa: E501
        """get_users  # noqa: E501

        Returns a list of contact, district admin, staff, student, and/or teacher users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param str role:
        :param str starting_after:
        :param str ending_before:
        :param str count:
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'role', 'starting_after', 'ending_before', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'role' in params:
            query_params.append(('role', params['role']))  # noqa: E501
        if 'starting_after' in params:
            query_params.append(('starting_after', params['starting_after']))  # noqa: E501
        if 'ending_before' in params:
            query_params.append(('ending_before', params['ending_before']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UsersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
