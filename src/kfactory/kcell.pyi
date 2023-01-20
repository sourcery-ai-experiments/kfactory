from typing import (
    Any,
    Callable,
    Hashable,
    Iterator,
    Optional,
    Sequence,
    Union,
    overload,
)

from _typeshed import Incomplete
from cachetools import Cache

from . import kdb

class KLib(kdb.Layout):
    kcells: Incomplete
    def __init__(self, editable: bool = ...) -> None: ...
    def create_cell(self, kcell: KCell, name: str, *args: Union[list[str], list[Union[str, dict[str, Any]]], list[Union[str, str]]], allow_duplicate: bool = ...) -> kdb.Cell: ...  # type: ignore[override]
    def update_cell_name(self, name: str, new_name: str) -> None: ...

library: Incomplete

class Port:
    name: str
    width: int
    trans: kdb.Trans
    layer: int
    port_type: str
    yaml_tag: str
    @overload
    def __init__(
        self,
        *,
        name: str,
        trans: kdb.Trans,
        width: int,
        layer: int,
        port_type: str = ...,
    ) -> None: ...
    @overload
    def __init__(self, *, name: Optional[str] = ..., port: Port) -> None: ...
    @overload
    def __init__(
        self,
        *,
        name: str,
        width: int,
        position: tuple[int, int],
        angle: int,
        layer: int,
        port_type: str = ...,
        mirror_x: bool = ...,
    ) -> None: ...
    def hash(self) -> bytes: ...
    def copy(self, trans: kdb.Trans = ...) -> Port: ...
    @property
    def position(self) -> tuple[int, int]: ...
    @property
    def angle(self) -> int: ...
    @property
    def mirror(self) -> bool: ...
    @property
    def x(self) -> int: ...
    @property
    def y(self) -> int: ...
    def move(
        self, origin: tuple[int, int], destination: Optional[tuple[int, int]] = ...
    ) -> None: ...
    def rotate(self, angle: int) -> None: ...
    @classmethod
    def to_yaml(cls, representer, node): ...  # type: ignore[no-untyped-def]
    @classmethod
    def from_yaml(cls, constructor, node): ...  # type: ignore[no-untyped-def]

class DPort:
    name: str
    width: float
    trans: kdb.Trans
    layer: int
    port_type: str
    yaml_tag: str
    @overload
    def __init__(
        self,
        *,
        name: str,
        trans: kdb.DTrans,
        width: float,
        layer: int,
        port_type: str = ...,
    ) -> None: ...
    @overload
    def __init__(self, *, name: Optional[str] = ..., port: DPort) -> None: ...
    @overload
    def __init__(
        self,
        *,
        name: str,
        width: float,
        position: tuple[float, float],
        angle: int,
        layer: int,
        port_type: str = ...,
        mirror_x: bool = ...,
    ) -> None: ...
    def hash(self) -> bytes: ...
    def copy(self, trans: kdb.DTrans = ...) -> DPort: ...
    @property
    def position(self) -> tuple[float, float]: ...
    @property
    def angle(self) -> int: ...
    @property
    def mirror(self) -> bool: ...
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    def move(
        self,
        origin: tuple[float, float],
        destination: Optional[tuple[float, float]] = ...,
    ) -> None: ...
    def rotate(self, angle: int) -> None: ...
    @classmethod
    def to_yaml(cls, representer, node): ...  # type: ignore[no-untyped-def]
    @classmethod
    def from_yaml(cls, constructor, node): ...  # type: ignore[no-untyped-def]

class ICplxPort:
    name: str
    width: int
    trans: kdb.ICplxTrans
    layer: int
    port_type: str
    yaml_tag: str
    @overload
    def __init__(
        self,
        *,
        name: str,
        trans: kdb.ICplxTrans,
        width: int,
        layer: int,
        port_type: str = ...,
    ) -> None: ...
    @overload
    def __init__(self, *, name: Optional[str] = ..., port: ICplxPort) -> None: ...
    @overload
    def __init__(
        self,
        *,
        name: str,
        width: int,
        position: tuple[int, int],
        angle: float,
        layer: int,
        port_type: str = ...,
        mirror_x: bool = ...,
    ) -> None: ...
    def hash(self) -> bytes: ...
    def copy(self, trans: kdb.ICplxTrans = ...) -> ICplxPort: ...
    @property
    def position(self) -> tuple[int, int]: ...
    @property
    def angle(self) -> float: ...
    @property
    def mirror(self) -> bool: ...
    @property
    def x(self) -> int: ...
    @property
    def y(self) -> int: ...
    def move(
        self, origin: tuple[int, int], destination: Optional[tuple[int, int]] = ...
    ) -> None: ...
    def rotate(self, angle: float) -> None: ...
    @classmethod
    def to_yaml(cls, representer, node): ...  # type: ignore[no-untyped-def]
    @classmethod
    def from_yaml(cls, constructor, node): ...  # type: ignore[no-untyped-def]

