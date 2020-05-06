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
where `$CODE_SRC` is the path of your code source, `$SEMANTIC_FEAT` is the type of semantic feature you would like to use (same notations as in our paper).

This process should make a copy of your original code and create a new version with the modifications for semantic features.

E.g., if you want to run the offical "Back Translation with Environmental Dropout" model using semantic features, after installing their repo from [**https://github.com/airsplay/R2R-EnvDrop**](https://github.com/airsplay/R2R-EnvDrop), copy the downloaded semantic features into their `img_features` folder. Put `modify.py` into the repo, and run:
```
python modify.py --CODE_ROOT r2r_src --REPLACE_FEAT GT-Seg
```
After that, when you follow their instructions for training, the model will be trained with our ground-truth semantic segmentation features.

### Result samples
When running the "EnvDrop(https://github.com/airsplay/R2R-EnvDrop)" agent (without back translation) using semantic features, we can get the following results:

| Feature type | Val seen (%) | Val unseen (%) | \|gap\| |
| ---- | :---: | :---: | :---:|
| ResNet | 58.4 | 45.8 | 12.6 |
| ImageNet | 45.6 | 45.4 | **0.2** |
| Detection | 51.2 | **49.9** | 1.3 |
| GT-Seg | 48.3 | 48.9 | **0.6** |
| Learned-Seg | 49.4 | 46.0 | 3.4 |