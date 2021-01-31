#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from granatum_sdk import Granatum
from matplotlib_venn_wordcloud import venn3_wordcloud
from matplotlib_venn import venn3, venn3_circles
import matplotlib.patheffects as path_effects


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
    merged_frequencies = {**filtered_set1, **filtered_set2, **filtered_set3}

    packedsets = [set(filtered_set1.keys()), set(filtered_set2.keys()), set(filtered_set3.keys())]

    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(5,4)

    caption = (
        'The area weighted Venn diagram is shown for the gene sets matching the criteria'
    )

    if wordcloud:
        out = venn3_wordcloud(packedsets, set_labels=(labelSet1, labelSet2, labelSet3), wordcloud_kwargs=dict(max_font_size=36), word_to_frequency=merged_frequencies, ax=ax)
        for text in out.set_labels:
            if text:
                text.set_fontsize(18)
        for text in out.subset_labels:
            if text:
                text.set_fontsize(16)
                text.set_path_effects([path_effects.SimpleLineShadow(), path_effects.Normal()])
    else:
        out = venn3(packedsets, set_labels=(labelSet1, labelSet2, labelSet3))
        venn3_circles(packedsets, linestyle='dashed', linewidth=1, color="black")
        for text in out.set_labels:
            if text:
                text.set_fontsize(18)
        for text in out.subset_labels:
            if text:
                text.set_fontsize(16)
                text.set_path_effects([path_effects.SimpleLineShadow(), path_effects.Normal()])

    gn.add_current_figure_to_results(caption, dpi=300)

    gn.commit()


if __name__ == '__main__':
    main()
