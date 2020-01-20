VizWiz Captions Evaluation
===================

Code for the VizWiz API and evaluation of generated captions.

### [View the tutorial Jupyter Notebook](demo_vizwiz_caption_evaluation.ipynb).

## Requirements ##
- python 3
- java 1.8.0 (for caption evaluation)


## Files ##
```./```
- ```demo_vizwiz_caption_evaluation.ipynb``` (tutorial notebook)

```./vizwiz_api```
- ```vizwiz.py```: This file contains the ```VizWiz``` API class that can be used to load VizWiz dataset JSON files and analyze them.


```./annotations```
- ```train.json``` (VizWiz-Captions training set)
- ```val.json``` (VizWiz-Captions validation set)
- Dataset shares the same data format as [MS COCO](http://cocodataset.org/#format-data).

```./results```
- ```fake_caption_val.json``` (an example of fake results for running demo)
- Dataset shares the same data format as [MS COCO](http://cocodataset.org/#format-data).


```./vizwiz_eval_cap```: The folder where all caption evaluation codes are stored.
- ```evals.py```: This file includes the ```VizWizEvalCap``` class that can be used to evaluate results on VizWiz.
- ```tokenizer```: Python wrapper of Stanford CoreNLP PTBTokenizer
- ```bleu```: Bleu evalutation codes
- ```rouge```: Rouge-L evaluation codes
- ```cider```: CIDEr evaluation codes
- ```spice```: SPICE evaluation codes

## Setup ##
- The primary VizWiz API is standalone.
- Download [annotation files](https://ivc.ischool.utexas.edu/VizWiz_final/caption/annotations.zip).
- For caption evaluation, you will first need to download the [Stanford CoreNLP 3.6.0](http://stanfordnlp.github.io/CoreNLP/index.html) code and models for use by SPICE. To do this, run:
    ```./get_stanford_models.sh```
    - To run shell scripts in Windows, you can setup [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). 
    - The command for Windows will then be ```bash get_stanford_models.sh``` 
- Note: SPICE will try to create a cache of parsed sentences in ./vizwiz_eval_cap/spice/cache/. This dramatically speeds up repeated evaluations. The cache directory can be moved by setting 'CACHE_DIR' in ./vizwiz_eval_cap/spice. In the same file, caching can be turned off by removing the '-cache' argument to 'spice_cmd'. 

## References ##
- [VizWiz Project](http://vizwiz.org)
- PTBTokenizer: We use the [Stanford Tokenizer](http://nlp.stanford.edu/software/tokenizer.shtml) which is included in [Stanford CoreNLP 3.4.1](http://nlp.stanford.edu/software/corenlp.shtml).
- BLEU: [BLEU: a Method for Automatic Evaluation of Machine Translation](http://www.aclweb.org/anthology/P02-1040.pdf)
- Meteor: [Project page](http://www.cs.cmu.edu/~alavie/METEOR/) with related publications. We use the latest version (1.5) of the [Code](https://github.com/mjdenkowski/meteor). Changes have been made to the source code to properly aggreate the statistics for the entire corpus.
- Rouge-L: [ROUGE: A Package for Automatic Evaluation of Summaries](http://anthology.aclweb.org/W/W04/W04-1013.pdf)
- CIDEr: [CIDEr: Consensus-based Image Description Evaluation](http://arxiv.org/pdf/1411.5726.pdf)
- SPICE: [SPICE: Semantic Propositional Image Caption Evaluation](https://arxiv.org/abs/1607.08822)

## Developers ##
- [Yinan Zhao (University of Texas at Austin)](http://www.cs.utexas.edu/~alexzhao/)
- [Nilavra Bhattacharya (University of Texas at Austin)](https://nilavra.in)

## Acknowledgement ##
This work is closely adapted from [MS COCO API](https://github.com/cocodataset/cocoapi) and [MS COCO Caption Evaluation API](https://github.com/tylin/coco-caption). 

#### Original Developers ##
- Xinlei Chen (CMU)
- Hao Fang (University of Washington)
- Tsung-Yi Lin (Cornell)
- Ramakrishna Vedantam (Virgina Tech)

#### Original Acknowledgements ##
- David Chiang (University of Norte Dame)
- Michael Denkowski (CMU)
- Alexander Rush (Harvard University)
