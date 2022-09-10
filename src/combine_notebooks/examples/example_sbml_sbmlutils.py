# <markdowncell>
# Example script for creating SBML repressilator with sbmlutils.

# https://github.com/matthiaskoenig/libsbgn-python
# <codecell>
from pathlib import Path

from sbmlutils.factory import (
    AssignmentRule,
    Compartment,
    FactoryResult,
    Model,
    ModelUnits,
    Parameter,
    Reaction,
    Species,
    Units,
    create_model,
)
from sbmlutils.metadata import *
from sbmlutils.metadata import BQB

from combine_notebooks import RESULTS_DIR


# <codecell>
model = Model(
    "repressilator_sbmlutils",
    units=Units,
    model_units=ModelUnits(
        time=Units.second,
        substance=Units.mole,
        extent=Units.mole,
        volume=Units.litre,
    ),
    compartments=[
        Compartment(
            sid="cell",
            value=1.0,
            sboTerm="SBO:0000290",
            annotations=[(BQB.IS, "obo.go/GO:0005623")],
        )
    ],
    # obo.go/GO:3A0005623
    species=[
        Species(
            sid="PX",
            compartment="cell",
            name="LacI protein",
            sboTerm="SBO:0000252",
            initialAmount=0,
            hasOnlySubstanceUnits=True,
            annotations=[(BQB.IS, "uniprot/P03023")],
        ),
        Species(
            sid="PY",
            compartment="cell",
            name="TetR protein",
            sboTerm="SBO:0000252",
            initialAmount=0,
            hasOnlySubstanceUnits=True,
            annotations=[(BQB.IS, "uniprot/P04483")],
        ),
        Species(
            sid="PZ",
            compartment="cell",
            name="cI protein",
            sboTerm="SBO:0000252",
            initialAmount=0,
            hasOnlySubstanceUnits=True,
            annotations=[(BQB.IS, "uniprot/P03034")],
        ),
        Species(
            sid="X",
            compartment="cell",
            name="Lacl mRNA",
            sboTerm="SBO:0000250",
            initialAmount=20,
            hasOnlySubstanceUnits=True,
            annotations=[
                (BQB.IS_VERSION_OF, "chebi/CHEBI:33699"),
                (BQB.IS_VERSION_OF, "kegg.compound/C00046"),
                (BQB.ENCODES, "uniprot/P03023"),
            ],
        ),
        Species(
            sid="Y",
            compartment="cell",
            name="TetR mRNA",
            sboTerm="SBO:0000250",
            initialAmount=20,
            hasOnlySubstanceUnits=True,
            annotations=[
                (BQB.IS_VERSION_OF, "chebi/CHEBI:33699"),
                (BQB.IS_VERSION_OF, "kegg.compound/C00046"),
                (BQB.ENCODES, "uniprot/P04483"),
            ],
        ),
        Species(
            sid="Z",
            compartment="cell",
            name="cl mRNA",
            sboTerm="SBO:0000250",
            initialAmount=0,
            hasOnlySubstanceUnits=True,
            annotations=[
                (BQB.IS_VERSION_OF, "chebi/CHEBI:33699"),
                (BQB.IS_VERSION_OF, "kegg.compound/C00046"),
                (BQB.ENCODES, "uniprot/P03034"),
            ],
        ),
    ],
    parameters=[
        Parameter(sid="tau_mRNA", name="mRNA half life", constant=True, value=2.0),
        Parameter(sid="kd_mRNA", name="kd_mRNA", constant=False, sboTerm="SBO:0000356"),
        Parameter(sid="k_tl", name="k_tl", constant=False, sboTerm="SBO:0000016"),
        Parameter(
            sid="t_ave",
            name="average mRNA life time",
            constant=False,
            sboTerm="SBO:0000348",
        ),
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
        AssignmentRule(
            sid="kd_mRNA", value="ln(2) / tau_mRNA", name="kd_MRNA", sboTerm=None
        ),
        AssignmentRule(
            sid="t_ave", value="tau_mRNA / ln(2)", name="t_ave", sboTerm=None
        ),
        AssignmentRule(sid="k_tl", value="eff / t_ave", name="k_tl", sboTerm=None),
        AssignmentRule(
            sid="kd_prot", value="ln(2) / tau_prot", name="kd_prot", sboTerm=None
        ),
        AssignmentRule(sid="a0_tr", value="ps_0 * 60", name="a0_tr", sboTerm=None),
        AssignmentRule(
            sid="a_tr", value="(ps_a - ps_0) * 60", name="a_tr", sboTerm=None
        ),
    ],
    reactions=[
        Reaction(
            sid="Reaction1",
            sboTerm="SBO:0000179",
            name="degradation of LacI transcripts",
            reversible=False,
            equation="X -> ",
            formula=("kd_mRNA * X", None),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0006402")],
        ),
        Reaction(
            sid="Reaction2",
            sboTerm="SBO:0000179",
            name="degradation of TetR transcripts",
            reversible=False,
            equation="Y -> ",
            formula=("kd_mRNA * Y", None),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0006402")],
        ),
        Reaction(
            sid="Reaction3",
            sboTerm="SBO:0000179",
            name="degradation of CI transcripts",
            reversible=False,
            equation="Z -> ",
            formula=("kd_mRNA * Z", None),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0006402")],
        ),
        Reaction(
            sid="Reaction4",
            sboTerm="SBO:0000184",
            name="translation of LacI",
            reversible=False,
            equation=" -> PX [X]",
            formula=("k_tl * X", None),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0006412")],
        ),
        Reaction(
            sid="Reaction5",
            sboTerm="SBO:0000184",
            name="translation of TetR",
            reversible=False,
            equation=" -> PY [Y]",
            formula=("k_tl * Y", None),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0006412")],
        ),
        Reaction(
            sid="Reaction6",
            sboTerm="SBO:0000184",
            name="translation of CI",
            reversible=False,
            equation=" -> PZ [Z]",
            formula=("k_tl *Z", None),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0006412")],
        ),
        Reaction(
            sid="Reaction7",
            sboTerm="SBO:0000179",
            name="degradation of LacI",
            reversible=False,
            equation="PX -> ",
            formula=("kd_prot * PX", None),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0030163")],
        ),
        Reaction(
            sid="Reaction8",
            sboTerm="SBO:0000179",
            name="degradation of TetR",
            reversible=False,
            equation="PY -> ",
            formula=("kd_prot * PY", None),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0030163")],
        ),
        Reaction(
            sid="Reaction9",
            sboTerm="SBO:0000179",
            name="degradation of CI",
            reversible=False,
            equation="PZ -> ",
            formula=("kd_prot * PZ", None),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0030163")],
        ),
        Reaction(
            sid="Reaction10",
            sboTerm="SBO:0000183",
            name="transcription of LacI",
            reversible=False,
            equation=" -> X [PZ]",
            formula=(
                "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PZ, n))",
                None,
            ),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0006351")],
        ),
        Reaction(
            sid="Reaction11",
            sboTerm="SBO:0000183",
            name="transcription of TetR",
            reversible=False,
            equation=" -> Y [PX]",
            formula=(
                "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PX, n))",
                None,
            ),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0006351")],
        ),
        Reaction(
            sid="Reaction12",
            sboTerm="SBO:0000184",
            name="transcription of CI",
            reversible=False,
            equation=" -> Z [PY]",
            formula=(
                "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PY, n))",
                None,
            ),
            annotations=[(BQB.IS_VERSION_OF, "obo.go/GO:0006351")],
        ),
    ],
)

# <codecell>


def create_repressilator(sbml_path: Path) -> FactoryResult:
    """Create the repressilator model in the results_dir."""
    results = create_model(
        models=model,
        output_dir=sbml_path.parent,
        filename=sbml_path.name,
        tmp=False,
        units_consistency=False,
        sbml_level=2,
        sbml_version=3,
    )
    return results


# <codecell>
if __name__ == "__main__":
    # RESOURCES_DIR: Path = Path(__file__).parent / "resources"
    # RESULTS_DIR: Path = RESOURCES_DIR / "results"

    create_repressilator(sbml_path=RESULTS_DIR / "repressilator_sbmlutils.xml")
