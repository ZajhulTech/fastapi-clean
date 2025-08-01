from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List, Dict, Any

T = TypeVar("T")

class IBaseRepository(ABC, Generic[T]):
    @abstractmethod
    def find_by_id(self, id: Any) -> Optional[T]: ...
    
    @abstractmethod
    def find(self, filter: Dict[str, Any]) -> Optional[T]: ...
    
    @abstractmethod
    def find_all(self, filter: Dict[str, Any]) -> List[T]: ...
    
    @abstractmethod
    def insert(self, data: T) -> Any: ...
    
    @abstractmethod
    def update(self, id: Any, data: Dict[str, Any]) -> int: ...
    
    @abstractmethod
    def delete(self, id: Any) -> int: ...
    
    @abstractmethod
    def count(self, filter: Dict[str, Any]) -> int: ...
