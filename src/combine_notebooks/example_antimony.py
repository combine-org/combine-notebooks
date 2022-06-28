"""Create repressilator with antimony.

http://antimony.sourceforge.net/
"""
from pathlib import Path


def create_repressilator(sbml_path: Path) -> None:
    """Create repressilator with antimony."""
    model: str = '''
        model antimony_repressilator:
            #compartment
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
            t_ave = tau_mRNA/ln(2)
            beta = tau_mRNA/tau_prot
            k_tl = eff/t_ave
            a_tr = (ps_a - ps_0)*60
            a0_tr = ps_0*60
            kd_prot = ln(2)/tau_prot
            kd_mRNA = ln(2)/tau_mRNA
            alpha = (a_tr*eff*tau_prot)/(ln(2)*KM)
            alpha0 = (a0_tr*eff*tau_prot)/(ln(2)*KM)
            # reactions
            X ->
            Y ->
            Z ->
            -> PX
            -> PY
            -> PZ
            PX ->
            PY ->
            PZ ->
            -> X
            -> Y
            -> Z
        end
    '''
    print(model)


if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR
    create_repressilator(sbml_path=RESULTS_DIR / "repressilator_antimony.xml")
