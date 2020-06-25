import kiwi

# predictor_config = 'F:/openkiwi-auto/experiments/train_predictor.yaml'
# kiwi.train(predictor_config)
estimator_config = '/home/snchen/project/openkiwi-auto/experiments/train_nuqe.yaml'
kiwi.train(estimator_config)

predict_config = '/home/snchen/project/openkiwi-auto/experiments/predict_nuqe.yaml'
kiwi.predict(predict_config)

evaluate_config = '/home/snchen/project/openkiwi-auto/experiments/evaluate_nuqe.yaml'
kiwi.evaluate(evaluate_config)
