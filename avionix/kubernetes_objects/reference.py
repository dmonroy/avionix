from typing import Optional

from avionix.kubernetes_objects.base_objects import KubernetesBaseObject


class ObjectReference(KubernetesBaseObject):
    """
    :param field_path:If referring to a piece of an object instead of an entire \
        object, this string should contain a valid JSON/Go field access statement, \
        such as desiredState.manifest.containers[2]. For example, if the object \
        reference is to a container within a pod, this would take on a value like: \
        "spec.containers{name}" (where "name" refers to the name of the container that \
        triggered the event) or if no container name is specified "spec.containers[2]" \
        (container with index 2 in this pod). This syntax is chosen only to have some \
        well-defined way of referencing a part of an object.
    :type field_path: str
    :param resource_version:Specific resourceVersion to which this reference is made, \
        if any. More info: \
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency  # noqa
    :type resource_version: str
    :param uid:UID of the referent. More info: \
        https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids
    :type uid: str
    :param api_version:API version of the referent.
    :type api_version: Optional[str]
    :param name:Name of the referent. More info: \
        https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  # noqa
    :type name: Optional[str]
    :param namespace:Namespace of the referent. More info: \
        https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
    :type namespace: Optional[str]
    """

    def __init__(
        self,
        field_path: str,
        resource_version: str,
        uid: str,
        api_version: Optional[str] = None,
        name: Optional[str] = None,
        namespace: Optional[str] = None,
    ):
        super().__init__(api_version)
        self.fieldPath = field_path
        self.resourceVersion = resource_version
        self.uid = uid
        self.name = name
        self.namespace = namespace
