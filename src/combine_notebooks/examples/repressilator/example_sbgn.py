# <markdowncell>
# Create the repressilator from libsbgn.
#
# See on libsbgn-python: https://github.com/matthiaskoenig/libsbgn-python

# <codecell>
from pathlib import Path

import IPython
import libsbgnpy.libsbgn as libsbgn
from IPython.core.display import HTML
from IPython.display import Image
from libsbgnpy.libsbgnTypes import ArcClass, GlyphClass, Language, Orientation
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer


# <codecell>
def pprint_xml(xml_str: str) -> None:
    """Create highlighted xml."""
    IPython.display.display(
        HTML(
            '<style type="text/css">{}</style>{}'.format(
                HtmlFormatter().get_style_defs(".highlight"),
                highlight(xml_str, PythonLexer(), HtmlFormatter()),
            )
        )
    )


# <codecell>
def create_repressilator(sbgn_path: Path) -> libsbgn.sbgn:
    """Create repressilator SBGN using libsbgn."""
    # create empty sbgn
    sbgn: libsbgn.sbgn = libsbgn.sbgn()

    # create map, set language and set in sbgn
    map = libsbgn.map()
    map.set_language(Language.PD)
    sbgn.set_map(map)

    # create a bounding box for the map
    box = libsbgn.bbox(x=0, y=0, w=363, h=253)
    map.set_bbox(box)

    # create some glyphs
    # glyphs with labels
    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph3")
    g.set_bbox(libsbgn.bbox(x=530, y=25, w=36, h=36))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph2")
    g.set_bbox(libsbgn.bbox(x=180, y=25, w=36, h=36))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph11")
    g.set_bbox(libsbgn.bbox(x=455, y=265, w=36, h=36))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph12")
    g.set_bbox(libsbgn.bbox(x=625, y=125, w=36, h=36))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph5")
    g.set_bbox(libsbgn.bbox(x=273, y=33, w=20, h=20))
    g.add_port(libsbgn.port(y="43.0", x="263.0", id="glyph5.1"))
    g.add_port(libsbgn.port(y="43.0", x="303.0", id="glyph5.2"))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph10")
    g.set_bbox(libsbgn.bbox(x=545, y=378.61728, w=36, h=36))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph15")
    g.set_bbox(libsbgn.bbox(x=800, y=125, w=36, h=36))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph25")
    g.set_bbox(libsbgn.bbox(x=800, y=450, w=36, h=36))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph16")
    g.set_bbox(libsbgn.bbox(x=808, y=228, w=20, h=20))
    g.add_port(libsbgn.port(y="218.0", x="818.0", id="glyph16.1"))
    g.add_port(libsbgn.port(y="258.0", x="818.0", id="glyph16.2"))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.MACROMOLECULE, id="glyph8")
    g.set_label(libsbgn.label(text="Laclp"))
    g.set_bbox(libsbgn.bbox(x=342, y=20.5, w=72, h=45))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph30")
    g.set_bbox(libsbgn.bbox(x=275, y=625, w=36, h=36))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph14")
    g.set_bbox(libsbgn.bbox(x=283, y=558, w=20, h=20))
    g.add_port(libsbgn.port(y="588.0", x="293.0", id="glyph14.2"))
    g.add_port(libsbgn.port(y="548.0", x="293.0", id="glyph14.1"))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph17")
    g.set_bbox(libsbgn.bbox(x=115, y=480, w=36, h=36))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph19")
    g.set_bbox(libsbgn.bbox(x=350, y=378.61728, w=36, h=36))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph18")
    g.set_bbox(libsbgn.bbox(x=20, y=378.617, w=36, h=36))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.MACROMOLECULE, id="glyph27")
    g.set_label(libsbgn.label(text="Clp"))
    g.set_bbox(libsbgn.bbox(x=782, y=280.5, w=72, h=45))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.MACROMOLECULE, id="glyph24")
    g.set_label(libsbgn.label(text="Tetp"))
    g.set_bbox(libsbgn.bbox(x=257, y=475.5, w=72, h=45))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph13")
    g.set_label(libsbgn.label(text="Laclp"))
    g.set_bbox(libsbgn.bbox(y="386.61728", x="618.0", h="20.0", w="20.0"))
    g.add_port(libsbgn.port(y="396.61728", x="608.0", id="glyph13.1"))
    g.add_port(libsbgn.port(y="396.61728", x="648.0", id="glyph13.2"))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph26")
    g.set_label(libsbgn.label(text="Laclp"))
    g.set_bbox(libsbgn.bbox(y="386.61728", x="808.0", h="20.0", w="20.0"))
    g.add_port(libsbgn.port(y="376.61728", x="818.0", id="glyph26.1"))
    g.add_port(libsbgn.port(y="416.61728", x="818.0", id="glyph26.2"))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.SOURCE_AND_SINK, id="glyph22")
    g.set_bbox(libsbgn.bbox(y="528.6667", x="700.0", h="36.0", w="36.0"))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.NUCLEIC_ACID_FEATURE, id="glyph21")
    g.set_label(libsbgn.label(text="Clm"))
    g.set_bbox(libsbgn.bbox(y="374.117", x="682.0", h="45.0", w="72.0"))
    """
    <glyph id="glyph21a" class="unit of information">
                    <label text="ct:mRNA"/>
                    <bbox y="365.367" x="686.25" h="17.5" w="63.5"/>
                </glyph>
    """
    g1 = libsbgn.glyph(id="glyph21a", class_=GlyphClass.UNIT_OF_INFORMATION)

    g1.set_label(libsbgn.label(text="ct:mRNA"))
    g1.set_bbox(libsbgn.bbox(y="365.367", x="686.25", h="17.5", w="63.5"))
    map.add_glyph(g)
    g.add_glyph(g1)
    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph28")
    g.set_bbox(libsbgn.bbox(y="456.6667", x="708.0", h="20.0", w="20.0"))
    g.add_port(libsbgn.port(y="486.6667", x="718.0", id="glyph28.2"))
    g.add_port(libsbgn.port(y="446.6667", x="718.0", id="glyph28.1"))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph32")
    g.set_bbox(libsbgn.bbox(y="386.61728", x="288.0", h="20.0", w="20.0"))
    g.add_port(libsbgn.port(y="396.61728", x="318.0", id="glyph32.2"))
    g.add_port(libsbgn.port(y="396.61728", x="278.0", id="glyph32.1"))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph9")
    g.set_bbox(libsbgn.bbox(y="386.61728", x="110.0", h="20.0", w="20.0"))
    g.add_port(libsbgn.port(y="396.61728", x="100.0", id="glyph9.1"))
    g.add_port(libsbgn.port(y="396.61728", x="140.0", id="glyph9.2"))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.NUCLEIC_ACID_FEATURE, id="glyph1")
    g.set_label(libsbgn.label(text="Tetm"))
    g.set_bbox(libsbgn.bbox(y="374.117", x="167.0", h="45.0", w="72.0"))
    g1 = libsbgn.glyph(id="glyph1a", class_=GlyphClass.UNIT_OF_INFORMATION)

    g1.set_label(libsbgn.label(text="ct:mRNA"))
    g1.set_bbox(libsbgn.bbox(y="365.367", x="171.25", h="17.5", w="63.5"))
    """
    <glyph id="glyph1a" class="unit of information">
                    <label text="ct:mRNA"/>
                    <bbox y="365.367" x="171.25" h="17.5" w="63.5"/>
                </glyph>
    """
    map.add_glyph(g)
    g.add_glyph(g1)

    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph23")
    g.set_bbox(libsbgn.bbox(y="488.0", x="194.0", h="20.0", w="20.0"))
    g.add_port(libsbgn.port(y="498.0", x="184.0", id="glyph23.1"))
    g.add_port(libsbgn.port(y="498.0", x="224.0", id="glyph23.2"))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph4")
    g.set_bbox(libsbgn.bbox(y="33.0", x="463.0", h="20.0", w="20.0"))
    g.add_port(libsbgn.port(y="43.0", x="493.0", id="glyph4.2"))
    g.add_port(libsbgn.port(y="43.0", x="453.0", id="glyph4.1"))
    map.add_glyph(g)

    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph7")
    g.set_label(libsbgn.label(text="Tetm"))
    g.set_bbox(libsbgn.bbox(y="208.0", x="463.0", h="20.0", w="20.0"))
    g.add_port(libsbgn.port(y="238.0", x="473.0", id="glyph7.2"))
    g.add_port(libsbgn.port(y="198.0", x="473.0", id="glyph7.1"))
    map.add_glyph(g)

    # """
    # <glyph id="glyph20" class="nucleic acid feature">
    #     <label text="Laclm"/>
    #     <bbox y="120.5" x="437.0" h="45.0" w="72.0"/>
    #     <glyph id="glyph20a" class="unit of information">
    #         <label text="ct:mRNA"/>
    #         <bbox y="111.75" x="441.25" h="17.5" w="63.5"/>
    #     </glyph>
    # </glyph>
    # """

    g = libsbgn.glyph(class_=GlyphClass.NUCLEIC_ACID_FEATURE, id="glyph20")
    g.set_label(libsbgn.label(text="Laclm"))
    g.set_bbox(libsbgn.bbox(y="120.5", x="437.0", h="45.0", w="72.0"))
    g1 = libsbgn.glyph(id="glyph20a", class_=GlyphClass.UNIT_OF_INFORMATION)

    g1.set_label(libsbgn.label(text="ct:mRNA"))
    g1.set_bbox(libsbgn.bbox(y="111.75", x="441.25", h="17.5", w="63.5"))
    # TODO: add nested glyphs
    # g.add_glyph()
    map.add_glyph(g)
    g.add_glyph(g1)

    g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph6")

    g.set_bbox(libsbgn.bbox(y="133.0", x="553.0", h="20.0", w="20.0"))
    g.add_port(libsbgn.port(y="143.0", x="583.0", id="glyph6.2"))
    g.add_port(libsbgn.port(y="143.0", x="543.0", id="glyph6.1"))
    map.add_glyph(g)

    # g = libsbgn.glyph(class_=GlyphClass.PROCESS, id="glyph6")
    # g.set_label(libsbgn.label(text="Tetm"))
    # g.set_bbox(libsbgn.bbox(y="133.0", x="553.0", h="20.0", w="20.0"))
    # map.add_glyph(g)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph4.2", source="glyph3", id="arc1"
    )
    a.set_start(libsbgn.startType(y="43.0", x="530.0"))
    a.set_end(libsbgn.endType(y="43.0", x="493.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.PRODUCTION, target="glyph2", source="glyph5.1", id="arc4"
    )
    a.set_start(libsbgn.startType(y="43.0", x="263.0"))
    a.set_end(libsbgn.endType(y="43.0", x="216.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph7.2", source="glyph11", id="arc6"
    )
    a.set_start(libsbgn.startType(y="265.0", x="473.0"))
    a.set_end(libsbgn.endType(y="238.0", x="473.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.PRODUCTION, target="glyph12", source="glyph6.2", id="arc9"
    )
    a.set_start(libsbgn.startType(y="143.0", x="583.0"))
    a.set_end(libsbgn.endType(y="143.0", x="625.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph5.2", source="glyph8", id="arc3"
    )
    a.set_start(libsbgn.startType(y="43.0", x="342.0"))
    a.set_end(libsbgn.endType(y="43.0", x="303.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph13.1", source="glyph10", id="arc19"
    )
    a.set_start(libsbgn.startType(y="396.61728", x="581.0"))
    a.set_end(libsbgn.endType(y="396.61728", x="608.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.PRODUCTION, target="glyph8", source="glyph4.1", id="arc22"
    )
    a.set_start(libsbgn.startType(y="43.0", x="453.0"))
    a.set_end(libsbgn.endType(y="43.0", x="414.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph15", source="glyph16.1", id="arc24"
    )
    a.set_start(libsbgn.startType(y="218.0", x="818.0"))
    a.set_end(libsbgn.endType(y="161.0", x="818.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.PRODUCTION, target="glyph27", source="glyph26.1", id="arc10"
    )
    a.set_start(libsbgn.startType(y="376.61728", x="818.0"))
    a.set_end(libsbgn.endType(y="325.5", x="818.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph26.2", source="glyph25", id="arc11"
    )
    a.set_start(libsbgn.startType(y="450.0", x="818.0"))
    a.set_end(libsbgn.endType(y="416.61728", x="818.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph16.2", source="glyph27", id="arc13"
    )
    a.set_start(libsbgn.startType(y="280.5", x="818.0"))
    a.set_end(libsbgn.endType(y="258.0", x="818.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.INHIBITION, target="glyph32", source="glyph8", id="arc15"
    )
    a.set_start(libsbgn.startType(y="65.5", x="353.74677"))
    a.set_end(libsbgn.endType(y="386.61728", x="297.89154"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.PRODUCTION, target="glyph30", source="glyph14.2", id="arc16"
    )
    a.set_start(libsbgn.startType(y="588.0", x="293.0"))
    a.set_end(libsbgn.endType(y="625.0", x="293.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph14.1", source="glyph24", id="arc17"
    )
    a.set_start(libsbgn.startType(y="520.5", x="293.0"))
    a.set_end(libsbgn.endType(y="548.0", x="293.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph23.1", source="glyph17", id="arc20"
    )
    a.set_start(libsbgn.startType(y="498.0", x="151.0"))
    a.set_end(libsbgn.endType(y="498.0", x="184.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.PRODUCTION, target="glyph24", source="glyph23.2", id="arc21"
    )
    a.set_start(libsbgn.startType(y="498.0", x="224.0"))
    a.set_end(libsbgn.endType(y="498.0", x="257.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph32.2", source="glyph19", id="arc25"
    )
    a.set_start(libsbgn.startType(y="396.61728", x="350.0"))
    a.set_end(libsbgn.endType(y="396.61728", x="318.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.PRODUCTION, target="glyph18", source="glyph9.1", id="arc28"
    )
    a.set_start(libsbgn.startType(y="396.61728", x="100.0"))
    a.set_end(libsbgn.endType(y="396.617", x="56.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.INHIBITION, target="glyph7", source="glyph27", id="arc2"
    )
    a.set_start(libsbgn.startType(y="280.5", x="791.871"))
    a.set_end(libsbgn.endType(y="217.66245", x="483.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.INHIBITION, target="glyph13", source="glyph24", id="arc23"
    )
    a.set_start(libsbgn.startType(y="498.77063", x="329.0"))
    a.set_end(libsbgn.endType(y="406.61728", x="627.2619"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.PRODUCTION, target="glyph21", source="glyph13.2", id="arc5"
    )
    a.set_start(libsbgn.startType(y="396.61728", x="648.0"))
    a.set_end(libsbgn.endType(y="396.617", x="682.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.NECESSARY_STIMULATION,
        target="glyph26",
        source="glyph21",
        id="arc7",
    )
    a.set_start(libsbgn.startType(y="396.617", x="754.0"))
    a.set_end(libsbgn.endType(y="396.61728", x="808.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.PRODUCTION, target="glyph22", source="glyph28.2", id="arc8"
    )
    a.set_start(libsbgn.startType(y="486.6667", x="718.0"))
    a.set_end(libsbgn.endType(y="528.6667", x="718.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph28.1", source="glyph21", id="arc12"
    )
    a.set_start(libsbgn.startType(y="419.117", x="718.0"))
    a.set_end(libsbgn.endType(y="446.6667", x="718.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.PRODUCTION, target="glyph1", source="glyph32.1", id="arc14"
    )
    a.set_start(libsbgn.startType(y="396.61728", x="278.0"))
    a.set_end(libsbgn.endType(y="396.617", x="239.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph9.2", source="glyph1", id="arc18"
    )
    a.set_start(libsbgn.startType(y="396.617", x="167.0"))
    a.set_end(libsbgn.endType(y="396.61728", x="140.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.NECESSARY_STIMULATION,
        target="glyph23",
        source="glyph1",
        id="arc26",
    )
    a.set_start(libsbgn.startType(y="419.117", x="203.22192"))
    a.set_end(libsbgn.endType(y="488.0", x="203.90137"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.NECESSARY_STIMULATION,
        target="glyph4",
        source="glyph20",
        id="arc27",
    )
    a.set_start(libsbgn.startType(y="120.5", x="473.0"))
    a.set_end(libsbgn.endType(y="53.0", x="473.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.PRODUCTION, target="glyph20", source="glyph7.1", id="arc29"
    )
    a.set_start(libsbgn.startType(y="198.0", x="473.0"))
    a.set_end(libsbgn.endType(y="165.5", x="473.0"))
    map.add_arc(a)

    a = libsbgn.arc(
        class_=ArcClass.CONSUMPTION, target="glyph6.1", source="glyph20", id="arc30"
    )
    a.set_start(libsbgn.startType(y="143.0", x="509.0"))
    a.set_end(libsbgn.endType(y="143.0", x="543.0"))
    map.add_arc(a)

    f_out = str(sbgn_path)
    sbgn.write_file(f_out)

    # render SBGN
    from libsbgnpy import render

    f_png: str = str(sbgn_path.parent / f"{sbgn_path.stem}.png")
    render.render_sbgn(sbgn, image_file=f_png, file_format="png")
    Image(f_png, width=300)
    return sbgn


# <codecell>
if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR

    RESULTS_DIR
    sbgn: libsbgn.sbgn = create_repressilator(
        sbgn_path=RESULTS_DIR / "repressilator.sbgn"
    )
