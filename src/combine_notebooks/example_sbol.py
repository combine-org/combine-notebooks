"""
https://github.com/combine-org/combine-notebooks/issues/5
"""
import getpass

import loica as lc
import sbol3
from flapjack import Flapjack
from sbol_utilities import component


# %matplotlib inline

dna = fj.get("dna", name="Rep")
if len(dna) == 0:
    dna = fj.create("dna", name="Rep")
vector = fj.get("vector", name="Rep")
if len(vector) == 0:
    vector = fj.create("vector", name="Rep", dnas=dna.id)
study = fj.get("study", name="Loica testing")
if len(study) == 0:
    study = fj.create("study", name="Loica testing", description="Test")
media = fj.get("media", name="Loica")
if len(media) == 0:
    media = fj.create("media", name="Loica", description="Simulated loica media")
strain = fj.get("strain", name="Loica strain")
if len(strain) == 0:
    strain = fj.create("strain", name="Loica strain", description="Loica test strain")

cfp = fj.get("signal", name="CFP")
if len(cfp) == 0:
    cfp = fj.create(
        "signal",
        name="CFP",
        color="cyan",
        description="Simulated cyan fluorescent protein",
    )
yfp = fj.get("signal", name="YFP")
if len(yfp) == 0:
    yfp = fj.create(
        "signal",
        name="YFP",
        color="yellow",
        description="Simulated yellow fluorescent protein",
    )
rfp = fj.get("signal", name="RFP")
if len(rfp) == 0:
    rfp = fj.create(
        "signal",
        name="RFP",
        color="red",
        description="Simulated red fluorescent protein",
    )

biomass_signal = fj.get("signal", name="OD")


def growth_rate(t):
    return gompertz_growth_rate(t, 0.01, 1, 1, 1)


def biomass(t):
    return gompertz(t, 0.01, 1, 1, 1)


doc = sbol3.Document()
sbol3.set_namespace("https://github.com/Gonza10V")

ptet, ptet_seq = component.promoter(
    "L3S2P21_UPA20_pTetR_RiboJ",
    "GTCCCTCGGTACCAAATTCCAGAAAAGAGGCCTCCCGAAAGGGGGGCCTTTTTTCGTTTTGGTCCGTGCCTACTCTGGAAAATCTtccctatcagtgatagagattgacatccctatcagtgatagagatactgagcacatcagcaggacgcactgaccAGCTGTCACCGGATGTGCTTTCCGGTCTGATGAGTCCGTGAGGACGAAACAGCCTCTACAAATAATTTTGTTTAAGGCTCG",
    description="BASIC - Potvin pTet (based on B-P27-pTetR-F1)",
)
plac, plac_seq = component.promoter(
    "L3S2P11_UPA20_pLac_RiboJ10",
    "GTCCCTCGGTACCAAATTCCAGAAAAGAGACGCTTTCGAGCGTCTTTTTTCGTTTTGGTCCGTGCCTACTCTGGAAAATCTcctttcgtcttcacctcgagaattgtgagcggataacaattgacattgtgagcggataacaagatactgagcacatcagcaggacgcactgaccgaattcattAGCGCTCAACGGGTGTGCTTCCCGTTCTGATGAGTCCGTGAGGACGAAAGCGCCTCTACAAATAATTTTGTTTAAGGCTCG",
    description="BASIC - Potvin pLac (based on B-P39-pLac-F2)",
)
plam, plam_seq = component.promoter(
    "L3S1P13_UPA20_plambda_RiboJ51",
    "GTCCGACGAACAATAAGGCCTCCCTAACGGGGGGCCTTTTTTATTGATAACAAAAGTGCCTACTCTGGAAAATCTccgccgccctagacctagctgcaggtcgaggataaatatctaacaccgtgcgtgttgactattttacctctggcggtgataatggttgcatgtactagaattcattAGTAGTCACCGGCTGTGCTTGCCGGTCTGATGAGCCTGTGAAGGCGAAACTACCTCTACAAATAATTTTGTTTAAGGCTCG",
    description="BASIC - Potvin plambda (based on B-P41-pPhlF-F3)",
)

op_ptet = component.engineered_region(
    "operator_ptet", [ptet], description="LOICA Operator pTet"
)
op_plac = component.engineered_region(
    "operator_plac", [plac], description="LOICA Operator pLac"
)
op_plam = component.engineered_region(
    "operator_plam", [plam], description="LOICA Operator pLambda"
)

toplevels = [ptet, ptet_seq, plac, plac_seq, plam, plam_seq, op_ptet, op_plac, op_plam]
doc.add(toplevels)

operators = [op_ptet, op_plac, op_plam]

for obj in doc.objects:
    print(obj.identity)
