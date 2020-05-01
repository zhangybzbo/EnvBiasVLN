# Diagnosing-EnvBias-VLN
Feature resources of IJCAI 2020 paper "Diagnosing the Environment Bias in Vision-and-Language Navigation" and code snippet to adapt VLN codebase for using semantic features.

## Download semantic features
Download semantic features by
```
bash ./img_features/download.sh
```

Several kinds of semantic features will be downloaded:
1. `ImageNet.tsv` ImageNet-1000 features
2. `Detection.tsv` detected object features
3. `GT-Seg.tsv` ground-truth semantic segmentation features
4. `Learned-Seg.tsv` predicted semantic features


## To use the semantic features for your own VLN model
Put the downloaded image features in `img_features` into the image feature directory of your VLN codebase.

Put `modify.py` into your VLN codebase and run
```
python modify.py --CODE_ROOT $CODE_SRC --REPLACE_FEAT $SEMANTIC_FEAT
```
where `$CODE_SRC` is the path of your code source, `$SEMANTIC_FEAT` is the type of semantic feature you would like to use.

This process should make a copy of your original code and create a new version with the modifications for semantic features.
