Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.transforms', names=[alias(name='AddConstTransform')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='generate_ar_df')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='LambdaTransform')], level=0), Import(names=[alias(name='pytest')]), ImportFrom(module='etna.transforms', names=[alias(name='LagTransform')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='LogTransform')], level=0), FunctionDef(name='ts_non_negative', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Name(id='generate_ar_df', ctx=Load()), args=[], keywords=[keyword(arg='start_time', value=Constant(value='2020-01-01')), keyword(arg='periods', value=Constant(value=300)), keyword(arg='ar_coef', value=List(elts=[Constant(value=1)], ctx=Load())), keyword(arg='sigma', value=Constant(value=1)), keyword(arg='n_segments', value=Constant(value=3)), keyword(arg='random_seed', value=Constant(value=0)), keyword(arg='freq', value=Constant(value='D'))])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='apply', ctx=Load()), args=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='abs', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[]))], keywords=[])), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[keyword(arg='freq', value=Constant(value='D'))])), Return(value=Name(id='ts', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())]), FunctionDef(name='test_transform', args=arguments(posonlyargs=[], args=[arg(arg='ts_range_const'), arg(arg='inplace'), arg(arg='check_column'), arg(arg='function'), arg(arg='inverse_function'), arg(arg='exp'), arg(arg='segment')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ȁ ô       Ơ»WƄ ͌ȴ       ')), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='LambdaTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='transform_func', value=Name(id='function', ctx=Load())), keyword(arg='inplace', value=Name(id='inplace', ctx=Load())), keyword(arg='inverse_transform_func', value=Name(id='inverse_function', ctx=Load())), keyword(arg='out_column', value=Name(id='check_column', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='ts_range_const', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_allclose', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[Subscript(value=Name(id='ts_range_const', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segment', ctx=Load()), Name(id='check_column', ctx=Load())], ctx=Load()), ctx=Load())], keywords=[]), Name(id='exp', ctx=Load())], keywords=[keyword(arg='rtol', value=Constant(value=1e-09))]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='inplace, segment, check_column, function, inverse_function, expected_result'), List(elts=[Tuple(elts=[Constant(value=False), Constant(value='1'), Constant(value='target_transformed'), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Pow(), right=Constant(value=2))), Constant(value=None), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[ListComp(elt=BinOp(left=Name(id='i', ctx=Load()), op=Pow(), right=Constant(value=2)), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='rang_e', ctx=Load()), args=[Constant(value=100)], keywords=[]), ifs=[], is_async=0)])], keywords=[])], ctx=Load()), Tuple(elts=[Constant(value=True), Constant(value='1'), Constant(value='target'), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Pow(), right=Constant(value=2))), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Pow(), right=Constant(value=0.5))), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[ListComp(elt=BinOp(left=Name(id='i', ctx=Load()), op=Pow(), right=Constant(value=2)), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='rang_e', ctx=Load()), args=[Constant(value=100)], keywords=[]), ifs=[], is_async=0)])], keywords=[])], ctx=Load()), Tuple(elts=[Constant(value=False), Constant(value='2'), Constant(value='target_transformed'), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Pow(), right=Constant(value=2))), Constant(value=None), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[BinOp(left=List(elts=[Constant(value=1), Constant(value=9)], ctx=Load()), op=Mult(), right=Constant(value=50))], keywords=[])], ctx=Load()), Tuple(elts=[Constant(value=True), Constant(value='2'), Constant(value='target'), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Pow(), right=Constant(value=2))), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Pow(), right=Constant(value=0.5))), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[BinOp(left=List(elts=[Constant(value=1), Constant(value=9)], ctx=Load()), op=Mult(), right=Constant(value=50))], keywords=[])], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_save_transform', args=arguments(posonlyargs=[], args=[arg(arg='ts_non_negative'), arg(arg='transform_originalwjcdf'), arg(arg='transform_function'), arg(arg='out_column')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='ts_copy', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[Call(func=Attribute(value=Name(id='ts_non_negative', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])], keywords=[keyword(arg='freq', value=Constant(value='D'))])), Expr(value=Call(func=Attribute(value=Name(id='ts_copy', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform_originalwjcdf', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='ts', ctx=Store())], value=Name(id='ts_non_negative', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Call(func=Name(id='LambdaTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='out_column', value=Name(id='out_column', ctx=Load())), keyword(arg='transform_func', value=Name(id='transform_function', ctx=Load())), keyword(arg='inplace', value=Constant(value=False))])], ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='SET', ctx=Load()), args=[Attribute(value=Name(id='ts_copy', ctx=Load()), attr='columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='SET', ctx=Load()), args=[Attribute(value=Name(id='ts', ctx=Load()), attr='columns', ctx=Load())], keywords=[])])), For(target=Name(id='column', ctx=Store()), iter=Attribute(value=Name(id='ts', ctx=Load()), attr='columns', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_allclose', ctx=Load()), args=[Subscript(value=Name(id='ts_copy', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load()), Subscript(value=Name(id='ts', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Name(id='column', ctx=Load())], ctx=Load()), ctx=Load())], keywords=[keyword(arg='rtol', value=Constant(value=1e-09))]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='transform_original, transform_function, out_column'), List(elts=[Tuple(elts=[Call(func=Name(id='LogTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='out_column', value=Constant(value='transform_target')), keyword(arg='inplace', value=Constant(value=False))]), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='log10', ctx=Load()), args=[BinOp(left=Name(id='x', ctx=Load()), op=Add(), right=Constant(value=1))], keywords=[])), Constant(value='transform_target')], ctx=Load()), Tuple(elts=[Call(func=Name(id='AddConstTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='out_column', value=Constant(value='transform_target')), keyword(arg='value', value=Constant(value=1)), keyword(arg='inplace', value=Constant(value=False))]), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Add(), right=Constant(value=1))), Constant(value='transform_target')], ctx=Load()), Tuple(elts=[Call(func=Name(id='LagTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='out_column', value=Constant(value='transform_target')), keyword(arg='lags', value=List(elts=[Constant(value=1)], ctx=Load()))]), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id='x', ctx=Load()), attr='shift', ctx=Load()), args=[Constant(value=1)], keywords=[])), Constant(value='transform_target_1')], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_nesessary_inverse_transform', args=arguments(posonlyargs=[], args=[arg(arg='ts_non_negative')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='inverse_transform_func must be defined, when inplace=True'))]))], body=[Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='LambdaTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='inplace', value=Constant(value=True)), keyword(arg='transform_func', value=Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Name(id='x', ctx=Load())))])), Expr(value=Call(func=Attribute(value=Name(id='ts_non_negative', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[]))])], decorator_list=[]), FunctionDef(name='test_inverse_transform', args=arguments(posonlyargs=[], args=[arg(arg='ts_range_const'), arg(arg='function'), arg(arg='inverse_function')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='~     Ŷ  ')), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='LambdaTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='transform_func', value=Name(id='function', ctx=Load())), keyword(arg='inplace', value=Constant(value=True)), keyword(arg='inverse_transform_func', value=Name(id='inverse_function', ctx=Load()))])), Assign(targets=[Name(id='original_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_range_const', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts_range_const', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts_range_const', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='check_column', ctx=Store())], value=Constant(value='target')), For(target=Name(id='segment', ctx=Store()), iter=Attribute(value=Name(id='ts_range_const', ctx=Load()), attr='segments', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_allclose', ctx=Load()), args=[Subscript(value=Name(id='ts_range_const', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segment', ctx=Load()), Name(id='check_column', ctx=Load())], ctx=Load()), ctx=Load()), Subscript(value=Name(id='original_df', ctx=Load()), slice=Tuple(elts=[Name(id='segment', ctx=Load()), Name(id='check_column', ctx=Load())], ctx=Load()), ctx=Load())], keywords=[keyword(arg='rtol', value=Constant(value=1e-09))]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='function, inverse_function'), List(elts=[Tuple(elts=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Pow(), right=Constant(value=2))), Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=BinOp(left=Name(id='x', ctx=Load()), op=Pow(), right=Constant(value=0.5)))], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test__interface_not_inplace', args=arguments(posonlyargs=[], args=[arg(arg='ts_non_negative')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='   Β  ̘ ˠ̭π        Ϳ  ɐ  ')), Assign(targets=[Name(id='add_column', ctx=Store())], value=Constant(value='target_transformed')), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='LambdaTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='out_column', value=Name(id='add_column', ctx=Load())), keyword(arg='transform_func', value=Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Name(id='x', ctx=Load()))), keyword(arg='inplace', value=Constant(value=False))])), Assign(targets=[Name(id='origin_al_columns', ctx=Store())], value=Call(func=Name(id='SET', ctx=Load()), args=[Attribute(value=Name(id='ts_non_negative', ctx=Load()), attr='columns', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts_non_negative', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='SET', ctx=Load()), args=[Attribute(value=Name(id='ts_non_negative', ctx=Load()), attr='columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Attribute(value=Name(id='origin_al_columns', ctx=Load()), attr='union', ctx=Load()), args=[SetComp(elt=Tuple(elts=[Name(id='segment', ctx=Load()), Name(id='add_column', ctx=Load())], ctx=Load()), generators=[comprehension(target=Name(id='segment', ctx=Store()), iter=Attribute(value=Name(id='ts_non_negative', ctx=Load()), attr='segments', ctx=Load()), ifs=[], is_async=0)])], keywords=[])]))], decorator_list=[]), FunctionDef(name='ts_range_const', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='period_s', ctx=Store())], value=Constant(value=100)), Assign(targets=[Name(id='_df_1', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp'), Constant(value='target'), Constant(value='segment')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2022-06-22')], keywords=[keyword(arg='periods', value=Name(id='period_s', ctx=Load()))]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Constant(value=0), Name(id='period_s', ctx=Load())], keywords=[]), Constant(value=1)])], keywords=[])), Assign(targets=[Name(id='df_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp'), Constant(value='target'), Constant(value='segment')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2022-06-22')], keywords=[keyword(arg='periods', value=Name(id='period_s', ctx=Load()))]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[BinOp(left=List(elts=[Constant(value=1), Constant(value=3)], ctx=Load()), op=Mult(), right=BinOp(left=Name(id='period_s', ctx=Load()), op=FloorDiv(), right=Constant(value=2)))], keywords=[]), Constant(value=2)])], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='_df_1', ctx=Load()), Name(id='df_2', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[keyword(arg='freq', value=Constant(value='D'))])), Return(value=Name(id='ts', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())]), FunctionDef(name='test_interface_i', args=arguments(posonlyargs=[], args=[arg(arg='ts_non_negative')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='LambdaTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='inplace', value=Constant(value=True)), keyword(arg='transform_func', value=Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Name(id='x', ctx=Load()))), keyword(arg='inverse_transform_func', value=Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Name(id='x', ctx=Load())))])), Assign(targets=[Name(id='origin_al_columns', ctx=Store())], value=Call(func=Name(id='SET', ctx=Load()), args=[Attribute(value=Name(id='ts_non_negative', ctx=Load()), attr='columns', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts_non_negative', ctx=Load()), attr='fit_transform', ctx=Load()), args=[List(elts=[Name(id='transform', ctx=Load())], ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='SET', ctx=Load()), args=[Attribute(value=Name(id='ts_non_negative', ctx=Load()), attr='columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Name(id='origin_al_columns', ctx=Load())])), Expr(value=Call(func=Attribute(value=Name(id='ts_non_negative', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='SET', ctx=Load()), args=[Attribute(value=Name(id='ts_non_negative', ctx=Load()), attr='columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Name(id='origin_al_columns', ctx=Load())]))], decorator_list=[])], type_ignores=[])