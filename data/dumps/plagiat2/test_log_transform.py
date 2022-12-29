Module(body=[Import(names=[alias(name='pytest')]), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='math', names=[alias(name='e')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.transforms', names=[alias(name='AddConstTransform')], level=0), ImportFrom(module='etna.transforms.math', names=[alias(name='LogTransform')], level=0), FunctionDef(name='positive_df_hM', args=arguments(posonlyargs=[], args=[arg(arg='random_seed')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='period_s', ctx=Store())], value=Constant(value=100)), Assign(targets=[Name(id='df1', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[keyword(arg='periods', value=Name(id='period_s', ctx=Load()))])])], keywords=[])), Assign(targets=[Subscript(value=Name(id='df1', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=BinOp(left=List(elts=[Constant(value='segment_1')], ctx=Load()), op=Mult(), right=Name(id='period_s', ctx=Load()))), Assign(targets=[Subscript(value=Name(id='df1', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='uniform', ctx=Load()), args=[Constant(value=10), Constant(value=20)], keywords=[keyword(arg='size', value=Name(id='period_s', ctx=Load()))])), Assign(targets=[Subscript(value=Name(id='df1', ctx=Load()), slice=Constant(value='expected'), ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='log10', ctx=Load()), args=[BinOp(left=Subscript(value=Name(id='df1', ctx=Load()), slice=Constant(value='target'), ctx=Load()), op=Add(), right=Constant(value=1))], keywords=[])), Assign(targets=[Name(id='d_f2', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[keyword(arg='periods', value=Name(id='period_s', ctx=Load()))])])], keywords=[])), Assign(targets=[Subscript(value=Name(id='d_f2', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=BinOp(left=List(elts=[Constant(value='segment_2')], ctx=Load()), op=Mult(), right=Name(id='period_s', ctx=Load()))), Assign(targets=[Subscript(value=Name(id='d_f2', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='uniform', ctx=Load()), args=[Constant(value=1), Constant(value=15)], keywords=[keyword(arg='size', value=Name(id='period_s', ctx=Load()))])), Assign(targets=[Subscript(value=Name(id='d_f2', ctx=Load()), slice=Constant(value='expected'), ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='log10', ctx=Load()), args=[BinOp(left=Subscript(value=Name(id='d_f2', ctx=Load()), slice=Constant(value='target'), ctx=Load()), op=Add(), right=Constant(value=1))], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[Tuple(elts=[Name(id='df1', ctx=Load()), Name(id='d_f2', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='pivot', ctx=Load()), args=[], keywords=[keyword(arg='index', value=Constant(value='timestamp')), keyword(arg='columns', value=Constant(value='segment'))]), attr='reorder_levels', ctx=Load()), args=[List(elts=[Constant(value=1), Constant(value=0)], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))]), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Store())], value=List(elts=[Constant(value='segment'), Constant(value='feature')], ctx=Load())), Return(value=Name(id='df', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='test_logpreproc_value', args=arguments(posonlyargs=[], args=[arg(arg='positive_df_hM', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Check the value o̹Ǽf transfȬorm r̗esɬult.')), Assign(targets=[Name(id='preprocesscWA', ctx=Store())], value=Call(func=Name(id='LogTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='base', value=Constant(value=10))])), Assign(targets=[Name(id='value', ctx=Store())], value=Call(func=Attribute(value=Name(id='preprocesscWA', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='positive_df_hM', ctx=Load()))])), For(target=Name(id='segment', ctx=Store()), iter=List(elts=[Constant(value='segment_1'), Constant(value='segment_2')], ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_array_almost_equal', ctx=Load()), args=[Subscript(value=Subscript(value=Name(id='value', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load()), slice=Constant(value='target'), ctx=Load()), Subscript(value=Subscript(value=Name(id='positive_df_hM', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load()), slice=Constant(value='expected'), ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='test_negative_series_behavior', args=arguments(posonlyargs=[], args=[arg(arg='non_positive_df_', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='preprocesscWA', ctx=Store())], value=Call(func=Name(id='LogTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target'))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[]))], body=[Assign(targets=[Name(id='_lEC', ctx=Store())], value=Call(func=Attribute(value=Name(id='preprocesscWA', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='non_positive_df_', ctx=Load()))]))])], decorator_list=[]), FunctionDef(name='test_in', args=arguments(posonlyargs=[], args=[arg(arg='positive_df_hM', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='basewYuYA', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='preprocesscWA', ctx=Store())], value=Call(func=Name(id='LogTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='base', value=Name(id='basewYuYA', ctx=Load()))])), Assign(targets=[Name(id='transformed_target', ctx=Store())], value=Call(func=Attribute(value=Name(id='preprocesscWA', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Call(func=Attribute(value=Name(id='positive_df_hM', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[]))])), Assign(targets=[Name(id='inversed', ctx=Store())], value=Call(func=Attribute(value=Name(id='preprocesscWA', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='transformed_target', ctx=Load()))])), For(target=Name(id='segment', ctx=Store()), iter=List(elts=[Constant(value='segment_1'), Constant(value='segment_2')], ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_array_almost_equal', ctx=Load()), args=[Subscript(value=Subscript(value=Name(id='inversed', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load()), slice=Constant(value='target'), ctx=Load()), Subscript(value=Subscript(value=Name(id='positive_df_hM', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load()), slice=Constant(value='target'), ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='base'), Tuple(elts=[Constant(value=5), Constant(value=10), Name(id='e', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_logpreproc_noninplace_interface', args=arguments(posonlyargs=[], args=[arg(arg='positive_df_hM', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='out_column', annotation=Name(id='str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='preprocesscWA', ctx=Store())], value=Call(func=Name(id='LogTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='out_column', value=Name(id='out_column', ctx=Load())), keyword(arg='base', value=Constant(value=10)), keyword(arg='inplace', value=Constant(value=False))])), Assign(targets=[Name(id='value', ctx=Store())], value=Call(func=Attribute(value=Name(id='preprocesscWA', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='positive_df_hM', ctx=Load()))])), Assign(targets=[Name(id='e', ctx=Store())], value=IfExp(test=Compare(left=Name(id='out_column', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=Name(id='out_column', ctx=Load()), orelse=Call(func=Attribute(value=Name(id='preprocesscWA', ctx=Load()), attr='__repr__', ctx=Load()), args=[], keywords=[]))), For(target=Name(id='segment', ctx=Store()), iter=List(elts=[Constant(value='segment_1'), Constant(value='segment_2')], ctx=Load()), body=[Assert(test=Compare(left=Name(id='e', ctx=Load()), ops=[In()], comparators=[Subscript(value=Name(id='value', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load())]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='out_column'), Tuple(elts=[Constant(value=None), Constant(value='log_transform')], ctx=Load())], keywords=[])]), FunctionDef(name='test_logpreproc_value_out_column', args=arguments(posonlyargs=[], args=[arg(arg='positive_df_hM', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='out_column', ctx=Store())], value=Constant(value='target_log_10')), Assign(targets=[Name(id='preprocesscWA', ctx=Store())], value=Call(func=Name(id='LogTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='out_column', value=Name(id='out_column', ctx=Load())), keyword(arg='base', value=Constant(value=10)), keyword(arg='inplace', value=Constant(value=False))])), Assign(targets=[Name(id='value', ctx=Store())], value=Call(func=Attribute(value=Name(id='preprocesscWA', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='positive_df_hM', ctx=Load()))])), For(target=Name(id='segment', ctx=Store()), iter=List(elts=[Constant(value='segment_1'), Constant(value='segment_2')], ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_array_almost_equal', ctx=Load()), args=[Subscript(value=Subscript(value=Name(id='value', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load()), slice=Name(id='out_column', ctx=Load()), ctx=Load()), Subscript(value=Subscript(value=Name(id='positive_df_hM', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load()), slice=Constant(value='expected'), ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='non_positive_df_', args=arguments(posonlyargs=[], args=[arg(arg='random_seed')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='period_s', ctx=Store())], value=Constant(value=100)), Assign(targets=[Name(id='df1', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[keyword(arg='periods', value=Name(id='period_s', ctx=Load()))])])], keywords=[])), Assign(targets=[Subscript(value=Name(id='df1', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=BinOp(left=List(elts=[Constant(value='segment_1')], ctx=Load()), op=Mult(), right=Name(id='period_s', ctx=Load()))), Assign(targets=[Subscript(value=Name(id='df1', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='uniform', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=10)), Constant(value=0)], keywords=[keyword(arg='size', value=Name(id='period_s', ctx=Load()))])), Assign(targets=[Name(id='d_f2', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[keyword(arg='periods', value=Name(id='period_s', ctx=Load()))])])], keywords=[])), Assign(targets=[Subscript(value=Name(id='d_f2', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=BinOp(left=List(elts=[Constant(value='segment_2')], ctx=Load()), op=Mult(), right=Name(id='period_s', ctx=Load()))), Assign(targets=[Subscript(value=Name(id='d_f2', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='uniform', ctx=Load()), args=[Constant(value=0), Constant(value=10)], keywords=[keyword(arg='size', value=Name(id='period_s', ctx=Load()))])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[Tuple(elts=[Name(id='df1', ctx=Load()), Name(id='d_f2', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='pivot', ctx=Load()), args=[], keywords=[keyword(arg='index', value=Constant(value='timestamp')), keyword(arg='columns', value=Constant(value='segment'))]), attr='reorder_levels', ctx=Load()), args=[List(elts=[Constant(value=1), Constant(value=0)], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))]), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Store())], value=List(elts=[Constant(value='segment'), Constant(value='feature')], ctx=Load())), Return(value=Name(id='df', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='test_inverse_transform_out_column', args=arguments(posonlyargs=[], args=[arg(arg='positive_df_hM', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='out_column', ctx=Store())], value=Constant(value='target_log_10')), Assign(targets=[Name(id='preprocesscWA', ctx=Store())], value=Call(func=Name(id='LogTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='out_column', value=Name(id='out_column', ctx=Load())), keyword(arg='base', value=Constant(value=10)), keyword(arg='inplace', value=Constant(value=False))])), Assign(targets=[Name(id='transformed_target', ctx=Store())], value=Call(func=Attribute(value=Name(id='preprocesscWA', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='positive_df_hM', ctx=Load()))])), Assign(targets=[Name(id='inversed', ctx=Store())], value=Call(func=Attribute(value=Name(id='preprocesscWA', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='transformed_target', ctx=Load()))])), For(target=Name(id='segment', ctx=Store()), iter=List(elts=[Constant(value='segment_1'), Constant(value='segment_2')], ctx=Load()), body=[Assert(test=Compare(left=Name(id='out_column', ctx=Load()), ops=[In()], comparators=[Subscript(value=Name(id='inversed', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load())]))], orelse=[])], decorator_list=[]), FunctionDef(name='TEST_FIT_TRANSFORM_WITH_NANS', args=arguments(posonlyargs=[], args=[arg(arg='TS_DIFF_ENDINGS')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='   ʶ ')), Assign(targets=[Name(id='tran', ctx=Store())], value=Call(func=Name(id='LogTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='inplace', value=Constant(value=True))])), Expr(value=Call(func=Attribute(value=Name(id='TS_DIFF_ENDINGS', ctx=Load()), attr='fit_transform', ctx=Load()), args=[BinOp(left=List(elts=[Call(func=Name(id='AddConstTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='value', value=Constant(value=100))])], ctx=Load()), op=Add(), right=List(elts=[Name(id='tran', ctx=Load())], ctx=Load()))], keywords=[]))], decorator_list=[])], type_ignores=[])