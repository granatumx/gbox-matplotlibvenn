#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from granatum_sdk import Granatum
from matplotlib_venn_wordcloud import venn3_wordcloud
from matplotlib_venn import venn3


def main():
    gn = Granatum()

    set1 = gn.get_import('set1')
    set2 = gn.get_import('set2')
    set3 = gn.get_import('set3')

    maxScore = gn.get_arg('maxScore')
    minScore = gn.get_arg('minScore')

    labelSet1 = gn.get_arg("labelSet1")
    labelSet2 = gn.get_arg("labelSet2")
    labelSet3 = gn.get_arg("labelSet3")

    wordcloud = gn.get_arg("wordcloud")

    filtered_set1 = dict(filter(lambda elem: (elem[1] >= minScore) & (elem[1] <= maxScore), set1.items()))
    filtered_set2 = dict(filter(lambda elem: (elem[1] >= minScore) & (elem[1] <= maxScore), set2.items()))
    filtered_set3 = dict(filter(lambda elem: (elem[1] >= minScore) & (elem[1] <= maxScore), set3.items()))

    packedsets = [set(filtered_set1.keys()), set(filtered_set2.keys()), set(filtered_set3.keys())]

    plt.figure()

    caption = (
        'The area weighted Venn diagram is shown for the gene sets matching the criteria'
    )

    if wordcloud:
        venn3_wordcloud(packedsets, set_labels=(labelSet1, labelSet2, labelSet3))
    else:
        venn3(packedsets, set_labels=(labelSet1, labelSet2, labelSet3))

    gn.add_current_figure_to_results(caption, format="svg", dpi=100)

    gn.commit()


if __name__ == '__main__':
    main()
