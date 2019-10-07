import h2o
# h2o.init()

 # Get help
# 7 help(h2o.estimators.glm.H2OGeneralizedLinearEstimator)
# 8 help(h2o.estimators.gbm.H2OGradientBoostingEstimator)
# help(h2o.estimators.deeplearning.
# H2ODeepLearningEstimator)

# 11 # Show a demo
# print(h2o.demo("glm"))
# print(h2o.demo("gbm"))

# print(h2o.demo("deeplearning"))

from h2o.estimators.deeplearning import H2ODeepLearningEstimator
h2o.init()
train = h2o.import_file("https://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
print(train)
splits = train.split_frame(ratios=[0.75], seed=1234)
dl = H2ODeepLearningEstimator(distribution="quantile",quantile_alpha=0.8)
dl.train(x=[0,1], y="petal_len", training_frame=splits[0])
print(dl.predict(splits[1]))