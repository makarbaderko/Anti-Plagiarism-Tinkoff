Module(body=[ImportFrom(module='copy', names=[alias(name='deepcopy')], level=0), ImportFrom(module='typing', names=[alias(name='Any')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), ImportFrom(module='ruptures.costs', names=[alias(name='CostAR')], level=0), ImportFrom(module='ruptures.costs', names=[alias(name='CostL1')], level=0), ImportFrom(module='ruptures.costs', names=[alias(name='CostMl')], level=0), ImportFrom(module='ruptures.costs', names=[alias(name='CostLinear')], level=0), ImportFrom(module='ruptures.costs', names=[alias(name='CostNormal')], level=0), ImportFrom(module='etna.transforms.decomposition', names=[alias(name='BinsegTrendTransform')], level=0), ImportFrom(module='ruptures.costs', names=[alias(name='CostRank')], level=0), ImportFrom(module='ruptures.costs', names=[alias(name='CostL2')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='ruptures.costs', names=[alias(name='CostRbf')], level=0), FunctionDef(name='test_binseg_in_pi_peline', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='        k')), Assign(targets=[Name(id='bs', ctx=Store())], value=Call(func=Name(id='BinsegTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target'))])), Expr(value=Call(func=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='bs', ctx=Load())], ctx=Load())], keywords=[])), For(target=Name(id='segment', ctx=Store()), iter=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='segments', ctx=Load()), body=[Assert(test=Compare(left=Call(func=Name(id='abs', ctx=Load()), args=[Call(func=Attribute(value=Subscript(value=Name(id='example_tsds', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segment', ctx=Load()), Constant(value='target')], ctx=Load()), ctx=Load()), attr='mean', ctx=Load()), args=[], keywords=[])], keywords=[]), ops=[Lt()], comparators=[Constant(value=1)]))], orelse=[])], decorator_list=[]), FunctionDef(name='test_binseg_run_with_custom_costs', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='custom_cos_t_class', annotation=Name(id='Any', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='bs', ctx=Store())], value=Call(func=Name(id='BinsegTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='custom_cost', value=Call(func=Name(id='custom_cos_t_class', ctx=Load()), args=[], keywords=[]))])), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='example_tsds', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='bs', ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assert(test=Call(func=Attribute(value=Call(func=Attribute(value=Compare(left=Attribute(value=Name(id='ts', ctx=Load()), attr='df', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Name(id='example_tsds', ctx=Load()), attr='df', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[]), attr='all', ctx=Load()), args=[], keywords=[]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='custom_cost_class'), Tuple(elts=[Name(id='CostMl', ctx=Load()), Name(id='CostAR', ctx=Load()), Name(id='CostLinear', ctx=Load()), Name(id='CostRbf', ctx=Load()), Name(id='CostL2', ctx=Load()), Name(id='CostL1', ctx=Load()), Name(id='CostNormal', ctx=Load()), Name(id='CostRank', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_binseg_run_with_model', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='modelAP', annotation=Name(id='Any', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='bs', ctx=Store())], value=Call(func=Name(id='BinsegTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='model', value=Name(id='modelAP', ctx=Load()))])), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='example_tsds', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='bs', ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assert(test=Call(func=Attribute(value=Call(func=Attribute(value=Compare(left=Attribute(value=Name(id='ts', ctx=Load()), attr='df', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Name(id='example_tsds', ctx=Load()), attr='df', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[]), attr='all', ctx=Load()), args=[], keywords=[]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='model'), Tuple(elts=[Constant(value='l1'), Constant(value='l2'), Constant(value='normal'), Constant(value='rbf'), Constant(value='linear'), Constant(value='ar'), Constant(value='mahalanobis'), Constant(value='rank')], ctx=Load())], keywords=[])]), FunctionDef(name='test_fit_transform_with_nans_in_tails', args=arguments(posonlyargs=[], args=[arg(arg='df_with_nans_in_tailsACCay')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='transformw', ctx=Store())], value=Call(func=Name(id='BinsegTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target'))])), Assign(targets=[Name(id='transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='transformw', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df_with_nans_in_tailsACCay', ctx=Load()))])), For(target=Name(id='segment', ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='transformed', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='segment_slice', ctx=Store())], value=Subscript(value=Subscript(value=Attribute(value=Name(id='transformed', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Slice(), ctx=Load()), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segment', ctx=Load()), Slice()], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load())), Assert(test=Compare(left=Call(func=Name(id='abs', ctx=Load()), args=[Call(func=Attribute(value=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target'), ctx=Load()), attr='mean', ctx=Load()), args=[], keywords=[])], keywords=[]), ops=[Lt()], comparators=[Constant(value=0.1)]))], orelse=[])], decorator_list=[]), FunctionDef(name='test_fit_transform_with_nans_in_middle_raise_error', args=arguments(posonlyargs=[], args=[arg(arg='df_')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ɂ     ')), Assign(targets=[Name(id='transformw', ctx=Store())], value=Call(func=Name(id='BinsegTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target'))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueEr_ror', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='The input column contains NaNs in the middle of the series!'))]))], body=[Assign(targets=[Name(id='__', ctx=Store())], value=Call(func=Attribute(value=Name(id='transformw', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df_', ctx=Load()))]))])], decorator_list=[]), FunctionDef(name='test_binseg_runs_with_different_series_length', args=arguments(posonlyargs=[], args=[arg(arg='ts_with_different_series_length', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ɃìCʣheck thaKũΙntρŨ binseg\u0381Ϣ ϷworkǤsȡɅ ëJ·withʕˎ daơtasĵets wŢit̍͜hɻƺ dɶi͐Ĳf¼fer̔enˌt@ ǋλl¢e\u038dnş͞gtƔhÜ ƕ*seęrªΉΦieĿsʧ.')), Assign(targets=[Name(id='bs', ctx=Store())], value=Call(func=Name(id='BinsegTrendTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target'))])), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='ts_with_different_series_length', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='bs', ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Attribute(value=Attribute(value=Name(id='ts', ctx=Load()), attr='df', ctx=Load()), attr='values', ctx=Load()), Attribute(value=Attribute(value=Name(id='ts_with_different_series_length', ctx=Load()), attr='df', ctx=Load()), attr='values', ctx=Load())], keywords=[keyword(arg='equal_nan', value=Constant(value=True))]))], decorator_list=[])], type_ignores=[])