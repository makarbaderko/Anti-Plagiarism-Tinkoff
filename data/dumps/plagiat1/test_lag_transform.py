Module(body=[ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Sequence')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), ImportFrom(module='numpy.testing', names=[alias(name='assert_almost_equal')], level=0), ImportFrom(module='etna.datasets.tsdataset', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.transforms.math', names=[alias(name='LagTransform')], level=0), FunctionDef(name='int_df_one_segment', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='οGenerate datafrƃaȉme witƁh simpʱle ųtäargets fo˭rΎ laζg˼s cheǽck.')), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2020-01-01'), Constant(value='2020-06-01')], keywords=[])])], keywords=[])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='segment_1')), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Constant(value=0), Call(func=Name(id='len', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='set_index', ctx=Load()), args=[Constant(value='timestamp')], keywords=[keyword(arg='inplace', value=Constant(value=True))])), Return(value=Name(id='df', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='int_df_two_segment_s', args=arguments(posonlyargs=[], args=[arg(arg='int_df_one_segment')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df_1', ctx=Store())], value=Call(func=Attribute(value=Name(id='int_df_one_segment', ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='df_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='int_df_one_segment', ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Name(id='df_1', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='segment_1')), Assign(targets=[Subscript(value=Name(id='df_2', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='segment_2')), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='df_1', ctx=Load()), Name(id='df_2', ctx=Load())], ctx=Load())], keywords=[keyword(arg='ignore_index', value=Constant(value=True))])), Return(value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[]))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='test_repr', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Tǔest thaƛtϭ that __reprà__ī meϭŵth͙ı¼oΟdĀ wo̹rksȩ bfine.')), Assign(targets=[Name(id='transform_class', ctx=Store())], value=Constant(value='LagTransform')), Assign(targets=[Name(id='lags', ctx=Store())], value=Call(func=Name(id='listc', ctx=Load()), args=[Call(func=Name(id='ra', ctx=Load()), args=[Constant(value=8), Constant(value=24), Constant(value=1)], keywords=[])], keywords=[])), Assign(targets=[Name(id='out_column', ctx=Store())], value=Constant(value='lag_feature')), Assign(targets=[Name(id='transform_without_out_column', ctx=Store())], value=Call(func=Name(id='LagTransform', ctx=Load()), args=[], keywords=[keyword(arg='lags', value=Name(id='lags', ctx=Load())), keyword(arg='in_column', value=Constant(value='target'))])), Assign(targets=[Name(id='transform_with_out_column', ctx=Store())], value=Call(func=Name(id='LagTransform', ctx=Load()), args=[], keywords=[keyword(arg='lags', value=Name(id='lags', ctx=Load())), keyword(arg='in_column', value=Constant(value='target')), keyword(arg='out_column', value=Name(id='out_column', ctx=Load()))])), Assign(targets=[Name(id='true_repr_out_column', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='transform_class', ctx=Load()), conversion=-1), Constant(value="(in_column = 'target', lags = "), FormattedValue(value=Name(id='lags', ctx=Load()), conversion=-1), Constant(value=", out_column = '"), FormattedValue(value=Name(id='out_column', ctx=Load()), conversion=-1), Constant(value="', )")])), Assign(targets=[Name(id='true_repr_no_out_column', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='transform_class', ctx=Load()), conversion=-1), Constant(value="(in_column = 'target', lags = "), FormattedValue(value=Name(id='lags', ctx=Load()), conversion=-1), Constant(value=', out_column = None, )')])), Assign(targets=[Name(id='no_out_column_repr', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform_without_out_column', ctx=Load()), attr='__repr__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='out_column_repr', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform_with_out_column', ctx=Load()), attr='__repr__', ctx=Load()), args=[], keywords=[])), Assert(test=Compare(left=Name(id='no_out_column_repr', ctx=Load()), ops=[Eq()], comparators=[Name(id='true_repr_no_out_column', ctx=Load())])), Assert(test=Compare(left=Name(id='out_column_repr', ctx=Load()), ops=[Eq()], comparators=[Name(id='true_repr_out_column', ctx=Load())]))], decorator_list=[]), FunctionDef(name='test_interface_two_segments_out_column', args=arguments(posonlyargs=[], args=[arg(arg='lags', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='INT', ctx=Load()), Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='INT', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='expected_columns', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='int_df_two_segment_s')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Te͘st {that ˶αtͤȷǕȶraȰnVsfoɂrˎm generatʓe®ʿsƤą correct col\x93\u0383umnƶ naȂʬmeȳs usȗƛingͿ ̬͵o͏uĢ\x94ΤtɌϩ_cΪoͿluϠǅm·n pa̢rameterυ.')), Assign(targets=[Name(id='lf', ctx=Store())], value=Call(func=Name(id='LagTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='lags', value=Name(id='lags', ctx=Load())), keyword(arg='out_column', value=Constant(value='regressor_lag_feature'))])), Assign(targets=[Name(id='lags_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='lf', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='int_df_two_segment_s', ctx=Load()))])), For(target=Name(id='segment', ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='lags_df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='lags_df_lags_columns', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='filter', ctx=Load()), args=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id='x', ctx=Load()), attr='startswith', ctx=Load()), args=[Constant(value='regressor_lag_feature')], keywords=[])), Attribute(value=Subscript(value=Name(id='lags_df', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load()), attr='columns', ctx=Load())], keywords=[])], keywords=[])), Assert(test=Compare(left=Name(id='lags_df_lags_columns', ctx=Load()), ops=[Eq()], comparators=[Name(id='expected_columns', ctx=Load())]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='lags,expected_columns'), Tuple(elts=[Tuple(elts=[Constant(value=3), List(elts=[Constant(value='regressor_lag_feature_1'), Constant(value='regressor_lag_feature_2'), Constant(value='regressor_lag_feature_3')], ctx=Load())], ctx=Load()), Tuple(elts=[List(elts=[Constant(value=5), Constant(value=8)], ctx=Load()), List(elts=[Constant(value='regressor_lag_feature_5'), Constant(value='regressor_lag_feature_8')], ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_interface_two_segments_repr', args=arguments(posonlyargs=[], args=[arg(arg='lags', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='INT', ctx=Load()), Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='INT', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='int_df_two_segment_s')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='segments', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='int_df_two_segment_s', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='LagTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='lags', value=Name(id='lags', ctx=Load()))])), Assign(targets=[Name(id='transformed_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='int_df_two_segment_s', ctx=Load())], keywords=[])), Assign(targets=[Name(id='columns', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='transformed_df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), attr='drop', ctx=Load()), args=[Constant(value='target')], keywords=[])), Assert(test=IfExp(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='lags', ctx=Load()), Name(id='listc', ctx=Load())], keywords=[]), body=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='lags', ctx=Load())], keywords=[])]), orelse=Constant(value=1))), For(target=Name(id='column', ctx=Store()), iter=Name(id='columns', ctx=Load()), body=[Assign(targets=[Name(id='transform_temp', ctx=Store())], value=Call(func=Name(id='eval', ctx=Load()), args=[Name(id='column', ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_temp', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform_temp', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='int_df_two_segment_s', ctx=Load())], keywords=[])), Assign(targets=[Name(id='columns_temp', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='df_temp', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), attr='drop', ctx=Load()), args=[Constant(value='target')], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='columns_temp', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=1)])), Assign(targets=[Name(id='generated_column', ctx=Store())], value=Subscript(value=Name(id='columns_temp', ctx=Load()), slice=Constant(value=0), ctx=Load())), Assert(test=Compare(left=Name(id='generated_column', ctx=Load()), ops=[Eq()], comparators=[Name(id='column', ctx=Load())])), Assert(test=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='df_temp', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segments', ctx=Load()), Name(id='generated_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), attr='equals', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='transformed_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segments', ctx=Load()), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='lags'), Tuple(elts=[Constant(value=3), List(elts=[Constant(value=5), Constant(value=8)], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_lags_values_two_segments', args=arguments(posonlyargs=[], args=[arg(arg='lags', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='INT', ctx=Load()), Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='INT', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='int_df_two_segment_s')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='lf', ctx=Store())], value=Call(func=Name(id='LagTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='lags', value=Name(id='lags', ctx=Load())), keyword(arg='out_column', value=Constant(value='regressor_lag_feature'))])), Assign(targets=[Name(id='lags_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='lf', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='int_df_two_segment_s', ctx=Load()))])), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='lags', ctx=Load()), Name(id='INT', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='lags', ctx=Store())], value=Call(func=Name(id='listc', ctx=Load()), args=[Call(func=Name(id='ra', ctx=Load()), args=[Constant(value=1), BinOp(left=Name(id='lags', ctx=Load()), op=Add(), right=Constant(value=1))], keywords=[])], keywords=[]))], orelse=[]), For(target=Name(id='segment', ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='lags_df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), body=[For(target=Name(id='lag', ctx=Store()), iter=Name(id='lags', ctx=Load()), body=[Assign(targets=[Name(id='true_values', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load()), args=[BinOp(left=BinOp(left=List(elts=[Constant(value=None)], ctx=Load()), op=Mult(), right=Name(id='lag', ctx=Load())), op=Add(), right=Call(func=Name(id='listc', ctx=Load()), args=[Subscript(value=Attribute(value=Subscript(value=Name(id='int_df_two_segment_s', ctx=Load()), slice=Tuple(elts=[Name(id='segment', ctx=Load()), Constant(value='target')], ctx=Load()), ctx=Load()), attr='values', ctx=Load()), slice=Slice(upper=UnaryOp(op=USub(), operand=Name(id='lag', ctx=Load()))), ctx=Load())], keywords=[]))], keywords=[])), Expr(value=Call(func=Name(id='assert_almost_equal', ctx=Load()), args=[Attribute(value=Name(id='true_values', ctx=Load()), attr='values', ctx=Load()), Attribute(value=Subscript(value=Name(id='lags_df', ctx=Load()), slice=Tuple(elts=[Name(id='segment', ctx=Load()), JoinedStr(values=[Constant(value='regressor_lag_feature_'), FormattedValue(value=Name(id='lag', ctx=Load()), conversion=-1)])], ctx=Load()), ctx=Load()), attr='values', ctx=Load())], keywords=[]))], orelse=[])], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='lags'), Tuple(elts=[Constant(value=12), List(elts=[Constant(value=4), Constant(value=6), Constant(value=8), Constant(value=16)], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_invalid_lags_value_two_segments', args=arguments(posonlyargs=[], args=[arg(arg='lags')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Name(id='LagTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='lags', value=Name(id='lags', ctx=Load()))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='lags'), Tuple(elts=[Constant(value=0), UnaryOp(op=USub(), operand=Constant(value=1)), Tuple(elts=[Constant(value=10), Constant(value=15), UnaryOp(op=USub(), operand=Constant(value=2))], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_fit_transform_with_nans', args=arguments(posonlyargs=[], args=[arg(arg='ts_diff_endings')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='LagTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='lags', value=Constant(value=10))])), Expr(value=Call(func=Attribute(value=Name(id='ts_diff_endings', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[])], type_ignores=[])