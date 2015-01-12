import Orange

if __name__=="__main__":
    data = Orange.data.Table("training-2.txt")
    # print data.domain.variables
    # print data.domain.class_var
    # print data.domain.class_var.values
    # print type(data)
    # print data[0]
    # print data[0].get_class()

    #learner=Orange.classification.bayes.NaiveLearner()
    learner=Orange.classification.tree.C45Learner()
    classifier=learner(data)
    print classifier(data[50])

    learners = [learner]
    res=Orange.evaluation.testing.cross_validation(learners,data)
    CA=Orange.evaluation.scoring.CA(res)
    print CA[0]