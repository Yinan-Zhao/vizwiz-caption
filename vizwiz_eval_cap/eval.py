"""
Adapted from MS COCO API 
https://github.com/cocodataset/cocoapi
"""
__author__ = 'nilavra'
from vizwiz_eval_cap.tokenizer.ptbtokenizer import PTBTokenizer
from vizwiz_eval_cap.bleu.bleu import Bleu
from vizwiz_eval_cap.meteor.meteor import Meteor
from vizwiz_eval_cap.rouge.rouge import Rouge
from vizwiz_eval_cap.cider.cider import Cider
from vizwiz_eval_cap.spice.spice import Spice


class VizWizEvalCap:
    def __init__(self, vizwiz, vizwizRes):
        self.evalImgs = []
        self.eval = {}
        self.imgToEval = {}
        self.vizwiz = vizwiz
        self.vizwizRes = vizwizRes
        self.params = {'image_id': vizwiz.getImgIds()}
        self.params = {'res_image_id': vizwizRes.getImgIds()}

    def evaluate(self):
        # imgIds = self.params['image_id']
        imgIds = self.params['res_image_id']
        # imgIds = self.vizwiz.getImgIds()
        gts = {}
        res = {}
        for imgId in imgIds:
            if self.vizwiz.imgToAnns[imgId]:
                gts[imgId] = self.vizwiz.imgToAnns[imgId]
                res[imgId] = self.vizwizRes.imgToAnns[imgId]

        # =================================================
        # Set up scorers
        # =================================================
        print('tokenization...')
        tokenizer = PTBTokenizer()
        gts  = tokenizer.tokenize(gts)
        res = tokenizer.tokenize(res)

        # =================================================
        # Set up scorers
        # =================================================
        print('setting up scorers...')
        scorers = [
            (Bleu(4),  ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]),
            (Rouge(),  "ROUGE_L"),
            (Cider(),  "CIDEr"),
            (Spice(),  "SPICE"),
            (Meteor(), "METEOR"),
        ]

        # =================================================
        # Compute scores
        # =================================================
        for scorer, method in scorers:
            print('computing %s score...'%(scorer.method()))
            score, scores = scorer.compute_score(gts, res)
            if type(method) == list:
                for sc, scs, m in zip(score, scores, method):
                    self.setEval(sc, m)
                    self.setImgToEvalImgs(scs, gts.keys(), m)
                    print("%s: %0.3f"%(m, sc))
            else:
                self.setEval(score, method)
                self.setImgToEvalImgs(scores, gts.keys(), method)
                print("%s: %0.3f"%(method, score))
        self.setEvalImgs()

    def setEval(self, score, method):
        self.eval[method] = score

    def setImgToEvalImgs(self, scores, imgIds, method):
        for imgId, score in zip(imgIds, scores):
            if not imgId in self.imgToEval:
                self.imgToEval[imgId] = {}
                self.imgToEval[imgId]["image_id"] = imgId
            self.imgToEval[imgId][method] = score

    def setEvalImgs(self):
        self.evalImgs = [eval for imgId, eval in self.imgToEval.items()]
