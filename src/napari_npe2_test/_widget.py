"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/plugins/stable/guides.html#widgets

Replace code below according to your needs.
"""
from magicgui import magic_factory

@magic_factory
def example_magic_widget(image: "napari.types.ImageData") -> "napari.types.LabelsData":
    return example_function_widget(image)


# Uses the `autogenerate: true` flag in the plugin manifest
# to indicate it should be wrapped as a magicgui to autogenerate
# a widget.
def example_function_widget(image: "napari.types.ImageData") -> "napari.types.LabelsData":
    from skimage.filters import threshold_otsu
    binary_image = image > threshold_otsu(image)

    from skimage.measure import label
    return label(binary_image)

