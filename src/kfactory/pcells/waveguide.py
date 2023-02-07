from typing import Optional

from .. import KCell, LayerEnum, library
from ..utils import Enclosure
from .dbu.waveguide import waveguide as waveguide_dbu


def waveguide(
    width: float,
    length: float,
    layer: int | LayerEnum,
    enclosure: Optional[Enclosure] = None,
) -> KCell:
    return waveguide_dbu(
        int(width / library.dbu), int(length / library.dbu), layer, enclosure=enclosure
    )
