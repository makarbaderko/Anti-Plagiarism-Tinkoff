Module(body=[ImportFrom(module='copy', names=[alias(name='deepcopy')], level=0), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), ImportFrom(module='ruptures', names=[alias(name='Binseg')], level=0), ImportFrom(module='sklearn.ensemble', names=[alias(name='RandomForestRegressor')], level=0), ImportFrom(module='sklearn.linear_model', names=[alias(name='LinearRegression')], level=0), ImportFrom(module='etna.datasets.tsdataset', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.transforms.decomposition', names=[alias(name='TrendTransform')], level=0), ImportFrom(module='etna.transforms.decomposition.trend', names=[alias(name='_OneSegmentTrendTransform')], level=0), Assign(targets=[Name(id='DEFAULT_SEGMENT', ctx=Store())], value=Constant(value='segment_1')), FunctionDef(name='df_one_segment', args=arguments(posonlyargs=[], args=[arg(arg='example_df')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Attribute(value=Subscript(value=Name(id='example_df', ctx=Load()), slice=Compare(left=Subscript(value=Name(id='example_df', ctx=Load()), slice=Constant(value='segment'), ctx=Load()), ops=[Eq()], comparators=[Name(id='DEFAULT_SEGMENT', ctx=Load())]), ctx=Load()), attr='set_index', ctx=Load()), args=[Constant(value='timestamp')], keywords=[]))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='test_fit_transform_one_segment', args=arguments(posonlyargs=[], args=[arg(arg='df_one_segment', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n    Test that fit_transform interface works correctly for one segment.\n    ')), Assign(targets=[Name(id='df_one_segment_original', ctx=Store())], value=Call(func=Attribute(value=Name(id='df_one_segment', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='out_column', ctx=Store())], value=Constant(value='regressor_result')), Assign(targets=[Name(id='trend_transform', ctx=Store())], value=Call(func=Name(id='_OneSegmentTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='detrend_model', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Constant(value=5)), keyword(arg='out_column', value=Name(id='out_column', ctx=Load()))])), Assign(targets=[Name(id='df_one_segment', ctx=Store())], value=Call(func=Attribute(value=Name(id='trend_transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='df_one_segment', ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Attribute(value=Name(id='df_one_segment', ctx=Load()), attr='columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='sorted', ctx=Load()), args=[List(elts=[Constant(value='target'), Constant(value='segment'), Name(id='out_column', ctx=Load())], ctx=Load())], keywords=[])])), Assert(test=Call(func=Attribute(value=Compare(left=Subscript(value=Name(id='df_one_segment', ctx=Load()), slice=Constant(value='target'), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Name(id='df_one_segment_original', ctx=Load()), slice=Constant(value='target'), ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='residue', ctx=Store())], value=BinOp(left=Subscript(value=Name(id='df_one_segment', ctx=Load()), slice=Constant(value='target'), ctx=Load()), op=Sub(), right=Subscript(value=Name(id='df_one_segment', ctx=Load()), slice=Name(id='out_column', ctx=Load()), ctx=Load()))), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='residue', ctx=Load()), attr='mean', ctx=Load()), args=[], keywords=[]), ops=[Lt()], comparators=[Constant(value=1)]))], decorator_list=[], returns=Constant(value=None)), FunctionDef(name='test_inverse_transform_one_segment', args=arguments(posonlyargs=[], args=[arg(arg='df_one_segment', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n    Test that inverse_transform interface works correctly for one segment.\n    ')), Assign(targets=[Name(id='trend_transform', ctx=Store())], value=Call(func=Name(id='_OneSegmentTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='detrend_model', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Constant(value=5)), keyword(arg='out_column', value=Constant(value='test'))])), Assign(targets=[Name(id='df_one_segment_transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='trend_transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='df_one_segment', ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_one_segment_inverse_transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='trend_transform', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[Name(id='df_one_segment', ctx=Load())], keywords=[])), Assert(test=Call(func=Attribute(value=Call(func=Attribute(value=Compare(left=Name(id='df_one_segment_transformed', ctx=Load()), ops=[Eq()], comparators=[Name(id='df_one_segment_inverse_transformed', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[]), attr='all', ctx=Load()), args=[], keywords=[]))], decorator_list=[], returns=Constant(value=None)), FunctionDef(name='test_fit_transform_many_segments', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n    Test that fit_transform interface works correctly for many segment.\n    ')), Assign(targets=[Name(id='out_column', ctx=Store())], value=Constant(value='regressor_result')), Assign(targets=[Name(id='example_tsds_original', ctx=Store())], value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='example_tsds', ctx=Load())], keywords=[])), Assign(targets=[Name(id='trend_transform', ctx=Store())], value=Call(func=Name(id='TrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='detrend_model', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Constant(value=5)), keyword(arg='out_column', value=Name(id='out_column', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='trend_transform', ctx=Load())], ctx=Load())], keywords=[])), For(target=Name(id='segment', ctx=Store()), iter=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='segments', ctx=Load()), body=[Assign(targets=[Name(id='segment_slice', ctx=Store())], value=Subscript(value=Subscript(value=Name(id='example_tsds', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segment', ctx=Load()), Slice()], ctx=Load()), ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='segment_slice_original', ctx=Store())], value=Subscript(value=Subscript(value=Name(id='example_tsds_original', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segment', ctx=Load()), Slice()], ctx=Load()), ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load())), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Attribute(value=Name(id='segment_slice', ctx=Load()), attr='columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='sorted', ctx=Load()), args=[List(elts=[Constant(value='target'), Name(id='out_column', ctx=Load())], ctx=Load())], keywords=[])])), Assert(test=Call(func=Attribute(value=Compare(left=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target'), ctx=Load()), ops=[Eq()], comparators=[Subscript(value=Name(id='segment_slice_original', ctx=Load()), slice=Constant(value='target'), ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='residue', ctx=Store())], value=BinOp(left=Subscript(value=Name(id='segment_slice_original', ctx=Load()), slice=Constant(value='target'), ctx=Load()), op=Sub(), right=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Name(id='out_column', ctx=Load()), ctx=Load()))), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='residue', ctx=Load()), attr='mean', ctx=Load()), args=[], keywords=[]), ops=[Lt()], comparators=[Constant(value=1)]))], orelse=[])], decorator_list=[], returns=Constant(value=None)), FunctionDef(name='test_inverse_transform_many_segments', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n    Test that inverse_transform interface works correctly for many segment.\n    ')), Assign(targets=[Name(id='trend_transform', ctx=Store())], value=Call(func=Name(id='TrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='detrend_model', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Constant(value=5)), keyword(arg='out_column', value=Constant(value='test'))])), Expr(value=Call(func=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='trend_transform', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='original_df', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assert(test=Call(func=Attribute(value=Call(func=Attribute(value=Compare(left=Name(id='original_df', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Name(id='example_tsds', ctx=Load()), attr='df', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[]), attr='all', ctx=Load()), args=[], keywords=[]))], decorator_list=[], returns=Constant(value=None)), FunctionDef(name='test_transform_inverse_transform', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n    Test inverse transform of TrendTransform.\n    ')), Assign(targets=[Name(id='trend_transform', ctx=Store())], value=Call(func=Name(id='TrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='detrend_model', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[])), keyword(arg='model', value=Constant(value='rbf'))])), Expr(value=Call(func=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='trend_transform', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='original', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assert(test=Call(func=Attribute(value=Call(func=Attribute(value=Compare(left=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='df', ctx=Load()), ops=[Eq()], comparators=[Name(id='original', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[]), attr='all', ctx=Load()), args=[], keywords=[]))], decorator_list=[], returns=Constant(value=None)), FunctionDef(name='test_transform_interface_out_column', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test transform interface with out_column param')), Assign(targets=[Name(id='out_column', ctx=Store())], value=Constant(value='regressor_test')), Assign(targets=[Name(id='trend_transform', ctx=Store())], value=Call(func=Name(id='TrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='detrend_model', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[])), keyword(arg='model', value=Constant(value='rbf')), keyword(arg='out_column', value=Name(id='out_column', ctx=Load()))])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='trend_transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Attribute(value=Name(id='example_tsds', ctx=Load()), attr='df', ctx=Load())], keywords=[])), For(target=Name(id='seg', ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='result', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value=0)], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), body=[Assert(test=Compare(left=Name(id='out_column', ctx=Load()), ops=[In()], comparators=[Attribute(value=Subscript(value=Name(id='result', ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Load()), attr='columns', ctx=Load())]))], orelse=[])], decorator_list=[], returns=Constant(value=None)), FunctionDef(name='test_transform_interface_repr', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test transform interface without out_column param')), Assign(targets=[Name(id='trend_transform', ctx=Store())], value=Call(func=Name(id='TrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='detrend_model', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[])), keyword(arg='model', value=Constant(value='rbf'))])), Assign(targets=[Name(id='out_column', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Call(func=Attribute(value=Name(id='trend_transform', ctx=Load()), attr='__repr__', ctx=Load()), args=[], keywords=[]), conversion=-1)])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='trend_transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Attribute(value=Name(id='example_tsds', ctx=Load()), attr='df', ctx=Load())], keywords=[])), For(target=Name(id='seg', ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='result', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value=0)], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), body=[Assert(test=Compare(left=Name(id='out_column', ctx=Load()), ops=[In()], comparators=[Attribute(value=Subscript(value=Name(id='result', ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Load()), attr='columns', ctx=Load())]))], orelse=[])], decorator_list=[], returns=Constant(value=None)), FunctionDef(name='test_fit_transform_with_nans_in_tails', args=arguments(posonlyargs=[], args=[arg(arg='df_with_nans_in_tails'), arg(arg='model')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='TrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='detrend_model', value=Name(id='model', ctx=Load())), keyword(arg='model', value=Constant(value='rbf')), keyword(arg='out_column', value=Constant(value='regressor_result'))])), Assign(targets=[Name(id='transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df_with_nans_in_tails', ctx=Load()))])), For(target=Name(id='segment', ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='transformed', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='segment_slice', ctx=Store())], value=Subscript(value=Subscript(value=Attribute(value=Name(id='transformed', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Slice(), ctx=Load()), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segment', ctx=Load()), Slice()], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='residue', ctx=Store())], value=BinOp(left=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target'), ctx=Load()), op=Sub(), right=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='regressor_result'), ctx=Load()))), Assert(test=Compare(left=Call(func=Attribute(value=Name(id='residue', ctx=Load()), attr='mean', ctx=Load()), args=[], keywords=[]), ops=[Lt()], comparators=[Constant(value=0.13)]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='model'), Tuple(elts=[Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[]), Call(func=Name(id='RandomForestRegressor', ctx=Load()), args=[], keywords=[])], ctx=Load())], keywords=[])]), FunctionDef(name='test_fit_transform_with_nans_in_middle_raise_error', args=arguments(posonlyargs=[], args=[arg(arg='df_with_nans'), arg(arg='model')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='TrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='detrend_model', value=Name(id='model', ctx=Load())), keyword(arg='model', value=Constant(value='rbf'))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='The input column contains NaNs in the middle of the series!'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df_with_nans', ctx=Load()))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='model'), Tuple(elts=[Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[]), Call(func=Name(id='RandomForestRegressor', ctx=Load()), args=[], keywords=[])], ctx=Load())], keywords=[])])], type_ignores=[])