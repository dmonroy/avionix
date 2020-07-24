from datetime import time
from typing import List, Optional

from avionix.kubernetes_objects.base_objects import KubernetesBaseObject
from avionix.kubernetes_objects.meta import ListMeta, ObjectMeta
from avionix.yaml.yaml_handling import HelmYaml


class ServiceReference(HelmYaml):
    """
    :param name:Name is the name of the service
    :type name: Optional[str]
    :param namespace:Namespace is the namespace of the service
    :type namespace: Optional[str]
    :param port:If specified, the port on the service that hosting webhook. Default to \
        443 for backward compatibility. `port` should be a valid port number (1-65535, \
        inclusive).
    :type port: Optional[int]
    """

    def __init__(
        self,
        name: Optional[str] = None,
        namespace: Optional[str] = None,
        port: Optional[int] = None,
    ):
        self.name = name
        self.namespace = namespace
        self.port = port


class APIServiceSpec(HelmYaml):
    """
    :param ca_bundle:CABundle is a PEM encoded CA bundle which will be used to \
        validate an API server's serving certificate. If unspecified, system trust \
        roots on the apiserver are used.
    :type ca_bundle: str
    :param group:Group is the API group name this server hosts
    :type group: str
    :param group_priority_minimum:GroupPriorityMininum is the priority this group \
        should have at least. Higher priority means that the group is preferred by \
        clients over lower priority ones. Note that other versions of this group might \
        specify even higher GroupPriorityMininum values such that the whole group gets \
        a higher priority. The primary sort is based on GroupPriorityMinimum, ordered \
        highest number to lowest (20 before 10). The secondary sort is based on the \
        alphabetical comparison of the name of the object.  (v1.bar before v1.foo) \
        We'd recommend something like: *.k8s.io (except extensions) at 18000 and \
        PaaSes (OpenShift, Deis) are recommended to be in the 2000s
    :type group_priority_minimum: int
    :param insecure_skip_tlsverify:InsecureSkipTLSVerify disables TLS certificate \
        verification when communicating with this server. This is strongly \
        discouraged.  You should use the CABundle instead.
    :type insecure_skip_tlsverify: bool
    :param service:Service is a reference to the service for this API server.  It must \
        communicate on port 443 If the Service is nil, that means the handling for the \
        API groupversion is handled locally on this server. The call will simply \
        delegate to the normal handler chain to be fulfilled.
    :type service: ServiceReference
    :param version:Version is the API version this server hosts.  For example, "v1"
    :type version: str
    :param version_priority:VersionPriority controls the ordering of this API version \
        inside of its group.  Must be greater than zero. The primary sort is based on \
        VersionPriority, ordered highest to lowest (20 before 10). Since it's inside \
        of a group, the number can be small, probably in the 10s. In case of equal \
        version priorities, the version string will be used to compute the order \
        inside a group. If the version string is "kube-like", it will sort above non \
        "kube-like" version strings, which are ordered lexicographically. "Kube-like" \
        versions start with a "v", then are followed by a number (the major version), \
        then optionally the string "alpha" or "beta" and another number (the minor \
        version). These are sorted first by GA > beta > alpha (where GA is a version \
        with no suffix such as beta or alpha), and then by comparing major version, \
        then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, \
        v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.
    :type version_priority: int
    """

    def __init__(
        self,
        ca_bundle: str,
        group: str,
        group_priority_minimum: int,
        insecure_skip_tlsverify: bool,
        service: ServiceReference,
        version: str,
        version_priority: int,
    ):
        self.caBundle = ca_bundle
        self.group = group
        self.groupPriorityMinimum = group_priority_minimum
        self.insecureSkipTLSVerify = insecure_skip_tlsverify
        self.service = service
        self.version = version
        self.versionPriority = version_priority


class APIServiceCondition(HelmYaml):
    """
    :param last_transition_time:Last time the condition transitioned from one status \
        to another.
    :type last_transition_time: time
    :param message:Human-readable message indicating details about last transition.
    :type message: str
    :param reason:Unique, one-word, CamelCase reason for the condition's last \
        transition.
    :type reason: str
    :param type:Type is the type of the condition.
    :type type: str
    """

    def __init__(
        self, last_transition_time: time, message: str, reason: str, type: str
    ):
        self.lastTransitionTime = last_transition_time
        self.message = message
        self.reason = reason
        self.type = type


class APIService(KubernetesBaseObject):
    """
    :param metadata:None
    :type metadata: ObjectMeta
    :param spec:Spec contains information for locating and communicating with a server
    :type spec: APIServiceSpec
    :param api_version:APIVersion defines the versioned schema of this representation \
        of an object. Servers should convert recognized schemas to the latest internal \
        value, and may reject unrecognized values. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa
    :type api_version: Optional[str]
    """

    def __init__(
        self,
        metadata: ObjectMeta,
        spec: APIServiceSpec,
        api_version: Optional[str] = None,
    ):
        super().__init__(api_version)
        self.metadata = metadata
        self.spec = spec


class APIServiceList(KubernetesBaseObject):
    """
    :param items:None
    :type items: List[APIService]
    :param metadata:None
    :type metadata: ListMeta
    :param api_version:APIVersion defines the versioned schema of this representation \
        of an object. Servers should convert recognized schemas to the latest internal \
        value, and may reject unrecognized values. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa
    :type api_version: Optional[str]
    """

    def __init__(
        self,
        items: List[APIService],
        metadata: ListMeta,
        api_version: Optional[str] = None,
    ):
        super().__init__(api_version)
        self.items = items
        self.metadata = metadata
