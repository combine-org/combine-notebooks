from pathlib import Path
from sbmlutils.io import read_sbml, write_sbml, validate_sbml

from sbmlutils.factory import *
from sbmlutils.metadata import *

import tempfile

model = Model(
    "example_repressilator_model",
    units=Units,
    model_units=ModelUnits(
        time=Units.second,
        substance=Units.mole,
        extent=Units.mole,
        volume=Units.litre,
    ),
    compartments=[Compartment(sid="cell", value=1.0, sboTerm="SBO:0000290")],
    species=[
        Species(
            sid="PX",
            compartment="cell",
            name="LacI protein",
            sboTerm="SBO:0000252",
            initialAmount=0,
            hasOnlySubstanceUnits=True,
        ),
        Species(
            sid="PY",
            compartment="cell",
            name="TetR protein",
            sboTerm="SBO:0000252",
            initialAmount=0,
            hasOnlySubstanceUnits=True
        ),
        Species(
            sid="PZ",
            compartment="cell",
            name="cI protein",
            sboTerm="SBO:0000252",
            initialAmount=0,
            hasOnlySubstanceUnits=True
        ),
        Species(
            sid="X",
            compartment="cell",
            name="Lacl mRNA",
            sboTerm="SBO:0000250",
            initialAmount=20,
            hasOnlySubstanceUnits=True
        ),
        Species(
            sid="Y",
            compartment="cell",
            name="TetR mRNA",
            sboTerm="SBO:0000250",
            initialAmount=20,
            hasOnlySubstanceUnits=True
        ),
        Species(
            sid="Z",
            compartment="cell",
            name="cl mRNA",
            sboTerm="SBO:0000250",
            initialAmount=0,
            hasOnlySubstanceUnits=True
        )
    ],

    parameters=[Parameter(sid="tau_mRNA", name="mRNA half life", constant=True, value=2.0),
                Parameter(sid="kd_mRNA", name="kd_mRNA", constant=False, sboTerm="SBO:0000356"),
                Parameter(sid="k_tl", name="k_tl", constant=False, sboTerm="SBO:0000016"),
                Parameter(sid="t_ave", name="average mRNA life time", constant=False, sboTerm="SBO:0000348"),
                Parameter(sid="eff", name="translation efficiency", constant=True, value=20),
                Parameter(sid="kd_prot", name="kd_prot", constant=False, sboTerm="SBO:0000356"),
                Parameter(sid="tau_prot", name="protien half life", constant=True, value=10),
                Parameter(sid="a0_tr", name="a0_tr", constant=False, sboTerm="SBO:0000485"),
                Parameter(sid="ps_0", name="tps_repr", constant=True, value=0.0005),
                Parameter(sid="ps_a", name="tps_active", constant=True, value=0.5),
                Parameter(sid="KM", name="KM", constant=True, value=40),
                Parameter(sid="n", name="n", constant=True, value=2.0),
                Parameter(sid="a_tr", name="a_tr", constant=False, sboTerm="SBO:0000186"),
                ],

    rules=[

    ],

    reactions=[
        Reaction(sid="Reaction1", sboTerm="SBO:0000179", name="degradation of LacI transcripts",
                 reversible=False, equation="X -> ", formula=("kd_mRNA * X", None)),
Reaction(sid="Reaction2", sboTerm="SBO:0000179", name="degradation of TetR transcripts",
                 reversible=False, equation="Y -> ", formula=("kd_mRNA * Y", None)),
Reaction(sid="Reaction3", sboTerm="SBO:0000179", name="degradation of CI transcripts",
                 reversible=False, equation="Z -> ", formula=("kd_mRNA * Z", None)),
Reaction(sid="Reaction4", sboTerm="SBO:0000184", name="translation of LacI",
                 reversible=False, equation=" -> PX", formula=("k_tl * X", None)),
    ],
)

with tempfile.TemporaryDirectory() as tmp_path:
    results = create_model(
        models=model,
        output_dir=Path(tmp_path),
        tmp=False,
        units_consistency=False,
        sbml_level=3,
        sbml_version=1,
    )
    # show level and version and print SBML
    doc = read_sbml(source=results.sbml_path, validate=False)
    sbml = write_sbml(doc)
    print(sbml)