report_sbol3 = doc.validate()
print(len(report_sbol3))

rbs1, rbs1_seq = component.rbs(
    "RBS1",
    "ttgaacaccgtcTCAGGTAAGTATCAGTTGTAAatcacacaggacta",
    description="BASIC Linker RBS1",
)
rbs2, rbs2_seq = component.rbs(
    "RBS2",
    "ttgaacaccgtcTCAGGTAAGTATCAGTTGTAAaaagaggggaaata",
    description="BASIC Linker RBS2",
)
rbs3, rbs3_seq = component.rbs(
    "RBS3",
    "ttgaacaccgtcTCAGGTAAGTATCAGTTGTAAaaagaggagaaata",
    description="BASIC Linker RBS3",
)

mven, mven_seq = component.cds(
    "mVenus",
    "GTCCCTCGGTACCAAATTCCAGAAAAGAGGCCTCCCGAAAGGGGGGCCTTTTTTCGTTTTGGTCCGTGCCTACTCTGGAAAATCTtccctatcagtgatagagattgacatccctatcagtgatagagatactgagcacatcagcaggacgcactgaccAGCTGTCACCGGATGTGCTTTCCGGTCTGATGAGTCCGTGAGGACGAAACAGCCTCTACAAATAATTTTGTTTAAGGCTCG",
    description="mVenus Coding Sequence from Potvin-Trottier pLPT119, no BasI site, no stop codon",
)
tetr, tetr_seq = component.cds(
    "TetR",
    "GTCCatgtccagattagataaaagtaaagtgattaacagcgcattagagctgcttaatgaggtcggaatcgaaggtttaacaacccgtaaactcgcccagaagctaggtgtagagcagcctacattgtattggcatgtaaaaaataagcgggctttgctcgacgccttagccattgagatgttagataggcaccatactcacttttgccctttagaaggggaaagctggcaagattttttacgtaataacgctaaaagttttagatgtgctttactaagtcatcgcgatggagcaaaagtacatttaggtacacggcctacagaaaaacagtatgaaactctcgaaaatcaattagcctttttatgccaacaaggtttttcactagagaatgcattatatgcactcagcgctgtggggcattttactttaggttgcgtattggaagatcaagagcatcaagtcgctaaagaagaaagggaaacacctactactgatagtatgccgccattattacgacaagctatcgaattatttgatcaccaaggtgcagagccagccttcttattcggccttgaattgatcatatgcggattagaaaaacaacttaaatgtgaaagtgggtctGGCTCG",
    description="TetR Coding Sequence from Potvin-Trottier pLPT119, no stop codon",
)
laci, laci_seq = component.cds(
    "LacI",
    "GTCCatggtgaatgtgaaaccagtaacgttatacgatgtcgcagagtatgccggtgtctcttatcagaccgtttcccgcgtggtgaaccaggccagccacgtttctgcgaaaacgcgggaaaaagtggaagcggcgatggcggagctgaattacattcccaaccgcgtggcacaacaactggcgggcaaacagtcgttgctgattggcgttgccacctccagtctggccctgcacgcgccgtcgcaaattgtcgcggcgattaaatctcgcgccgatcaactgggtgccagcgtggtggtgtcgatggtagaacgaagcggcgtcgaagcctgtaaagcggcggtgcacaatcttctcgcgcaacgcgtcagtgggctgatcattaactatccgctggatgaccaggatgccattgctgtggaagctgcctgcactaatgttccggcgttatttcttgatgtctctgaccagacacccatcaacagtattattttctcccatgaagacggtacgcgactgggcgtggagcatctggtcgcattgggtcaccagcaaatcgcgctgttagcgggcccattaagttctgtctcggcgcgtctgcgtctggctggctggcataaatatctcactcgcaatcaaattcagccgatagcggaacgggaaggcgactggagtgccatgtccggttttcaacaaaccatgcaaatgctgaatgagggcatcgttcccactgcgatgctggttgccaacgatcagatggcgctgggcgcaatgcgcgccattaccgagtccgggctgcgcgttggtgcggatatctcggtagtgggatacgacgataccgaagacagctcatgttatatcccgccgttaaccaccatcaaacaggattttcgcctgctggggcaaaccagcgtggaccgcttgctgcaactctctcagggccaggcggtgaagggcaatcagctgttgcccgtctcactggtgaaaagaaaaaccaccctggcgcccaatacgcaaaccgcctctccccgcgcgttggccgattcattaatgcagctggcacgacaggtttcccgactggaaagcgggcagGGCTCG",
    description="LacI Coding Sequence from Potvin-Trottier pLPT119, no stop codon",
)
lamr, lamr_seq = component.cds(
    "LamR",
    "GTCCCTCGGTACCAAATTCCAGAAAAGAGGCCTCCCGAAAGGGGGGCCTTTTTTCGTTTTGGTCCGTGCCTACTCTGGAAAATCTtccctatcagtgatagagattgacatccctatcagtgatagagatactgagcacatcagcaggacgcactgaccAGCTGTCACCGGATGTGCTTTCCGGTCTGATGAGTCCGTGAGGACGAAACAGCCTCTACAAATAATTTTGTTTAAGGCTCG",
    description="lambdaR Coding Sequence from Potvin-Trottier pLPT119, no stop codon",
)

