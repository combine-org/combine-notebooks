# <markdowncell>
# Create repressilator with antimony.

# http://antimony.sourceforge.net/
# https://tellurium.readthedocs.io/en/latest/antimony.html

# <codecell>
from pathlib import Path

import antimony
import libsbml

from combine_notebooks.validation.validation_sbml import validate_sbml


# <codecell>
def create_repressilator(sbml_path: Path) -> libsbml.SBMLDocument:
    """Create repressilator with antimony."""
    model: str = """
        model antimony_repressilator
            # compartment
            compartment cell = 1
            # species
            species PX = 0
            species PY = 0
            species PZ = 0
            species X = 0
            species Y = 20
            species Z = 0
            # parameters
            beta = 0.2
            alpha0 = 0.2164
            alpha = 216.404
            eff = 20
            n = 2
            KM = 40
            tau_mRNA = 2
            tau_prot = 10
            ps_a = 0.5
            ps_0 = 0.0005
            # assignment rules
            t_ave := tau_mRNA/ln(2);
            beta := tau_mRNA/tau_prot;
            k_tl := eff/t_ave;
            a_tr := (ps_a - ps_0)*60;
            a0_tr := ps_0*60;
            kd_prot := ln(2)/tau_prot;
            kd_mRNA := ln(2)/tau_mRNA;
            alpha := a_tr*eff*tau_prot/(ln(2)*KM);
            alpha0 := (a0_tr*eff*tau_prot)/(ln(2)*KM);

            # reactions
            X ->; kd_mRNA*X;
            Y ->; kd_mRNA*Y;
            Z ->; kd_mRNA*Z;
            -> PX; k_tl*X;
            -> PY; k_tl*Y;
            -> PZ; k_tl*Z;
            PX ->; kd_prot*PX;
            PY ->; kd_prot*PY;
            PZ ->; kd_prot*PZ;
            -> X; a0_tr +a_tr *KM^n/(KM^n +PZ ^n);
            -> Y; a0_tr +a_tr *KM^n/(KM^n +PX ^n);
            -> Z; a0_tr +a_tr *KM^n/(KM^n +PY ^n);

            # annotations
            cell identity "http://identifiers.org/SBO:0000290"
            cell identity "http://identifiers.org/GO:0005623"
            PX identity "http://identifiers.org/SBO:0000252"
            PX identity "http://identifiers.org/uniprot/P03023"
            PY identity "http://identifiers.org/SBO:0000252"
            PY identity "http://identifiers.org/uniprot/P04483"
            PZ identity "http://identifiers.org/SBO:0000252"
            PZ identity "http://identifiers.org/uniprot/P03034"
            X identity "http://identifiers.org/SBO:0000250"
            X identity "http://identifiers.org/CHEBI:33699"
            X identity "http://identifiers.org/kegg.compound/C00046"
            X identity "http://identifiers.org/uniprot/P03023"
            Y identity "http://identifiers.org/SBO:0000250"
            Y identity "http://identifiers.org/CHEBI:33699"
            Y identity "http://identifiers.org/kegg.compound/C00046"
            Y identity "http://identifiers.org/uniprot/P04483"
            Z identity "http://identifiers.org/SBO:0000250"
            Z identity "http://identifiers.org/CHEBI:33699"
            Z identity "http://identifiers.org/kegg.compound/C00046"
            Z identity "http://identifiers.org/uniprot/P03034"
            tau_mRNA identity "http://identifiers.org/SBO:0000356"
            k_tl identity "http://identifiers.org/SBO:0000016"
            t_ave identity "http://identifiers.org/SBO:0000348"
            kd_prot identity "http://identifiers.org/SBO:0000356"
            a0_tr identity "http://identifiers.org/SBO:0000485"
            a_tr identity "http://identifiers.org/SBO:0000186"
            _J0 identity "http://identifiers.org/SBO:0000179"
            _J0 identity "http://identifiers.org/GO:0006402"
            _J1 identity "http://identifiers.org/SBO:0000179"
            _J1 identity "http://identifiers.org/GO:0006402"
            _J2 identity "http://identifiers.org/SBO:0000179"
            _J2 identity "http://identifiers.org/GO:0006402"
            _J3 identity "http://identifiers.org/SBO:0000184"
            _J3 identity "http://identifiers.org/GO:0006412"
            _J4 identity "http://identifiers.org/SBO:0000184"
            _J4 identity "http://identifiers.org/GO:0006412"
            _J5 identity "http://identifiers.org/SBO:0000184"
            _J5 identity "http://identifiers.org/GO:0006412"
            _J6 identity "http://identifiers.org/SBO:0000179"
            _J6 identity "http://identifiers.org/GO:0030163"
            _J7 identity "http://identifiers.org/SBO:0000179"
            _J7 identity "http://identifiers.org/GO:0030163"
            _J8 identity "http://identifiers.org/SBO:0000179"
            _J8 identity "http://identifiers.org/GO:0030163"
            _J9 identity "http://identifiers.org/SBO:0000183"
            _J9 identity "http://identifiers.org/GO:0006351"
            _J10 identity "http://identifiers.org/SBO:0000183"
            _J10 identity "http://identifiers.org/GO:0006351"
            _J11 identity "http://identifiers.org/SBO:0000184"
            _J11 identity "http://identifiers.org/GO:0006351"

        end
    """
    print(model)

    status = antimony.loadAntimonyString(model)
    print(f"Antimony status: {status}")
    print(antimony.getLastError())
    sbml_str = antimony.getSBMLString()
    print(sbml_str)
    print(antimony.getSBMLWarnings())

    # validation
    doc = libsbml.readSBMLFromString(sbml_str)
    validate_sbml(doc)

    # write SBML
    libsbml.writeSBMLToFile(doc, str(sbml_path))

    return doc


# <codecell>
if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR

    create_repressilator(sbml_path=RESULTS_DIR / "repressilator_antimony.xml")
