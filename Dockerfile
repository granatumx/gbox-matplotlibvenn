FROM granatumx/gbox-py-sdk:1.0.0

RUN pip install matplotlib-venn
RUN pip install matplotlib_venn_wordcloud

COPY . .

RUN ./GBOXtranslateVERinYAMLS.sh
RUN tar zcvf /gbox.tgz package.yaml yamls/*.yaml