m0050, m0050_seq = component.protein_stability_element(
    "M0050",
    "gctgctaacgacgaaaactacgctctggctgctTAAattgaacta",
    description="http://parts.igem.org/wiki/index.php?title=Part:BBa_M0050",
)
m0051, m0051_seq = component.protein_stability_element(
    "M0051",
    "gctgctaacgacgaaaactacaactacgctgacgcttctTAActa",
    description="http://parts.igem.org/wiki/index.php?title=Part:BBa_M0051",
)
m0052, m0052_seq = component.protein_stability_element(
    "M0052",
    "gctgctaacgacgaaaactacgctgacgcttctTAAattgaacta",
    description="http://parts.igem.org/wiki/index.php?title=Part:BBa_M0052",
)

ter1, ter1_seq = component.terminator(
    "TER1",
    "GTCCatttgtcctactcaggagagcgttcaccgacaaacaacagataaaacgaaaggcccagtctttcgactgagcctttcgttttatttgTAAGGCTCG",
    description="rrnB T1 terminator from Potvin-Trottier pLPT119, extra stop codon",
)

toplevels = [
    rbs1,
    rbs1_seq,
    rbs2,
    rbs2_seq,
    rbs3,
    rbs3_seq,
    mven,
    mven_seq,
    tetr,
    tetr_seq,
    laci,
    laci_seq,
    lamr,
    lamr_seq,
    m0050,
    m0050_seq,
    m0051,
    m0051_seq,
    m0052,
    m0052_seq,
    ter1,
    ter1_seq,
]
doc.add(toplevels)

# Automate design from lists of components, could be a collection
rbss = [rbs1]  # [rbs1, rbs2, rbs3]
cdss = [mven, tetr, laci, lamr]
degtags = [m0050]  # [m0050, m0051, m0052]
terminators = [ter1]

# Wrap it together
geneproducts = []
for rbs in rbss:
    for cds in cdss:
        for degtag in degtags:
            for ter in terminators:
                geneproduct = component.engineered_region(
                    f"geneproduct_{cds.display_id}_{degtag.display_id}_{ter.display_id}",
                    [rbs, cds, degtag, ter],
                    description="LOICA gene product",
                )
                doc.add(geneproduct)
                geneproducts.append(geneproduct)

for obj in doc.objects:
    print(obj.identity)
report_sbol3 = doc.validate()
print(len(report_sbol3))

rep = lc.GeneticNetwork(vector=vector.id[0])

tetr_reg = lc.Regulator(name="TetR", degradation_rate=1, sbol_comp=geneproducts[1])
laci_reg = lc.Regulator(
    name="LacI", degradation_rate=1, init_concentration=5, sbol_comp=geneproducts[2]
)
ci_reg = lc.Regulator(name="cI", degradation_rate=1, sbol_comp=geneproducts[3])
rep.add_regulator([tetr_reg, laci_reg, ci_reg])

mven_rep = lc.Reporter(
    name="mVenus",
    degradation_rate=1,
    signal_id=yfp.id[0],
    sbol_comp=geneproducts[0],
    color="yellow",
)
rep.add_reporter(mven_rep)

laci_not_tetr = lc.Hill1(
    input=laci_reg, output=tetr_reg, alpha=[100, 0], K=1, n=2, sbol_comp=op_plac
)
ci_not_laci = lc.Hill1(
    input=ci_reg, output=laci_reg, alpha=[100, 0], K=1, n=2, sbol_comp=op_plam
)
tetr_not_ci = lc.Hill1(
    input=tetr_reg, output=ci_reg, alpha=[100, 0], K=1, n=2, sbol_comp=op_ptet
)
tetr_not_mven = lc.Hill1(
    input=tetr_reg, output=mven_rep, alpha=[100, 0], K=1, n=2, sbol_comp=op_ptet
)
rep.add_operator([laci_not_tetr, ci_not_laci, tetr_not_ci, tetr_not_mven])
rep.draw()

repressilator_doc = rep.to_sbol(sbol_doc=doc)
for obj in repressilator_doc.objects:
    print(obj.identity)
report_sbol3 = repressilator_doc.validate()
print(len(report_sbol3))
