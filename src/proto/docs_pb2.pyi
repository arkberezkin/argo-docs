from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Doc(_message.Message):
    __slots__ = ["text", "title", "user_id"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    text: str
    title: str
    user_id: str
    def __init__(self, title: _Optional[str] = ..., user_id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class DocsRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class DocsResponse(_message.Message):
    __slots__ = ["documents"]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedCompositeFieldContainer[Doc]
    def __init__(self, documents: _Optional[_Iterable[_Union[Doc, _Mapping]]] = ...) -> None: ...
