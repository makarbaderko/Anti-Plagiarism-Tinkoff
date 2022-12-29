Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), ImportFrom(module='etna.analysis', names=[alias(name='StatisticsRelevanceTable')], level=0), ImportFrom(module='etna.transforms.feature_selection', names=[alias(name='MRMRFeatureSelectionTransform')], level=0), FunctionDef(name='test_get_features_to_use', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_exog', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='features_to_use'), arg(arg='expected_features')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='base_selector', ctx=Store())], value=Call(func=Name(id='MRMRFeatureSelectionTransform', ctx=Load()), args=[], keywords=[keyword(arg='relevance_table', value=Call(func=Name(id='StatisticsRelevanceTable', ctx=Load()), args=[], keywords=[])), keyword(arg='top_k', value=Constant(value=3)), keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load()))])), Assign(targets=[Name(id='features', ctx=Store())], value=Call(func=Attribute(value=Name(id='base_selector', ctx=Load()), attr='_get_features_to_use', ctx=Load()), args=[Attribute(value=Name(id='ts_with_exog', ctx=Load()), attr='df', ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Name(id='features', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='sorted', ctx=Load()), args=[Name(id='expected_features', ctx=Load())], keywords=[])]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='features_to_use, expected_features'), Tuple(elts=[Tuple(elts=[Constant(value='all'), List(elts=[Constant(value='regressor_1'), Constant(value='regressor_2'), Constant(value='exog')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='regressor_1')], ctx=Load()), List(elts=[Constant(value='regressor_1')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='regressor_1'), Constant(value='unknown_column')], ctx=Load()), List(elts=[Constant(value='regressor_1')], ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_get_features_to_use_raise_warning', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_exog', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='base_selector', ctx=Store())], value=Call(func=Name(id='MRMRFeatureSelectionTransform', ctx=Load()), args=[], keywords=[keyword(arg='relevance_table', value=Call(func=Name(id='StatisticsRelevanceTable', ctx=Load()), args=[], keywords=[])), keyword(arg='top_k', value=Constant(value=3)), keyword(arg='features_to_use', value=List(elts=[Constant(value='regressor_1'), Constant(value='unknown_column')], ctx=Load()))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='warns', ctx=Load()), args=[Name(id='UserWarning', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Columns from feature_to_use which are out of dataframe columns will be dropped!'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='base_selector', ctx=Load()), attr='_get_features_to_use', ctx=Load()), args=[Attribute(value=Name(id='ts_with_exog', ctx=Load()), attr='df', ctx=Load())], keywords=[]))])], decorator_list=[]), FunctionDef(name='test_transform', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_exog', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='features_to_use'), arg(arg='selected_features'), arg(arg='expected_columns')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' Ʀ      ')), Assign(targets=[Name(id='base_selector', ctx=Store())], value=Call(func=Name(id='MRMRFeatureSelectionTransform', ctx=Load()), args=[], keywords=[keyword(arg='relevance_table', value=Call(func=Name(id='StatisticsRelevanceTable', ctx=Load()), args=[], keywords=[])), keyword(arg='top_k', value=Constant(value=3)), keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load())), keyword(arg='return_features', value=Constant(value=False))])), Assign(targets=[Attribute(value=Name(id='base_selector', ctx=Load()), attr='selected_features', ctx=Store())], value=Name(id='selected_features', ctx=Load())), Assign(targets=[Name(id='transformed_df_with_exog', ctx=Store())], value=Call(func=Attribute(value=Name(id='base_selector', ctx=Load()), attr='transform', ctx=Load()), args=[Attribute(value=Name(id='ts_with_exog', ctx=Load()), attr='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='columns', ctx=Store())], value=Call(func=Name(id='se', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='transformed_df_with_exog', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Name(id='columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='sorted', ctx=Load()), args=[Name(id='expected_columns', ctx=Load())], keywords=[])]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='features_to_use, selected_features, expected_columns'), Tuple(elts=[Tuple(elts=[Constant(value='all'), List(elts=[Constant(value='regressor_1')], ctx=Load()), List(elts=[Constant(value='regressor_1'), Constant(value='target')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='regressor_1'), Constant(value='regressor_2')], ctx=Load()), List(elts=[Constant(value='regressor_1')], ctx=Load()), List(elts=[Constant(value='regressor_1'), Constant(value='exog'), Constant(value='target')], ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_transform_save_columns', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_exog'), arg(arg='features_to_use'), arg(arg='selected_features'), arg(arg='expected_columns'), arg(arg='return_features')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='original_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_with_exog', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='MRMRFeatureSelectionTransform', ctx=Load()), args=[], keywords=[keyword(arg='relevance_table', value=Call(func=Name(id='StatisticsRelevanceTable', ctx=Load()), args=[], keywords=[])), keyword(arg='top_k', value=Constant(value=3)), keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load())), keyword(arg='return_features', value=Name(id='return_features', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='transform', ctx=Load()), attr='selected_features', ctx=Store())], value=Name(id='selected_features', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='ts_with_exog', ctx=Load()), attr='transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_saved', ctx=Store())], value=Attribute(value=Name(id='transform', ctx=Load()), attr='_df_removed', ctx=Load())), If(test=Name(id='return_features', ctx=Load()), body=[Assign(targets=[Name(id='got_columns', ctx=Store())], value=Call(func=Name(id='se', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df_saved', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[])), Assert(test=Compare(left=Name(id='got_columns', ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='se', ctx=Load()), args=[Name(id='expected_columns', ctx=Load())], keywords=[])])), For(target=Name(id='column', ctx=Store()), iter=Name(id='got_columns', ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Subscript(value=Attribute(value=Name(id='df_saved', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Name(id='original_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())])], keywords=[]))], orelse=[])], orelse=[Assert(test=Compare(left=Name(id='df_saved', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='return_features'), List(elts=[Constant(value=True), Constant(value=False)], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='features_to_use, selected_features, expected_columns'), Tuple(elts=[Tuple(elts=[Constant(value='all'), List(elts=[Constant(value='regressor_1')], ctx=Load()), List(elts=[Constant(value='exog'), Constant(value='regressor_2')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='regressor_1'), Constant(value='regressor_2')], ctx=Load()), List(elts=[Constant(value='regressor_1')], ctx=Load()), List(elts=[Constant(value='regressor_2')], ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_inverse_transform_back_excl', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_exog'), arg(arg='features_to_use'), arg(arg='return_features'), arg(arg='expected_columns')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\x89Τ        ͊æʹǻ    Ǫ  Ƣ ')), Assign(targets=[Name(id='original_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_with_exog', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='MRMRFeatureSelectionTransform', ctx=Load()), args=[], keywords=[keyword(arg='relevance_table', value=Call(func=Name(id='StatisticsRelevanceTable', ctx=Load()), args=[], keywords=[])), keyword(arg='top_k', value=Constant(value=2)), keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load())), keyword(arg='return_features', value=Name(id='return_features', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='ts_with_exog', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts_with_exog', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='columns_inversed', ctx=Store())], value=Call(func=Name(id='se', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='ts_with_exog', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[])), Assert(test=Compare(left=Name(id='columns_inversed', ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='se', ctx=Load()), args=[Name(id='expected_columns', ctx=Load())], keywords=[])])), For(target=Name(id='column', ctx=Store()), iter=Name(id='columns_inversed', ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='all', ctx=Load()), args=[Compare(left=Subscript(value=Name(id='ts_with_exog', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Attribute(value=Name(id='original_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())])], keywords=[]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='features_to_use, expected_columns, return_features'), List(elts=[Tuple(elts=[Constant(value='all'), List(elts=[Constant(value='exog'), Constant(value='regressor_1'), Constant(value='regressor_2'), Constant(value='target')], ctx=Load()), Constant(value=True)], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='regressor_1'), Constant(value='regressor_2')], ctx=Load()), List(elts=[Constant(value='regressor_2'), Constant(value='regressor_1'), Constant(value='exog'), Constant(value='target')], ctx=Load()), Constant(value=False)], ctx=Load()), Tuple(elts=[Constant(value='all'), List(elts=[Constant(value='regressor_2'), Constant(value='exog'), Constant(value='target')], ctx=Load()), Constant(value=False)], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='regressor_1'), Constant(value='regressor_2')], ctx=Load()), List(elts=[Constant(value='regressor_2'), Constant(value='regressor_1'), Constant(value='exog'), Constant(value='target')], ctx=Load()), Constant(value=True)], ctx=Load())], ctx=Load())], keywords=[])])], type_ignores=[])