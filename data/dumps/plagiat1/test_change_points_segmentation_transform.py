Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), ImportFrom(module='ruptures', names=[alias(name='Binseg')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='generate_ar_df')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='SMAPE')], level=0), ImportFrom(module='etna.models', names=[alias(name='CatBoostModelPerSegment')], level=0), ImportFrom(module='etna.pipeline', names=[alias(name='Pipeline')], level=0), ImportFrom(module='etna.transforms', names=[alias(name='ChangePointsSegmentationTransform')], level=0), ImportFrom(module='etna.transforms.decomposition.base_change_points', names=[alias(name='RupturesChangePointsModel')], level=0), ImportFrom(module='etna.transforms.decomposition.change_points_segmentation', names=[alias(name='_OneSegmentChangePointsSegmentationTransform')], level=0), Assign(targets=[Name(id='OUT_COLUMN', ctx=Store())], value=Constant(value='result')), Assign(targets=[Name(id='N_BKPS', ctx=Store())], value=Constant(value=5)), FunctionDef(name='test_fit_one_segment', args=arguments(posonlyargs=[], args=[arg(arg='pre_transformed_dfE', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='change_point_model', ctx=Store())], value=Call(func=Name(id='RupturesChangePointsModel', ctx=Load()), args=[], keywords=[keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Name(id='N_BKPS', ctx=Load()))])), Assign(targets=[Name(id='bs', ctx=Store())], value=Call(func=Name(id='_OneSegmentChangePointsSegmentationTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Name(id='change_point_model', ctx=Load())), keyword(arg='out_column', value=Name(id='OUT_COLUMN', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='bs', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Subscript(value=Name(id='pre_transformed_dfE', ctx=Load()), slice=Constant(value='segment_1'), ctx=Load()))])), Assert(test=Compare(left=Attribute(value=Name(id='bs', ctx=Load()), attr='intervals', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]))], decorator_list=[]), FunctionDef(name='simple_ar_ts', args=arguments(posonlyargs=[], args=[arg(arg='RANDOM_SEED')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Name(id='generate_ar_df', ctx=Load()), args=[], keywords=[keyword(arg='periods', value=Constant(value=125)), keyword(arg='start_time', value=Constant(value='2021-05-20')), keyword(arg='n_segments', value=Constant(value=3)), keyword(arg='ar_coef', value=List(elts=[Constant(value=2)], ctx=Load())), keyword(arg='freq', value=Constant(value='D'))])), Assign(targets=[Name(id='df_ts_format', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Return(value=Call(func=Name(id='TSDataset', ctx=Load()), args=[Name(id='df_ts_format', ctx=Load())], keywords=[keyword(arg='freq', value=Constant(value='D'))]))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())]), FunctionDef(name='multitrend_df_with_nans_in_tails', args=arguments(posonlyargs=[], args=[arg(arg='multitrend_df')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Subscript(value=Attribute(value=Name(id='multitrend_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[List(elts=[Subscript(value=Attribute(value=Name(id='multitrend_df', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=0), ctx=Load()), Subscript(value=Attribute(value=Name(id='multitrend_df', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=1), ctx=Load()), Subscript(value=Attribute(value=Name(id='multitrend_df', ctx=Load()), attr='index', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=2)), ctx=Load()), Subscript(value=Attribute(value=Name(id='multitrend_df', ctx=Load()), attr='index', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load())], ctx=Load()), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Constant(value='segment_1'), Constant(value='target')], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Store())], value=Constant(value=None)), Return(value=Name(id='multitrend_df', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())]), FunctionDef(name='pre_transformed_dfE', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2019-12-01'), Constant(value='2019-12-31')], keywords=[])])], keywords=[])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=Constant(value=0)), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='segment_1')), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df', ctx=Load()))])), Return(value=Name(id='df', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='test_transform_format_one_segmentTW', args=arguments(posonlyargs=[], args=[arg(arg='pre_transformed_dfE', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ȓCǔheck ʤt·ɣhŐ at tra\u0379ƯŲ̱nƞ¢sfʺϑZorƦmϮ metˡɑhΏod Ĵ5geƋʓnΩƥëLˬera̪șt͒e nϺew2 ȴcĐϏolumn.')), Assign(targets=[Name(id='change_point_model', ctx=Store())], value=Call(func=Name(id='RupturesChangePointsModel', ctx=Load()), args=[], keywords=[keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Name(id='N_BKPS', ctx=Load()))])), Assign(targets=[Name(id='bs', ctx=Store())], value=Call(func=Name(id='_OneSegmentChangePointsSegmentationTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Name(id='change_point_model', ctx=Load())), keyword(arg='out_column', value=Name(id='OUT_COLUMN', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='bs', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Subscript(value=Name(id='pre_transformed_dfE', ctx=Load()), slice=Constant(value='segment_1'), ctx=Load()))])), Assign(targets=[Name(id='transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='bs', ctx=Load()), attr='transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Subscript(value=Name(id='pre_transformed_dfE', ctx=Load()), slice=Constant(value='segment_1'), ctx=Load()))])), Assert(test=Compare(left=Call(func=Name(id='se', ctx=Load()), args=[Attribute(value=Name(id='transformed', ctx=Load()), attr='columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Set(elts=[Constant(value='target'), Name(id='OUT_COLUMN', ctx=Load())])])), Assert(test=Compare(left=Attribute(value=Subscript(value=Name(id='transformed', ctx=Load()), slice=Name(id='OUT_COLUMN', ctx=Load()), ctx=Load()), attr='dtype', ctx=Load()), ops=[Eq()], comparators=[Constant(value='category')]))], decorator_list=[]), FunctionDef(name='test_monotonously_result', args=arguments(posonlyargs=[], args=[arg(arg='pre_transformed_dfE', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='change_point_model', ctx=Store())], value=Call(func=Name(id='RupturesChangePointsModel', ctx=Load()), args=[], keywords=[keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Name(id='N_BKPS', ctx=Load()))])), Assign(targets=[Name(id='bs', ctx=Store())], value=Call(func=Name(id='_OneSegmentChangePointsSegmentationTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Name(id='change_point_model', ctx=Load())), keyword(arg='out_column', value=Name(id='OUT_COLUMN', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='bs', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Subscript(value=Name(id='pre_transformed_dfE', ctx=Load()), slice=Constant(value='segment_1'), ctx=Load()))])), Assign(targets=[Name(id='transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='bs', ctx=Load()), attr='transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Call(func=Attribute(value=Subscript(value=Name(id='pre_transformed_dfE', ctx=Load()), slice=Constant(value='segment_1'), ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[keyword(arg='deep', value=Constant(value=True))]))])), Assign(targets=[Name(id='result', ctx=Store())], value=Attribute(value=Call(func=Attribute(value=Subscript(value=Name(id='transformed', ctx=Load()), slice=Name(id='OUT_COLUMN', ctx=Load()), ctx=Load()), attr='astype', ctx=Load()), args=[Name(id='int', ctx=Load())], keywords=[]), attr='values', ctx=Load())), Assert(test=Compare(left=Call(func=Attribute(value=Compare(left=BinOp(left=Subscript(value=Name(id='result', ctx=Load()), slice=Slice(lower=Constant(value=1)), ctx=Load()), op=Sub(), right=Subscript(value=Name(id='result', ctx=Load()), slice=Slice(upper=UnaryOp(op=USub(), operand=Constant(value=1))), ctx=Load())), ops=[GtE()], comparators=[Constant(value=0)]), attr='mean', ctx=Load()), args=[], keywords=[]), ops=[Eq()], comparators=[Constant(value=1)]))], decorator_list=[]), FunctionDef(name='test_transform_raise_error_if_not_fitted', args=arguments(posonlyargs=[], args=[arg(arg='pre_transformed_dfE', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test thʀat þtransfĚorm fʮor one Msegment raise erro®r w^hen calling transform Ⱥwitho\x98uȑt being fit.ʄ')), Assign(targets=[Name(id='change_point_model', ctx=Store())], value=Call(func=Name(id='RupturesChangePointsModel', ctx=Load()), args=[], keywords=[keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Name(id='N_BKPS', ctx=Load()))])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='_OneSegmentChangePointsSegmentationTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Name(id='change_point_model', ctx=Load())), keyword(arg='out_column', value=Name(id='OUT_COLUMN', ctx=Load()))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueErro_r', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Transform is not fitted!'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Subscript(value=Name(id='pre_transformed_dfE', ctx=Load()), slice=Constant(value='segment_1'), ctx=Load()))]))])], decorator_list=[]), FunctionDef(name='test_backtest', args=arguments(posonlyargs=[], args=[arg(arg='simple_ar_ts')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  ')), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='CatBoostModelPerSegment', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='horizon', ctx=Store())], value=Constant(value=3)), Assign(targets=[Name(id='change_point_model', ctx=Store())], value=Call(func=Name(id='RupturesChangePointsModel', ctx=Load()), args=[], keywords=[keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Name(id='N_BKPS', ctx=Load()))])), Assign(targets=[Name(id='bs', ctx=Store())], value=Call(func=Name(id='ChangePointsSegmentationTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Name(id='change_point_model', ctx=Load())), keyword(arg='out_column', value=Name(id='OUT_COLUMN', ctx=Load()))])), Assign(targets=[Name(id='pipeline', ctx=Store())], value=Call(func=Name(id='Pipeline', ctx=Load()), args=[], keywords=[keyword(arg='model', value=Name(id='model', ctx=Load())), keyword(arg='transforms', value=List(elts=[Name(id='bs', ctx=Load())], ctx=Load())), keyword(arg='horizon', value=Name(id='horizon', ctx=Load()))])), Assign(targets=[Tuple(elts=[Name(id='_', ctx=Store()), Name(id='_', ctx=Store()), Name(id='_', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='pipeline', ctx=Load()), attr='backtest', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='simple_ar_ts', ctx=Load())), keyword(arg='metrics', value=List(elts=[Call(func=Name(id='SMAPE', ctx=Load()), args=[], keywords=[])], ctx=Load())), keyword(arg='n_folds', value=Constant(value=3))]))], decorator_list=[]), FunctionDef(name='test_future_and_past_filling', args=arguments(posonlyargs=[], args=[arg(arg='simple_ar_ts')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='change_point_model', ctx=Store())], value=Call(func=Name(id='RupturesChangePointsModel', ctx=Load()), args=[], keywords=[keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Name(id='N_BKPS', ctx=Load()))])), Assign(targets=[Name(id='bs', ctx=Store())], value=Call(func=Name(id='ChangePointsSegmentationTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Name(id='change_point_model', ctx=Load())), keyword(arg='out_column', value=Name(id='OUT_COLUMN', ctx=Load()))])), Assign(targets=[Tuple(elts=[Name(id='before', ctx=Store()), Name(id='ts', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='simple_ar_ts', ctx=Load()), attr='train_test_split', ctx=Load()), args=[], keywords=[keyword(arg='test_start', value=Constant(value='2021-06-01'))])), Assign(targets=[Tuple(elts=[Name(id='train', ctx=Store()), Name(id='a', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='train_test_split', ctx=Load()), args=[], keywords=[keyword(arg='test_start', value=Constant(value='2021-08-01'))])), Expr(value=Call(func=Attribute(value=Name(id='bs', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Attribute(value=Name(id='train', ctx=Load()), attr='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='before', ctx=Store())], value=Call(func=Attribute(value=Name(id='bs', ctx=Load()), attr='transform', ctx=Load()), args=[Attribute(value=Name(id='before', ctx=Load()), attr='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='a', ctx=Store())], value=Call(func=Attribute(value=Name(id='bs', ctx=Load()), attr='transform', ctx=Load()), args=[Attribute(value=Name(id='a', ctx=Load()), attr='df', ctx=Load())], keywords=[])), For(target=Name(id='seg', ctx=Store()), iter=Attribute(value=Name(id='train', ctx=Load()), attr='segments', ctx=Load()), body=[Assert(test=Compare(left=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='sum', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='abs', ctx=Load()), args=[Call(func=Attribute(value=Subscript(value=Subscript(value=Name(id='before', ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Load()), slice=Name(id='OUT_COLUMN', ctx=Load()), ctx=Load()), attr='astype', ctx=Load()), args=[Name(id='int', ctx=Load())], keywords=[])], keywords=[])], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)])), Assert(test=Call(func=Attribute(value=Compare(left=Call(func=Attribute(value=Subscript(value=Subscript(value=Name(id='a', ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Load()), slice=Name(id='OUT_COLUMN', ctx=Load()), ctx=Load()), attr='astype', ctx=Load()), args=[Name(id='int', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=5)]), attr='all', ctx=Load()), args=[], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='test_make_future', args=arguments(posonlyargs=[], args=[arg(arg='simple_ar_ts')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  ')), Assign(targets=[Name(id='change_point_model', ctx=Store())], value=Call(func=Name(id='RupturesChangePointsModel', ctx=Load()), args=[], keywords=[keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[])), keyword(arg='n_bkps', value=Name(id='N_BKPS', ctx=Load()))])), Assign(targets=[Name(id='bs', ctx=Store())], value=Call(func=Name(id='ChangePointsSegmentationTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='change_point_model', value=Name(id='change_point_model', ctx=Load())), keyword(arg='out_column', value=Name(id='OUT_COLUMN', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='simple_ar_ts', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='transforms', value=List(elts=[Name(id='bs', ctx=Load())], ctx=Load()))])), Assign(targets=[Name(id='fut_ure', ctx=Store())], value=Call(func=Attribute(value=Name(id='simple_ar_ts', ctx=Load()), attr='make_future', ctx=Load()), args=[Constant(value=10)], keywords=[])), For(target=Name(id='seg', ctx=Store()), iter=Attribute(value=Name(id='simple_ar_ts', ctx=Load()), attr='segments', ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Compare(left=Call(func=Attribute(value=Subscript(value=Subscript(value=Call(func=Attribute(value=Name(id='fut_ure', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[]), slice=Name(id='seg', ctx=Load()), ctx=Load()), slice=Name(id='OUT_COLUMN', ctx=Load()), ctx=Load()), attr='astype', ctx=Load()), args=[Name(id='int', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=5)]), attr='all', ctx=Load()), args=[], keywords=[]))], orelse=[])], decorator_list=[])], type_ignores=[])