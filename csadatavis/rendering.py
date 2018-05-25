"""
This module contains functionality for rendering the generated Vega-lite
specification for the visualizations into an HTML webpage.
"""

import chevron

PLOTS_TEMPLATE_FILE = "csadatavis/templates/plots.mustache"
SPEC_TAG = "spec"

def render_webpage_string(vegalite_spec: str) -> str:
    """
    Renders the given Vega-lite specification into a string of an HTML webpage
    that displays the specified plots.

    :param vegalite_spec str: The Vega-lite plot specification to create a
        webpage for.
    :returns: A string of a webpage with the specified plots.
    :rtype: str
    """
    with open(PLOTS_TEMPLATE_FILE, "r") as template_file:
        return chevron.render(template_file, {SPEC_TAG: vegalite_spec})