class DCplxPort:
    name: str
    width: float
    trans: kdb.DCplxTrans
    layer: int
    port_type: str
    yaml_tag: str
    @overload
    def __init__(
        self,
        *,
        name: str,
        trans: kdb.DCplxTrans,
        width: float,
        layer: int,
        port_type: str = ...,
    ) -> None: ...
    @overload
    def __init__(self, *, name: Optional[str] = ..., port: DCplxPort) -> None: ...
    @overload
    def __init__(
        self,
        *,
        name: str,
        width: float,
        position: tuple[float, float],
        angle: float,
        layer: int,
        port_type: str = ...,
        mirror_x: bool = ...,
    ) -> None: ...
    def hash(self) -> bytes: ...
    def copy(self, trans: kdb.DCplxTrans = ...) -> DCplxPort: ...
    @property
    def position(self) -> tuple[float, float]: ...
    @property
    def angle(self) -> float: ...
    @property
    def mirror(self) -> bool: ...
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    def move(
        self,
        origin: tuple[float, float],
        destination: Optional[tuple[float, float]] = ...,
    ) -> None: ...
    def rotate(self, angle: float) -> None: ...
    @classmethod
    def to_yaml(cls, representer, node): ...  # type: ignore[no-untyped-def]
    @classmethod
    def from_yaml(cls, constructor, node): ...  # type: ignore[no-untyped-def]

