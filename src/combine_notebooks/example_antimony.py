"""Create repressilator with antimony.

http://antimony.sourceforge.net/
https://tellurium.readthedocs.io/en/latest/antimony.html
"""
from pathlib import Path

import antimony
import libsbml

from combine_notebooks.validation_sbml import validate_sbml


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
        end
    """
    print(model)

    status = antimony.loadAntimonyString(model)
    print(f"Antimony status: {status}")
    print(antimony.getLastError())
    sbml_str = antimony.getSBMLString()
    print(sbml_str)
    print(antimony.getSBMLWarnings())

    import libsbml

    doc = libsbml.readSBMLFromString(sbml_str)
    validate_sbml(doc)
    return doc


if __name__ == "__main__":
    # print(model)
    # RESOURCES_DIR: Path = Path(__file__).parent / "resources"
    # RESULTS_DIR: Path = RESOURCES_DIR / "results"
    from combine_notebooks import RESULTS_DIR

    create_repressilator(sbml_path=RESULTS_DIR / "repressilator_antimony.xml")
