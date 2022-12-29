Module(body=[ImportFrom(module='sklearn.linear_model', names=[alias(name='LogisticRegression')], level=0), ImportFrom(module='tsfresh.feature_extraction.settings', names=[alias(name='MinimalFCParameters')], level=0), ImportFrom(module='etna.experimental.classification.feature_extraction', names=[alias(name='TSFreshFeatureExtractor')], level=0), FunctionDef(name='test_fit_transform_format', args=arguments(posonlyargs=[], args=[arg(arg='x_y')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='x', ctx=Store()), Name(id='y', ctx=Store())], ctx=Store())], value=Name(id='x_y', ctx=Load())), Assign(targets=[Name(id='feature_extractor', ctx=Store())], value=Call(func=Name(id='TSFreshFeatureExtractor', ctx=Load()), args=[], keywords=[keyword(arg='default_fc_parameters', value=Call(func=Name(id='MinimalFCParameters', ctx=Load()), args=[], keywords=[]))])), Assign(targets=[Name(id='x_tr', ctx=Store())], value=Call(func=Attribute(value=Name(id='feature_extractor', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='x', ctx=Load()), Name(id='y', ctx=Load())], keywords=[])), Assert(test=Compare(left=Attribute(value=Name(id='x_tr', ctx=Load()), attr='shape', ctx=Load()), ops=[Eq()], comparators=[Tuple(elts=[Constant(value=5), Constant(value=10)], ctx=Load())]))], decorator_list=[]), FunctionDef(name='test_sklearn_classifier_fit_on_extracted_features', args=arguments(posonlyargs=[], args=[arg(arg='x_y')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='x', ctx=Store()), Name(id='y', ctx=Store())], ctx=Store())], value=Name(id='x_y', ctx=Load())), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='LogisticRegression', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='feature_extractor', ctx=Store())], value=Call(func=Name(id='TSFreshFeatureExtractor', ctx=Load()), args=[], keywords=[keyword(arg='default_fc_parameters', value=Call(func=Name(id='MinimalFCParameters', ctx=Load()), args=[], keywords=[]))])), Assign(targets=[Name(id='x_tr', ctx=Store())], value=Call(func=Attribute(value=Name(id='feature_extractor', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='x', ctx=Load()), Name(id='y', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='x_tr', ctx=Load()), Name(id='y', ctx=Load())], keywords=[]))], decorator_list=[])], type_ignores=[])