class KCell:
    yaml_tag: str
    library: Incomplete
    ports: Incomplete
    insts: Incomplete
    settings: Incomplete
    def __init__(
        self,
        name: Optional[str] = ...,
        library: KLib = ...,
        kdb_cell: Optional[kdb.Cell] = ...,
    ) -> None: ...
    def copy(self) -> KCell: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, new_name: str) -> None: ...
    @overload
    def create_port(
        self,
        *,
        name: str,
        trans: kdb.Trans,
        width: int,
        layer: int,
        port_type: str = ...,
    ) -> None: ...
    @overload
    def create_port(self, *, name: Optional[str] = ..., port: Port) -> None: ...
    @overload
    def create_port(
        self,
        *,
        name: str,
        width: int,
        position: tuple[int, int],
        angle: int,
        layer: int,
        port_type: str = ...,
        mirror_x: bool = ...,
    ) -> None: ...
    def add_port(self, port: PortLike[TT, FI], name: Optional[str] = ...) -> None: ...
    def create_inst(self, cell: KCell, trans: kdb.Trans = ...) -> Instance: ...
    def layer(self, *args: Any, **kwargs: Any) -> int: ...
    def __lshift__(self, cell: KCell) -> Instance: ...
    def __getattribute__(self, attr_name: str) -> Any: ...
    def __getattr__(self, attr_name: str) -> Any: ...
    def __setattr__(self, attr_name: str, attr_value: Any) -> None: ...
    def hash(self) -> bytes: ...
    def autorename_ports(self) -> None: ...
    def flatten(self, prune: bool = ..., merge: bool = ...) -> None: ...
    def draw_ports(self) -> None: ...
    @classmethod
    def to_yaml(cls, representer, node): ...  # type: ignore[no-untyped-def]
    @classmethod
    def from_yaml(cls, constructor, node, verbose: bool = ...): ...  # type: ignore[no-untyped-def]
    def basic_name(self) -> str: ...
    def bbox(self) -> kdb.Box: ...
    def bbox_per_layer(self, layer_index: int) -> kdb.Box: ...
    def begin_instances_rec(self) -> kdb.RecursiveInstanceIterator: ...
    @overload
    def begin_instances_rec_overlapping(
        self, region: kdb.Box
    ) -> kdb.RecursiveInstanceIterator: ...
    @overload
    def begin_instances_rec_overlapping(
        self, region: kdb.DBox
    ) -> kdb.RecursiveInstanceIterator: ...
    @overload
    def begin_instances_rec_touching(
        self, region: kdb.Box
    ) -> kdb.RecursiveInstanceIterator: ...
    @overload
    def begin_instances_rec_touching(
        self, region: kdb.DBox
    ) -> kdb.RecursiveInstanceIterator: ...
    def begin_shapes_rec(self, layer: int) -> kdb.RecursiveShapeIterator: ...
    @overload
    def begin_shapes_rec_overlapping(
        self, layer: int, region: kdb.Box
    ) -> kdb.RecursiveShapeIterator: ...
    @overload
    def begin_shapes_rec_overlapping(
        self, layer: int, region: kdb.DBox
    ) -> kdb.RecursiveShapeIterator: ...
    @overload
    def begin_shapes_rec_touching(
        self, layer: int, region: kdb.Box
    ) -> kdb.RecursiveShapeIterator: ...
    @overload
    def begin_shapes_rec_touching(
        self, layer: int, region: kdb.DBox
    ) -> kdb.RecursiveShapeIterator: ...
    def called_cells(self) -> Sequence[int]: ...
    def caller_cells(self) -> Sequence[int]: ...
    def cell_index(self) -> int: ...
    def child_cells(self) -> int: ...
    def child_instances(self) -> int: ...
    @overload
    def clear(self) -> None: ...
    @overload
    def clear(self, layer_index: int) -> None: ...
    def clear_insts(self) -> None: ...
    def clear_shapes(self) -> None: ...
    # @overload
    # def copy(self, src: int, dest: int) -> None: ...
    # @overload
    # def copy(self, src_cell: Cell, src_layer: int, dest: int) -> None: ...
    def dbbox(self) -> kdb.DBox: ...
    def dbbox_per_layer(self, layer_index: int) -> kdb.DBox: ...
    def delete(self) -> None: ...
    def delete_property(self, key: str | int) -> None: ...
    def display_titlle(self) -> str: ...
    def dup(self) -> kdb.Cell: ...
    def each_child_cell(self) -> Iterator[int]: ...
    @overload
    def each_overlapping_shape(
        self, layer_index: int, box: kdb.Box, flags: int
    ) -> Iterator[kdb.Shape]: ...
    @overload
    def each_overlapping_shape(
        self, layer_index: int, box: kdb.Box
    ) -> Iterator[kdb.Shape]: ...
    @overload
    def each_overlapping_shape(
        self, layer_index: int, box: kdb.DBox, fflags: int
    ) -> Iterator[kdb.Shape]: ...
    @overload
    def each_overlapping_shape(
        self, layer_index: int, box: kdb.DBox
    ) -> Iterator[kdb.Shape]: ...
    @overload
    def each_shape(self, layer_index: int, flags: int) -> Iterator[kdb.Shape]: ...
    @overload
    def each_shape(self, layer_index: int) -> Iterator[kdb.Shape]: ...
    @overload
    def each_touching_shape(
        self, layer_index: int, box: kdb.Box, flags: int
    ) -> Iterator[kdb.Shape]: ...
    @overload
    def each_touching_shape(
        self, layer_index: int, box: kdb.Box
    ) -> Iterator[kdb.Shape]: ...
    @overload
    def each_touching_shape(
        self, layer_index: int, box: kdb.DBox, flags: int
    ) -> Iterator[kdb.Shape]: ...
    @overload
    def fill_region(
        self,
        region: kdb.Region,
        fill_cell_index: int,
        ffc_box: kdb.Box,
        origin: kdb.Point = kdb.Point(0, 0),
        remaining_parts: Optional[kdb.Region] = None,
        fill_margin: kdb.Vector = kdb.Vector(0, 0),
        remaining_polygons: Optional[kdb.Region] = None,
        glue_box: kdb.Box = kdb.Box(),
    ) -> None: ...
    @overload
    def fill_region(
        self,
        region: kdb.Region,
        fill_cell_index: int,
        fc_bbox: kdb.Box,
        row_step: kdb.Vector,
        column_step: kdb.Vector,
        origin: kdb.Point = kdb.Point(0, 0),
        remaining_parts: Optional[kdb.Region] = None,
        fill_margin: kdb.Vector = kdb.Vector(0, 0),
        remaining_polygons: Optional[kdb.Region] = None,
        glue_box: kdb.Box = kdb.Box(),
    ) -> None: ...
    # @overload
    # def flatten(self, prune: bool) -> None: ...
    # @overload
    # def flatten(self, levels: int, prune: bool) -> None: ...
    def has_prop_id(self) -> bool: ...
    def hierarchy_levels(self) -> int: ...
    @overload
    def insert(self, inst: Instance) -> Instance: ...
    @overload
    def insert(
        self, cell_inst_array: kdb.CellInstArray | kdb.DCellInstArray
    ) -> kdb.Instance: ...
    @overload
    def insert(
        self, cell_inst_array: kdb.CellInstArray | kdb.DCellInstArray, property_id: int
    ) -> kdb.Instance: ...
    def is_empty(self) -> bool: ...
    def is_ghost_cell(self) -> bool: ...
    def is_leaf(self) -> bool: ...
    def is_library_cell(self) -> bool: ...
    @overload
    def is_pcell_variant(self) -> bool: ...
    @overload
    def is_pcell_variant(self, instance: kdb.Instance) -> bool: ...
    def is_proxy(self) -> bool: ...
    def is_top(self) -> bool: ...
    def is_valid(self, instance: kdb.Instance) -> bool: ...
    def layout(self) -> kdb.Layout: ...
    # def library(self) -> Optional[kdb.Library]: ...
    def library_cell_index(self) -> Optional[int]: ...
    @overload
    def move(self, src: int, dest: int) -> None: ...
    @overload
    def move(self, src_cell: kdb.Cell, src: int, dest: int) -> None: ...
    @overload
    def move_shapes(self, source_cell: kdb.Cell) -> None: ...
    @overload
    def move_shapes(
        self, source_cell: kdb.Cell, layer_mapping: kdb.LayerMapping
    ) -> None: ...
    def parent_cells(self) -> int: ...
    def prune_cell(self, levels: int = -1) -> None: ...
    def prune_subcells(self, levels: int = -1) -> None: ...
    def qname(self) -> str: ...
    @overload
    def replace(
        self,
        instance: kdb.Instance,
        cell_inst_array: kdb.CellInstArray | kdb.DCellInstArray,
    ) -> kdb.Instance: ...
    @overload
    def replace(
        self,
        instance: kdb.Instance,
        cell_inst_array: kdb.CellInstArray | kdb.DCellInstArray,
        property_id: int,
    ) -> kdb.Instance: ...
    def replace_prop_id(self, instance: Instance, property_id: int) -> Instance: ...
    def set_property(self, key: str | int, value: str | int | float) -> None: ...
    def shapes(self, layer_index: int) -> kdb.Shapes: ...
    def swap(self, layer_index1: int, layer_index2: int) -> None: ...
    @overload
    def transform(
        self,
        instance: Instance,
        trans: kdb.Trans | kdb.ICplxTrans | kdb.DTrans | kdb.DCplxTrans,
    ) -> Instance: ...
    @overload
    def transform(
        self, trans: kdb.Trans | kdb.DTrans | kdb.ICplxTrans | kdb.DCplxTrans
    ) -> None: ...
    @overload
    def transform_into(
        self,
        instance: Instance,
        trans: kdb.Trans | kdb.DTrans | kdb.ICplxTrans | kdb.DCplxTrans,
    ) -> Instance: ...
    @overload
    def transform_into(
        self, trans: kdb.Trans | kdb.DTrans | kdb.ICplxTrans | kdb.DCplxTrans
    ) -> None: ...
    @overload
    def write(self, file_name: str) -> None: ...
    @overload
    def write(self, file_name: str, options: kdb.SaveLayoutOptions) -> None: ...

