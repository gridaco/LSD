"""
    Flamenco manager

    Render Farm manager API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from flamenco.manager.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from flamenco.manager.exceptions import ApiAttributeError


def lazy_import():
    from flamenco.manager.model.job_all_of import JobAllOf
    from flamenco.manager.model.job_metadata import JobMetadata
    from flamenco.manager.model.job_settings import JobSettings
    from flamenco.manager.model.job_status import JobStatus
    from flamenco.manager.model.job_storage_info import JobStorageInfo
    from flamenco.manager.model.submitted_job import SubmittedJob
    globals()['JobAllOf'] = JobAllOf
    globals()['JobMetadata'] = JobMetadata
    globals()['JobSettings'] = JobSettings
    globals()['JobStatus'] = JobStatus
    globals()['JobStorageInfo'] = JobStorageInfo
    globals()['SubmittedJob'] = SubmittedJob


class Job(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'name': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'priority': (int,),  # noqa: E501
            'submitter_platform': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'created': (datetime,),  # noqa: E501
            'updated': (datetime,),  # noqa: E501
            'status': (JobStatus,),  # noqa: E501
            'activity': (str,),  # noqa: E501
            'type_etag': (str,),  # noqa: E501
            'settings': (JobSettings,),  # noqa: E501
            'metadata': (JobMetadata,),  # noqa: E501
            'storage': (JobStorageInfo,),  # noqa: E501
            'worker_tag': (str,),  # noqa: E501
            'delete_requested_at': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'type': 'type',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'submitter_platform': 'submitter_platform',  # noqa: E501
        'id': 'id',  # noqa: E501
        'created': 'created',  # noqa: E501
        'updated': 'updated',  # noqa: E501
        'status': 'status',  # noqa: E501
        'activity': 'activity',  # noqa: E501
        'type_etag': 'type_etag',  # noqa: E501
        'settings': 'settings',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'storage': 'storage',  # noqa: E501
        'worker_tag': 'worker_tag',  # noqa: E501
        'delete_requested_at': 'delete_requested_at',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Job - a model defined in OpenAPI

        Keyword Args:
            name (str):
            type (str):
            priority (int): defaults to 50  # noqa: E501
            submitter_platform (str): Operating system of the submitter. This is used to recognise two-way variables. This should be a lower-case version of the platform, like \"linux\", \"windows\", \"darwin\", \"openbsd\", etc. Should be ompatible with Go's `runtime.GOOS`; run `go tool dist list` to get a list of possible platforms. As a special case, the platform \"manager\" can be given, which will be interpreted as \"the Manager's platform\". This is mostly to make test/debug scripts easier, as they can use a static document on all platforms. 
            id (str): UUID of the Job
            created (datetime): Creation timestamp
            updated (datetime): Timestamp of last update.
            status (JobStatus):
            activity (str): Description of the last activity on this job.
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            type_etag (str): Hash of the job type, copied from the `AvailableJobType.etag` property of the job type. The job will be rejected if this field doesn't match the actual job type on the Manager. This prevents job submission with old settings, after the job compiler script has been updated. If this field is ommitted, the check is bypassed. . [optional]  # noqa: E501
            settings (JobSettings): [optional]  # noqa: E501
            metadata (JobMetadata): [optional]  # noqa: E501
            storage (JobStorageInfo): [optional]  # noqa: E501
            worker_tag (str): Worker tag that should execute this job. When a tag ID is given, only Workers in that tag will be scheduled to work on it. If empty or ommitted, all workers can work on this job. . [optional]  # noqa: E501
            delete_requested_at (datetime): If job deletion was requested, this is the timestamp at which that request was stored on Flamenco Manager. . [optional]  # noqa: E501
        """

        priority = kwargs.get('priority', 50)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Job - a model defined in OpenAPI

        Keyword Args:
            name (str):
            type (str):
            priority (int): defaults to 50  # noqa: E501
            submitter_platform (str): Operating system of the submitter. This is used to recognise two-way variables. This should be a lower-case version of the platform, like \"linux\", \"windows\", \"darwin\", \"openbsd\", etc. Should be ompatible with Go's `runtime.GOOS`; run `go tool dist list` to get a list of possible platforms. As a special case, the platform \"manager\" can be given, which will be interpreted as \"the Manager's platform\". This is mostly to make test/debug scripts easier, as they can use a static document on all platforms. 
            id (str): UUID of the Job
            created (datetime): Creation timestamp
            updated (datetime): Timestamp of last update.
            status (JobStatus):
            activity (str): Description of the last activity on this job.
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            type_etag (str): Hash of the job type, copied from the `AvailableJobType.etag` property of the job type. The job will be rejected if this field doesn't match the actual job type on the Manager. This prevents job submission with old settings, after the job compiler script has been updated. If this field is ommitted, the check is bypassed. . [optional]  # noqa: E501
            settings (JobSettings): [optional]  # noqa: E501
            metadata (JobMetadata): [optional]  # noqa: E501
            storage (JobStorageInfo): [optional]  # noqa: E501
            worker_tag (str): Worker tag that should execute this job. When a tag ID is given, only Workers in that tag will be scheduled to work on it. If empty or ommitted, all workers can work on this job. . [optional]  # noqa: E501
            delete_requested_at (datetime): If job deletion was requested, this is the timestamp at which that request was stored on Flamenco Manager. . [optional]  # noqa: E501
        """

        priority = kwargs.get('priority', 50)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              JobAllOf,
              SubmittedJob,
          ],
          'oneOf': [
          ],
        }