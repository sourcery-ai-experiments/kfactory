from functools import partial
import kfactory as kf
import numpy as np
from random import randint


def test_all_angle_bundle(LAYER: kf.LayerEnum) -> None:
    sf = partial(kf.cells.virtual.straight.virtual_straight, layer=LAYER.WG)
    bf = partial(
        kf.cells.virtual.euler.virtual_bend_euler, layer=LAYER.WG, radius=10, width=1
    )

    vc = kf.VKCell("test_all_angle")

    start_ports: list[kf.Port] = []
    end_ports: list[kf.Port] = []
    r = 50
    n = 3
    _l = 9

    for i in range(_l):
        # for i in range(1):
        a = (n - i) * 15
        a_rad = np.deg2rad(a)
        ae = 270 - n + i * 15
        ae_rad = np.deg2rad(ae)
        start_ports.append(
            vc.create_port(
                name="s0",
                dcplx_trans=kf.kdb.DCplxTrans(
                    1, a, False, -500 + r * np.cos(a_rad), -100 + r * np.sin(a_rad)
                ),
                layer=LAYER.WG,
                dwidth=1,
            )
        )
        end_ports.append(
            vc.create_port(
                name="s0",
                dcplx_trans=kf.kdb.DCplxTrans(
                    1, ae, False, 1510 + r * np.cos(ae_rad), 1410 + r * np.sin(ae_rad)
                ),
                layer=LAYER.WG,
                dwidth=1,
            )
        )

    kf.routing.aa.optical.route_bundle(
        vc,
        start_ports=start_ports,
        end_ports=end_ports,
        backbone=[kf.kdb.DPoint(550, 550), kf.kdb.DPoint(950, 950)],
        spacings=[randint(1, 5) for _ in range(_l)],
        radius_estimate=lambda angle: 60,
        straight_factory=sf,
        bend_factory=bf,
    )

    vc.show()