class Instance:
    yaml_tag: str
    cell: Incomplete
    instance: Incomplete
    ports: Incomplete
    def __init__(self, cell: KCell, reference: kdb.Instance) -> None: ...
    def hash(self) -> bytes: ...
    def connect(
        self,
        portname: str,
        other_instance: Union["Instance", Port],
        other_port_name: Optional[str] = ...,
        mirror: bool = ...,
    ) -> None: ...
    def __getattribute__(self, attr_name: str) -> Any: ...
    def __getattr__(self, attr_name: str) -> Any: ...
    def __setattr__(self, attr_name: str, attr_value: Any) -> None: ...
    @classmethod
    def to_yaml(cls, representer, node): ...  # type: ignore[no-untyped-def]

class Ports:
    yaml_tag: str
    def __init__(self, ports: list[Port] = ...) -> None: ...
    def copy(self) -> Ports: ...
    def contains(self, port: Port) -> bool: ...
    def each(self) -> Iterator["Port"]: ...
    def add_port(self, port: PortLike[TT, FI], name: Optional[str] = ...) -> None: ...
    @overload
    def create_port(
        self,
        *,
        name: str,
        trans: kdb.Trans,
        width: int,
        layer: int,
        port_type: str = ...,
    ) -> Port: ...
    @overload
    def create_port(
        self,
        *,
        name: str,
        width: int,
        layer: int,
        position: tuple[int, int],
        angle: int,
        port_type: str = ...,
    ) -> Port: ...
    def get_all(self) -> dict[str, Port]: ...
    def __getitem__(self, key: str) -> Port: ...
    def hash(self) -> bytes: ...
    @classmethod
    def to_yaml(cls, representer, node): ...  # type: ignore[no-untyped-def]
    @classmethod
    def from_yaml(cls, constructor, node): ...  # type: ignore[no-untyped-def]

class InstancePorts:
    cell_ports: Incomplete
    instance: Incomplete
    def __init__(self, instance: Instance) -> None: ...
    def __getitem__(self, key: str) -> Port: ...
    def get_all(self) -> dict[str, Port]: ...

def autocell(
    _func: Optional[Callable[..., KCell]] = ...,
    *,
    set_settings: bool = ...,
    set_name: bool = ...,
    maxsize: int = ...,
) -> Callable[..., KCell]: ...
def cell(
    _func: Optional[Callable[..., KCell]] = ..., *, set_settings: bool = ...
) -> Callable[..., KCell]: ...

class KCellCache(Cache[int, Any]):
    def popitem(self) -> tuple[int, Any]: ...

def default_save() -> kdb.SaveLayoutOptions: ...
