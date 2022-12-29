Module(body=[Expr(value=Constant(value='\nMIT LICENCE\n\nCopyright (c) 2016 Maximilian Christ, Blue Yonder GmbH\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\ndocumentation files (the "Software"), to deal in the Software without restriction, including without limitation the\nrights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\npersons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the\nSoftware.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE\nWARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\nCOPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR\nOTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n')), ImportFrom(module='multiprocessing', names=[alias(name='Pool')], level=0), Import(names=[alias(name='warnings')]), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='functools', names=[alias(name='partial'), alias(name='reduce')], level=0), ImportFrom(module='statsmodels.stats.multitest', names=[alias(name='multipletests')], level=0), ImportFrom(module='etna.libs.tsfresh', names=[alias(name='defaults')], level=0), ImportFrom(module='etna.libs.tsfresh.significance_tests', names=[alias(name='target_binary_feature_real_test'), alias(name='target_real_feature_binary_test'), alias(name='target_real_feature_real_test'), alias(name='target_binary_feature_binary_test')], level=0), ImportFrom(module='etna.libs.tsfresh.distribution', names=[alias(name='initialize_warnings_in_workers')], level=0), FunctionDef(name='calculate_relevance_table', args=arguments(posonlyargs=[], args=[arg(arg='X'), arg(arg='y'), arg(arg='ml_task'), arg(arg='multiclass'), arg(arg='n_significant'), arg(arg='n_jobs'), arg(arg='show_warnings'), arg(arg='chunksize'), arg(arg='test_for_binary_target_binary_feature'), arg(arg='test_for_binary_target_real_feature'), arg(arg='test_for_real_target_binary_feature'), arg(arg='test_for_real_target_real_feature'), arg(arg='fdr_level'), arg(arg='hypotheses_independent')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value='auto'), Constant(value=False), Constant(value=1), Attribute(value=Name(id='defaults', ctx=Load()), attr='N_PROCESSES', ctx=Load()), Attribute(value=Name(id='defaults', ctx=Load()), attr='SHOW_WARNINGS', ctx=Load()), Attribute(value=Name(id='defaults', ctx=Load()), attr='CHUNKSIZE', ctx=Load()), Attribute(value=Name(id='defaults', ctx=Load()), attr='TEST_FOR_BINARY_TARGET_BINARY_FEATURE', ctx=Load()), Attribute(value=Name(id='defaults', ctx=Load()), attr='TEST_FOR_BINARY_TARGET_REAL_FEATURE', ctx=Load()), Attribute(value=Name(id='defaults', ctx=Load()), attr='TEST_FOR_REAL_TARGET_BINARY_FEATURE', ctx=Load()), Attribute(value=Name(id='defaults', ctx=Load()), attr='TEST_FOR_REAL_TARGET_REAL_FEATURE', ctx=Load()), Attribute(value=Name(id='defaults', ctx=Load()), attr='FDR_LEVEL', ctx=Load()), Attribute(value=Name(id='defaults', ctx=Load()), attr='HYPOTHESES_INDEPENDENT', ctx=Load())]), body=[Expr(value=Constant(value='\n    Calculate the relevance table for the features contained in feature matrix `X` with respect to target vector `y`.\n    The relevance table is calculated for the intended machine learning task `ml_task`.\n\n    To accomplish this for each feature from the input pandas.DataFrame an univariate feature significance test\n    is conducted. Those tests generate p values that are then evaluated by the Benjamini Hochberg procedure to\n    decide which features to keep and which to delete.\n\n    We are testing\n\n        :math:`H_0` = the Feature is not relevant and should not be added\n\n    against\n\n        :math:`H_1` = the Feature is relevant and should be kept\n\n    or in other words\n\n        :math:`H_0` = Target and Feature are independent / the Feature has no influence on the target\n\n        :math:`H_1` = Target and Feature are associated / dependent\n\n    When the target is binary this becomes\n\n        :math:`H_0 = \\left( F_{\\text{target}=1} = F_{\\text{target}=0} \\right)`\n\n        :math:`H_1 = \\left( F_{\\text{target}=1} \\neq F_{\\text{target}=0} \\right)`\n\n    Where :math:`F` is the distribution of the target.\n\n    In the same way we can state the hypothesis when the feature is binary\n\n        :math:`H_0 =  \\left( T_{\\text{feature}=1} = T_{\\text{feature}=0} \\right)`\n\n        :math:`H_1 = \\left( T_{\\text{feature}=1} \\neq T_{\\text{feature}=0} \\right)`\n\n    Here :math:`T` is the distribution of the target.\n\n    TODO: And for real valued?\n\n    :param X: Feature matrix in the format mentioned before which will be reduced to only the relevant features.\n              It can contain both binary or real-valued features at the same time.\n    :type X: pandas.DataFrame\n\n    :param y: Target vector which is needed to test which features are relevant. Can be binary or real-valued.\n    :type y: pandas.Series or numpy.ndarray\n\n    :param ml_task: The intended machine learning task. Either `\'classification\'`, `\'regression\'` or `\'auto\'`.\n                    Defaults to `\'auto\'`, meaning the intended task is inferred from `y`.\n                    If `y` has a boolean, integer or object dtype, the task is assumed to be classification,\n                    else regression.\n    :type ml_task: str\n\n    :param multiclass: Whether the problem is multiclass classification. This modifies the way in which features\n                       are selected. Multiclass requires the features to be statistically significant for\n                       predicting n_significant classes.\n    :type multiclass: bool\n\n    :param n_significant: The number of classes for which features should be statistically significant predictors\n                          to be regarded as \'relevant\'\n    :type n_significant: int\n\n    :param test_for_binary_target_binary_feature: Which test to be used for binary target, binary feature\n                                                  (currently unused)\n    :type test_for_binary_target_binary_feature: str\n\n    :param test_for_binary_target_real_feature: Which test to be used for binary target, real feature\n    :type test_for_binary_target_real_feature: str\n\n    :param test_for_real_target_binary_feature: Which test to be used for real target, binary feature (currently unused)\n    :type test_for_real_target_binary_feature: str\n\n    :param test_for_real_target_real_feature: Which test to be used for real target, real feature (currently unused)\n    :type test_for_real_target_real_feature: str\n\n    :param fdr_level: The FDR level that should be respected, this is the theoretical expected percentage of irrelevant\n                      features among all created features.\n    :type fdr_level: float\n\n    :param hypotheses_independent: Can the significance of the features be assumed to be independent?\n                                   Normally, this should be set to False as the features are never\n                                   independent (e.g. mean and median)\n    :type hypotheses_independent: bool\n\n    :param n_jobs: Number of processes to use during the p-value calculation\n    :type n_jobs: int\n\n    :param show_warnings: Show warnings during the p-value calculation (needed for debugging of calculators).\n    :type show_warnings: bool\n\n    :param chunksize: The size of one chunk that is submitted to the worker\n        process for the parallelisation.  Where one chunk is defined as\n        the data for one feature. If you set the chunksize\n        to 10, then it means that one task is to filter 10 features.\n        If it is set it to None, depending on distributor,\n        heuristics are used to find the optimal chunksize. If you get out of\n        memory exceptions, you can try it with the dask distributor and a\n        smaller chunksize.\n    :type chunksize: None or int\n\n    :return: A pandas.DataFrame with each column of the input DataFrame X as index with information on the significance\n             of this particular feature. The DataFrame has the columns\n             "feature",\n             "type" (binary, real or const),\n             "p_value" (the significance of this feature as a p-value, lower means more significant)\n             "relevant" (True if the Benjamini Hochberg procedure rejected the null hypothesis [the feature is\n             not relevant] for this feature).\n             If the problem is `multiclass` with n classes, the DataFrame will contain n\n             columns named "p_value_CLASSID" instead of the "p_value" column.\n             `CLASSID` refers here to the different values set in `y`.\n             There will also be n columns named `relevant_CLASSID`, indicating whether\n             the feature is relevant for that class.\n    :rtype: pandas.DataFrame\n    ')), Assign(targets=[Name(id='y', ctx=Store())], value=Call(func=Attribute(value=Name(id='y', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='X', ctx=Store())], value=Call(func=Attribute(value=Name(id='X', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='list', ctx=Load()), args=[Attribute(value=Name(id='y', ctx=Load()), attr='index', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='list', ctx=Load()), args=[Attribute(value=Name(id='X', ctx=Load()), attr='index', ctx=Load())], keywords=[])]), msg=Constant(value='The index of X and y need to be the same')), If(test=Compare(left=Name(id='ml_task', ctx=Load()), ops=[NotIn()], comparators=[List(elts=[Constant(value='auto'), Constant(value='classification'), Constant(value='regression')], ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value="ml_task must be one of: 'auto', 'classification', 'regression'")], keywords=[]))], orelse=[If(test=Compare(left=Name(id='ml_task', ctx=Load()), ops=[Eq()], comparators=[Constant(value='auto')]), body=[Assign(targets=[Name(id='ml_task', ctx=Store())], value=Call(func=Name(id='infer_ml_task', ctx=Load()), args=[Name(id='y', ctx=Load())], keywords=[]))], orelse=[])]), If(test=Name(id='multiclass', ctx=Load()), body=[Assert(test=Compare(left=Name(id='ml_task', ctx=Load()), ops=[Eq()], comparators=[Constant(value='classification')]), msg=Constant(value='ml_task must be classification for multiclass problem')), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Call(func=Attribute(value=Name(id='y', ctx=Load()), attr='unique', ctx=Load()), args=[], keywords=[])], keywords=[]), ops=[GtE()], comparators=[Name(id='n_significant', ctx=Load())]), msg=Constant(value='n_significant must not exceed the total number of classes')), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Call(func=Attribute(value=Name(id='y', ctx=Load()), attr='unique', ctx=Load()), args=[], keywords=[])], keywords=[]), ops=[LtE()], comparators=[Constant(value=2)]), body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Constant(value='Two or fewer classes, binary feature selection will be used (multiclass = False)')], keywords=[])), Assign(targets=[Name(id='multiclass', ctx=Store())], value=Constant(value=False))], orelse=[])], orelse=[]), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='catch_warnings', ctx=Load()), args=[], keywords=[]))], body=[If(test=UnaryOp(op=Not(), operand=Name(id='show_warnings', ctx=Load())), body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='simplefilter', ctx=Load()), args=[Constant(value='ignore')], keywords=[]))], orelse=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='simplefilter', ctx=Load()), args=[Constant(value='default')], keywords=[]))]), If(test=Compare(left=Name(id='n_jobs', ctx=Load()), ops=[Eq()], comparators=[Constant(value=0)]), body=[Assign(targets=[Name(id='map_function', ctx=Store())], value=Name(id='map', ctx=Load()))], orelse=[Assign(targets=[Name(id='pool', ctx=Store())], value=Call(func=Name(id='Pool', ctx=Load()), args=[], keywords=[keyword(arg='processes', value=Name(id='n_jobs', ctx=Load())), keyword(arg='initializer', value=Name(id='initialize_warnings_in_workers', ctx=Load())), keyword(arg='initargs', value=Tuple(elts=[Name(id='show_warnings', ctx=Load())], ctx=Load()))])), Assign(targets=[Name(id='map_function', ctx=Store())], value=Call(func=Name(id='partial', ctx=Load()), args=[Attribute(value=Name(id='pool', ctx=Load()), attr='map', ctx=Load())], keywords=[keyword(arg='chunksize', value=Name(id='chunksize', ctx=Load()))]))]), Assign(targets=[Name(id='relevance_table', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[], keywords=[keyword(arg='index', value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load()), args=[Attribute(value=Name(id='X', ctx=Load()), attr='columns', ctx=Load())], keywords=[keyword(arg='name', value=Constant(value='feature'))]))])), Assign(targets=[Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='feature'), ctx=Store())], value=Attribute(value=Name(id='relevance_table', ctx=Load()), attr='index', ctx=Load())), Assign(targets=[Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='type'), ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load()), args=[Call(func=Name(id='map_function', ctx=Load()), args=[Name(id='get_feature_type', ctx=Load()), ListComp(elt=Subscript(value=Name(id='X', ctx=Load()), slice=Name(id='feature', ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='feature', ctx=Store()), iter=Attribute(value=Name(id='relevance_table', ctx=Load()), attr='index', ctx=Load()), ifs=[], is_async=0)])], keywords=[])], keywords=[keyword(arg='index', value=Attribute(value=Name(id='relevance_table', ctx=Load()), attr='index', ctx=Load()))])), Assign(targets=[Name(id='table_real', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Compare(left=Attribute(value=Name(id='relevance_table', ctx=Load()), attr='type', ctx=Load()), ops=[Eq()], comparators=[Constant(value='real')]), ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='table_binary', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Compare(left=Attribute(value=Name(id='relevance_table', ctx=Load()), attr='type', ctx=Load()), ops=[Eq()], comparators=[Constant(value='binary')]), ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='table_const', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Compare(left=Attribute(value=Name(id='relevance_table', ctx=Load()), attr='type', ctx=Load()), ops=[Eq()], comparators=[Constant(value='constant')]), ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Name(id='table_const', ctx=Load()), slice=Constant(value='p_value'), ctx=Store())], value=Attribute(value=Name(id='np', ctx=Load()), attr='NaN', ctx=Load())), Assign(targets=[Subscript(value=Name(id='table_const', ctx=Load()), slice=Constant(value='relevant'), ctx=Store())], value=Constant(value=False)), If(test=UnaryOp(op=Not(), operand=Attribute(value=Name(id='table_const', ctx=Load()), attr='empty', ctx=Load())), body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='[test_feature_significance] Constant features: {}'), attr='format', ctx=Load()), args=[Call(func=Attribute(value=Constant(value=', '), attr='join', ctx=Load()), args=[Call(func=Name(id='map', ctx=Load()), args=[Name(id='str', ctx=Load()), Attribute(value=Name(id='table_const', ctx=Load()), attr='feature', ctx=Load())], keywords=[])], keywords=[])], keywords=[]), Name(id='RuntimeWarning', ctx=Load())], keywords=[]))], orelse=[]), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='table_const', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='relevance_table', ctx=Load())], keywords=[])]), body=[If(test=Compare(left=Name(id='n_jobs', ctx=Load()), ops=[NotEq()], comparators=[Constant(value=0)]), body=[Expr(value=Call(func=Attribute(value=Name(id='pool', ctx=Load()), attr='close', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='pool', ctx=Load()), attr='terminate', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='pool', ctx=Load()), attr='join', ctx=Load()), args=[], keywords=[]))], orelse=[]), Return(value=Name(id='table_const', ctx=Load()))], orelse=[]), If(test=Compare(left=Name(id='ml_task', ctx=Load()), ops=[Eq()], comparators=[Constant(value='classification')]), body=[Assign(targets=[Name(id='tables', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='label', ctx=Store()), iter=Call(func=Attribute(value=Name(id='y', ctx=Load()), attr='unique', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='_test_real_feature', ctx=Store())], value=Call(func=Name(id='partial', ctx=Load()), args=[Name(id='target_binary_feature_real_test', ctx=Load())], keywords=[keyword(arg='y', value=Compare(left=Name(id='y', ctx=Load()), ops=[Eq()], comparators=[Name(id='label', ctx=Load())])), keyword(arg='test', value=Name(id='test_for_binary_target_real_feature', ctx=Load()))])), Assign(targets=[Name(id='_test_binary_feature', ctx=Store())], value=Call(func=Name(id='partial', ctx=Load()), args=[Name(id='target_binary_feature_binary_test', ctx=Load())], keywords=[keyword(arg='y', value=Compare(left=Name(id='y', ctx=Load()), ops=[Eq()], comparators=[Name(id='label', ctx=Load())]))])), Assign(targets=[Name(id='tmp', ctx=Store())], value=Call(func=Name(id='_calculate_relevance_table_for_implicit_target', ctx=Load()), args=[Name(id='table_real', ctx=Load()), Name(id='table_binary', ctx=Load()), Name(id='X', ctx=Load()), Name(id='_test_real_feature', ctx=Load()), Name(id='_test_binary_feature', ctx=Load()), Name(id='hypotheses_independent', ctx=Load()), Name(id='fdr_level', ctx=Load()), Name(id='map_function', ctx=Load())], keywords=[])), If(test=Name(id='multiclass', ctx=Load()), body=[Assign(targets=[Name(id='tmp', ctx=Store())], value=Call(func=Attribute(value=Name(id='tmp', ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[keyword(arg='drop', value=Constant(value=True))])), Assign(targets=[Attribute(value=Name(id='tmp', ctx=Load()), attr='columns', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='tmp', ctx=Load()), attr='columns', ctx=Load()), attr='map', ctx=Load()), args=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=IfExp(test=BoolOp(op=And(), values=[Compare(left=Name(id='x', ctx=Load()), ops=[NotEq()], comparators=[Constant(value='feature')]), Compare(left=Name(id='x', ctx=Load()), ops=[NotEq()], comparators=[Constant(value='type')])]), body=BinOp(left=BinOp(left=Name(id='x', ctx=Load()), op=Add(), right=Constant(value='_')), op=Add(), right=Call(func=Name(id='str', ctx=Load()), args=[Name(id='label', ctx=Load())], keywords=[])), orelse=Name(id='x', ctx=Load())))], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Name(id='tables', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='tmp', ctx=Load())], keywords=[]))], orelse=[]), If(test=Name(id='multiclass', ctx=Load()), body=[Assign(targets=[Name(id='relevance_table', ctx=Store())], value=Call(func=Name(id='reduce', ctx=Load()), args=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='left'), arg(arg='right')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='merge', ctx=Load()), args=[Name(id='left', ctx=Load()), Name(id='right', ctx=Load())], keywords=[keyword(arg='on', value=List(elts=[Constant(value='feature'), Constant(value='type')], ctx=Load())), keyword(arg='how', value=Constant(value='outer'))])), Name(id='tables', ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='n_significant'), ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='relevance_table', ctx=Load()), attr='filter', ctx=Load()), args=[], keywords=[keyword(arg='regex', value=Constant(value='^relevant_')), keyword(arg='axis', value=Constant(value=1))]), attr='sum', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='relevant'), ctx=Store())], value=Compare(left=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='n_significant'), ctx=Load()), ops=[GtE()], comparators=[Name(id='n_significant', ctx=Load())])), Assign(targets=[Attribute(value=Name(id='relevance_table', ctx=Load()), attr='index', ctx=Store())], value=Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='feature'), ctx=Load()))], orelse=[Assign(targets=[Name(id='relevance_table', ctx=Store())], value=Call(func=Name(id='combine_relevance_tables', ctx=Load()), args=[Name(id='tables', ctx=Load())], keywords=[]))])], orelse=[If(test=Compare(left=Name(id='ml_task', ctx=Load()), ops=[Eq()], comparators=[Constant(value='regression')]), body=[Assign(targets=[Name(id='_test_real_feature', ctx=Store())], value=Call(func=Name(id='partial', ctx=Load()), args=[Name(id='target_real_feature_real_test', ctx=Load())], keywords=[keyword(arg='y', value=Name(id='y', ctx=Load()))])), Assign(targets=[Name(id='_test_binary_feature', ctx=Store())], value=Call(func=Name(id='partial', ctx=Load()), args=[Name(id='target_real_feature_binary_test', ctx=Load())], keywords=[keyword(arg='y', value=Name(id='y', ctx=Load()))])), Assign(targets=[Name(id='relevance_table', ctx=Store())], value=Call(func=Name(id='_calculate_relevance_table_for_implicit_target', ctx=Load()), args=[Name(id='table_real', ctx=Load()), Name(id='table_binary', ctx=Load()), Name(id='X', ctx=Load()), Name(id='_test_real_feature', ctx=Load()), Name(id='_test_binary_feature', ctx=Load()), Name(id='hypotheses_independent', ctx=Load()), Name(id='fdr_level', ctx=Load()), Name(id='map_function', ctx=Load())], keywords=[]))], orelse=[])]), If(test=Compare(left=Name(id='n_jobs', ctx=Load()), ops=[NotEq()], comparators=[Constant(value=0)]), body=[Expr(value=Call(func=Attribute(value=Name(id='pool', ctx=Load()), attr='close', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='pool', ctx=Load()), attr='terminate', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='pool', ctx=Load()), attr='join', ctx=Load()), args=[], keywords=[]))], orelse=[]), If(test=Name(id='multiclass', ctx=Load()), body=[For(target=Name(id='column', ctx=Store()), iter=Attribute(value=Call(func=Attribute(value=Name(id='relevance_table', ctx=Load()), attr='filter', ctx=Load()), args=[], keywords=[keyword(arg='regex', value=Constant(value='^relevant_')), keyword(arg='axis', value=Constant(value=1))]), attr='columns', ctx=Load()), body=[Assign(targets=[Subscript(value=Name(id='table_const', ctx=Load()), slice=Name(id='column', ctx=Load()), ctx=Store())], value=Constant(value=False))], orelse=[]), Assign(targets=[Subscript(value=Name(id='table_const', ctx=Load()), slice=Constant(value='n_significant'), ctx=Store())], value=Constant(value=0)), Expr(value=Call(func=Attribute(value=Name(id='table_const', ctx=Load()), attr='drop', ctx=Load()), args=[], keywords=[keyword(arg='columns', value=List(elts=[Constant(value='p_value')], ctx=Load())), keyword(arg='inplace', value=Constant(value=True))]))], orelse=[]), Assign(targets=[Name(id='relevance_table', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='relevance_table', ctx=Load()), Name(id='table_const', ctx=Load())], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=0))])), If(test=Compare(left=Call(func=Name(id='sum', ctx=Load()), args=[Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='relevant'), ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)]), body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='No feature was found relevant for {} for fdr level = {} (which corresponds to the maximal percentage of irrelevant features, consider using an higher fdr level or add other features.'), attr='format', ctx=Load()), args=[Name(id='ml_task', ctx=Load()), Name(id='fdr_level', ctx=Load())], keywords=[]), Name(id='RuntimeWarning', ctx=Load())], keywords=[]))], orelse=[])]), Return(value=Name(id='relevance_table', ctx=Load()))], decorator_list=[]), FunctionDef(name='_calculate_relevance_table_for_implicit_target', args=arguments(posonlyargs=[], args=[arg(arg='table_real'), arg(arg='table_binary'), arg(arg='X'), arg(arg='test_real_feature'), arg(arg='test_binary_feature'), arg(arg='hypotheses_independent'), arg(arg='fdr_level'), arg(arg='map_function')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Subscript(value=Name(id='table_real', ctx=Load()), slice=Constant(value='p_value'), ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load()), args=[Call(func=Name(id='map_function', ctx=Load()), args=[Name(id='test_real_feature', ctx=Load()), ListComp(elt=Subscript(value=Name(id='X', ctx=Load()), slice=Name(id='feature', ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='feature', ctx=Store()), iter=Attribute(value=Name(id='table_real', ctx=Load()), attr='index', ctx=Load()), ifs=[], is_async=0)])], keywords=[])], keywords=[keyword(arg='index', value=Attribute(value=Name(id='table_real', ctx=Load()), attr='index', ctx=Load()))])), Assign(targets=[Subscript(value=Name(id='table_binary', ctx=Load()), slice=Constant(value='p_value'), ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load()), args=[Call(func=Name(id='map_function', ctx=Load()), args=[Name(id='test_binary_feature', ctx=Load()), ListComp(elt=Subscript(value=Name(id='X', ctx=Load()), slice=Name(id='feature', ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='feature', ctx=Store()), iter=Attribute(value=Name(id='table_binary', ctx=Load()), attr='index', ctx=Load()), ifs=[], is_async=0)])], keywords=[])], keywords=[keyword(arg='index', value=Attribute(value=Name(id='table_binary', ctx=Load()), attr='index', ctx=Load()))])), Assign(targets=[Name(id='relevance_table', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='table_real', ctx=Load()), Name(id='table_binary', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='method', ctx=Store())], value=IfExp(test=Name(id='hypotheses_independent', ctx=Load()), body=Constant(value='fdr_bh'), orelse=Constant(value='fdr_by'))), Assign(targets=[Subscript(value=Name(id='relevance_table', ctx=Load()), slice=Constant(value='relevant'), ctx=Store())], value=Subscript(value=Call(func=Name(id='multipletests', ctx=Load()), args=[Attribute(value=Name(id='relevance_table', ctx=Load()), attr='p_value', ctx=Load()), Name(id='fdr_level', ctx=Load()), Name(id='method', ctx=Load())], keywords=[]), slice=Constant(value=0), ctx=Load())), Return(value=Call(func=Attribute(value=Name(id='relevance_table', ctx=Load()), attr='sort_values', ctx=Load()), args=[Constant(value='p_value')], keywords=[]))], decorator_list=[]), FunctionDef(name='infer_ml_task', args=arguments(posonlyargs=[], args=[arg(arg='y')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="\n    Infer the machine learning task to select for.\n    The result will be either `'regression'` or `'classification'`.\n    If the target vector only consists of integer typed values or objects, we assume the task is `'classification'`.\n    Else `'regression'`.\n\n    :param y: The target vector y.\n    :type y: pandas.Series\n    :return: 'classification' or 'regression'\n    :rtype: str\n    ")), If(test=BoolOp(op=Or(), values=[Compare(left=Attribute(value=Attribute(value=Name(id='y', ctx=Load()), attr='dtype', ctx=Load()), attr='kind', ctx=Load()), ops=[In()], comparators=[Subscript(value=Attribute(value=Name(id='np', ctx=Load()), attr='typecodes', ctx=Load()), slice=Constant(value='AllInteger'), ctx=Load())]), Compare(left=Attribute(value=Name(id='y', ctx=Load()), attr='dtype', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Name(id='np', ctx=Load()), attr='object', ctx=Load())])]), body=[Assign(targets=[Name(id='ml_task', ctx=Store())], value=Constant(value='classification'))], orelse=[Assign(targets=[Name(id='ml_task', ctx=Store())], value=Constant(value='regression'))]), Return(value=Name(id='ml_task', ctx=Load()))], decorator_list=[]), FunctionDef(name='combine_relevance_tables', args=arguments(posonlyargs=[], args=[arg(arg='relevance_tables')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n    Create a combined relevance table out of a list of relevance tables,\n    aggregating the p-values and the relevances.\n\n    :param relevance_tables: A list of relevance tables\n    :type relevance_tables: List[pd.DataFrame]\n    :return: The combined relevance table\n    :rtype: pandas.DataFrame\n    ')), FunctionDef(name='_combine', args=arguments(posonlyargs=[], args=[arg(arg='a'), arg(arg='b')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[AugAssign(target=Attribute(value=Name(id='a', ctx=Load()), attr='relevant', ctx=Store()), op=BitOr(), value=Attribute(value=Name(id='b', ctx=Load()), attr='relevant', ctx=Load())), Assign(targets=[Attribute(value=Name(id='a', ctx=Load()), attr='p_value', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='a', ctx=Load()), attr='p_value', ctx=Load()), attr='combine', ctx=Load()), args=[Attribute(value=Name(id='b', ctx=Load()), attr='p_value', ctx=Load()), Name(id='min', ctx=Load()), Constant(value=1)], keywords=[])), Return(value=Name(id='a', ctx=Load()))], decorator_list=[]), Return(value=Call(func=Name(id='reduce', ctx=Load()), args=[Name(id='_combine', ctx=Load()), Name(id='relevance_tables', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='get_feature_type', args=arguments(posonlyargs=[], args=[arg(arg='feature_column')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="\n    For a given feature, determine if it is real, binary or constant.\n    Here binary means that only two unique values occur in the feature.\n\n    :param feature_column: The feature column\n    :type feature_column: pandas.Series\n    :return: 'constant', 'binary' or 'real'\n    ")), Assign(targets=[Name(id='n_unique_values', ctx=Store())], value=Call(func=Name(id='len', ctx=Load()), args=[Call(func=Name(id='set', ctx=Load()), args=[Attribute(value=Name(id='feature_column', ctx=Load()), attr='values', ctx=Load())], keywords=[])], keywords=[])), If(test=Compare(left=Name(id='n_unique_values', ctx=Load()), ops=[Eq()], comparators=[Constant(value=1)]), body=[Return(value=Constant(value='constant'))], orelse=[If(test=Compare(left=Name(id='n_unique_values', ctx=Load()), ops=[Eq()], comparators=[Constant(value=2)]), body=[Return(value=Constant(value='binary'))], orelse=[Return(value=Constant(value='real'))])])], decorator_list=[])], type_ignores=[])