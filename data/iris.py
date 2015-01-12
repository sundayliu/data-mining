import Orange

if __name__=="__main__":
    data = Orange.data.Table("iris.tab")
    print data.domain.variables
    print data.domain.class_var
    print data.domain.class_var.values
    print type(data)
    print data[0]
    print data[0].get_class()

    learner=Orange.classification.bayes.NaiveLearner()
    classifier=learner(data)
    print classifier(data[50])

    learners = [learner]
    res=Orange.evaluation.testing.cross_validation(learners,data)
    CA=Orange.evaluation.scoring.CA(res)
    print CA[0]

    learners = [Orange.classification.bayes.NaiveLearner(),
        Orange.classification.tree.TreeLearner(),
        Orange.classification.neural.NeuralNetworkLearner(),
        Orange.ensemble.forest.RandomForestLearner(),
        Orange.classification.svm.SVMLearner()]
    res=Orange.evaluation.testing.cross_validation(learners,data)
    CAs = Orange.evaluation.scoring.CA(res)
    for i, CA in enumerate(CAs):
        print "{:s} CA is {:2%}".format(learners[i].name,CAs[i])