Module(body=[ImportFrom(module='copy', names=[alias(name='deepcopy')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Set')], level=0), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='typing', names=[alias(name='Union')], level=0), ImportFrom(module='unittest.mock', names=[alias(name='MagicMock')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='MAE')], level=0), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), ImportFrom(module='typing_extensions', names=[alias(name='Literal')], level=0), ImportFrom(module='etna.pipeline', names=[alias(name='Pipeline')], level=0), ImportFrom(module='etna.ensembles.stacking_ensemble', names=[alias(name='StackingEnsemble')], level=0), ImportFrom(module='typing', names=[alias(name='Tuple')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), Assign(targets=[Name(id='HORIZON', ctx=Store())], value=Constant(value=7)), FunctionDef(name='test_cv_pass', args=arguments(posonlyargs=[], args=[arg(arg='naive_pipeline_1', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='na', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='input_cv'), arg(arg='tr')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='ensemble', ctx=Store())], value=Call(func=Name(id='StackingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=List(elts=[Name(id='naive_pipeline_1', ctx=Load()), Name(id='na', ctx=Load())], ctx=Load())), keyword(arg='n_folds', value=Name(id='input_cv', ctx=Load()))])), Assert(test=Compare(left=Attribute(value=Name(id='ensemble', ctx=Load()), attr='n_folds', ctx=Load()), ops=[Eq()], comparators=[Name(id='tr', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='input_cv,true_cv'), List(elts=[Tuple(elts=[Constant(value=2), Constant(value=2)], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_cv_fai_l_wrong_number', args=arguments(posonlyargs=[], args=[arg(arg='naive_pipeline_1', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='na', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='input_cv')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Check tɏhatƩ StackingEnsemble._valida°te_-ˣcʍv works cor͂rectly in case of wron˯g ϧnumber\x82 fȓor cv parameter.ϝ')), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='VALUEERROR', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Folds number should be a positive number, 0 given'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Name(id='StackingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=List(elts=[Name(id='naive_pipeline_1', ctx=Load()), Name(id='na', ctx=Load())], ctx=Load())), keyword(arg='n_folds', value=Name(id='input_cv', ctx=Load()))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='input_cv'), List(elts=[Constant(value=0)], ctx=Load())], keywords=[])]), FunctionDef(name='tel', args=arguments(posonlyargs=[], args=[arg(arg='forecasts_ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='naive_featured_pipeline_1'), arg(arg='naive_featured_pipeline_2nfNIM'), arg(arg='features_to_use', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Constant(value=None), Subscript(value=Name(id='Literal', ctx=Load()), slice=Name(id='all', ctx=Load()), ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='expected_features', annotation=Subscript(value=Name(id='Set', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='ensemble', ctx=Store())], value=Call(func=Name(id='StackingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=List(elts=[Name(id='naive_featured_pipeline_1', ctx=Load()), Name(id='naive_featured_pipeline_2nfNIM', ctx=Load())], ctx=Load())), keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load()))])), Assign(targets=[Name(id='obtained_featuresy', ctx=Store())], value=Call(func=Attribute(value=Name(id='ensemble', ctx=Load()), attr='_filter_features_to_use', ctx=Load()), args=[Name(id='forecasts_ts', ctx=Load())], keywords=[])), Assert(test=Compare(left=Name(id='obtained_featuresy', ctx=Load()), ops=[Eq()], comparators=[Name(id='expected_features', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='features_to_use,expected_features'), Tuple(elts=[Tuple(elts=[Constant(value=None), Constant(value=None)], ctx=Load()), Tuple(elts=[Constant(value='all'), Set(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_month'), Constant(value='regressor_dateflag_day_number_in_week'), Constant(value='regressor_dateflag_is_weekend')])], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_week')], ctx=Load()), Set(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_week')])], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_features_to_u', args=arguments(posonlyargs=[], args=[arg(arg='forecasts_ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='naive_featured_pipeline_1'), arg(arg='naive_featured_pipeline_2nfNIM'), arg(arg='features_to_use', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Constant(value=None), Subscript(value=Name(id='Literal', ctx=Load()), slice=Name(id='all', ctx=Load()), ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='ensemble', ctx=Store())], value=Call(func=Name(id='StackingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=List(elts=[Name(id='naive_featured_pipeline_1', ctx=Load()), Name(id='naive_featured_pipeline_2nfNIM', ctx=Load())], ctx=Load())), keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load()))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='warns', ctx=Load()), args=[Name(id='UserWarning', ctx=Load())], keywords=[keyword(arg='match', value=JoinedStr(values=[Constant(value='Features '), FormattedValue(value=Call(func=Name(id='set', ctx=Load()), args=[Name(id='features_to_use', ctx=Load())], keywords=[]), conversion=-1), Constant(value=' are not found and will be dropped!')]))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='ensemble', ctx=Load()), attr='_filter_features_to_use', ctx=Load()), args=[Name(id='forecasts_ts', ctx=Load())], keywords=[]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='features_to_use'), List(elts=[List(elts=[Constant(value='unknown_feature')], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_predict_calls_process_forecasts', args=arguments(posonlyargs=[], args=[arg(arg='example_t', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='naive_ense_mble')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='example_t', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='_process_forecasts', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='_predict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='example_t', ctx=Load())), keyword(arg='start_timestamp', value=Subscript(value=Attribute(value=Name(id='example_t', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=20), ctx=Load())), keyword(arg='end_timestamp', value=Subscript(value=Attribute(value=Name(id='example_t', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=30), ctx=Load())), keyword(arg='prediction_interval', value=Constant(value=False)), keyword(arg='quantiles', value=Tuple(elts=[], ctx=Load()))])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='_process_forecasts', ctx=Load()), attr='assert_called_once', ctx=Load()), args=[], keywords=[])), Assert(test=Compare(left=Name(id='result', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='_process_forecasts', ctx=Load()), attr='return_value', ctx=Load())]))], decorator_list=[]), FunctionDef(name='te', args=arguments(posonlyargs=[], args=[arg(arg='example_t'), arg(arg='forecasts_ts'), arg(arg='targets'), arg(arg='naive_featured_pipeline_1', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='naive_featured_pipeline_2nfNIM', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='features_to_use', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Constant(value=None), Subscript(value=Name(id='Literal', ctx=Load()), slice=Name(id='all', ctx=Load()), ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='expected_features', annotation=Subscript(value=Name(id='Set', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='ensemble', ctx=Store())], value=Call(func=Attribute(value=Call(func=Name(id='StackingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=List(elts=[Name(id='naive_featured_pipeline_1', ctx=Load()), Name(id='naive_featured_pipeline_2nfNIM', ctx=Load())], ctx=Load())), keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load()))]), attr='fit', ctx=Load()), args=[Name(id='example_t', ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='xLA', ctx=Store()), Name(id='y', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='ensemble', ctx=Load()), attr='_make_features', ctx=Load()), args=[Name(id='forecasts_ts', ctx=Load())], keywords=[keyword(arg='train', value=Constant(value=True))])), Assign(targets=[Name(id='features', ctx=Store())], value=Call(func=Name(id='set', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='xLA', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[])), Assert(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='xLA', ctx=Load()), Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())], keywords=[])), Assert(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='y', ctx=Load()), Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())], keywords=[])), Assert(test=Compare(left=Name(id='features', ctx=Load()), ops=[Eq()], comparators=[Name(id='expected_features', ctx=Load())])), Assert(test=Call(func=Attribute(value=Compare(left=Name(id='y', ctx=Load()), ops=[Eq()], comparators=[Name(id='targets', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='features_to_use,expected_features'), Tuple(elts=[Tuple(elts=[Constant(value=None), Set(elts=[Constant(value='regressor_target_0'), Constant(value='regressor_target_1')])], ctx=Load()), Tuple(elts=[Constant(value='all'), Set(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_month'), Constant(value='regressor_dateflag_day_number_in_week'), Constant(value='regressor_dateflag_is_weekend'), Constant(value='regressor_target_0'), Constant(value='regressor_target_1')])], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_week'), Constant(value='unknown')], ctx=Load()), Set(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_week'), Constant(value='regressor_target_0'), Constant(value='regressor_target_1')])], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_forecast_interface', args=arguments(posonlyargs=[], args=[arg(arg='example_t'), arg(arg='naive_featured_pipeline_1', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='naive_featured_pipeline_2nfNIM', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='features_to_use', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Constant(value=None), Subscript(value=Name(id='Literal', ctx=Load()), slice=Name(id='all', ctx=Load()), ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='expected_features', annotation=Subscript(value=Name(id='Set', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='ensemble', ctx=Store())], value=Call(func=Attribute(value=Call(func=Name(id='StackingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=List(elts=[Name(id='naive_featured_pipeline_1', ctx=Load()), Name(id='naive_featured_pipeline_2nfNIM', ctx=Load())], ctx=Load())), keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load()))]), attr='fit', ctx=Load()), args=[Name(id='example_t', ctx=Load())], keywords=[])), Assign(targets=[Name(id='forecast', ctx=Store())], value=Call(func=Attribute(value=Name(id='ensemble', ctx=Load()), attr='forecast', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='features', ctx=Store())], value=BinOp(left=Call(func=Name(id='set', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='forecast', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[]), op=Sub(), right=Set(elts=[Constant(value='target')]))), Assert(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='forecast', ctx=Load()), Name(id='TSDataset', ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='lenNYvv', ctx=Load()), args=[Attribute(value=Name(id='forecast', ctx=Load()), attr='df', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Name(id='HORIZON', ctx=Load())])), Assert(test=Compare(left=Name(id='features', ctx=Load()), ops=[Eq()], comparators=[Name(id='expected_features', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='features_to_use,expected_features'), Tuple(elts=[Tuple(elts=[Constant(value=None), Set(elts=[Constant(value='regressor_target_0'), Constant(value='regressor_target_1')])], ctx=Load()), Tuple(elts=[Constant(value='all'), Set(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_month'), Constant(value='regressor_dateflag_day_number_in_week'), Constant(value='regressor_dateflag_is_weekend'), Constant(value='regressor_target_0'), Constant(value='regressor_target_1')])], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_week'), Constant(value='unknown')], ctx=Load()), Set(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_week'), Constant(value='regressor_target_0'), Constant(value='regressor_target_1')])], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_forecast_raise_error_if_not_fitted_', args=arguments(posonlyargs=[], args=[arg(arg='naive_ense_mble', annotation=Name(id='StackingEnsemble', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='T˹est that StackiʸngEnsemble raiφse error whenͶ cal̲ling forecast without being fit.')), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='VALUEERROR', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='StackingEnsemble is not fitted!'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='forecast', ctx=Load()), args=[], keywords=[]))])], decorator_list=[]), FunctionDef(name='test_forecast_prediction_interval_interface', args=arguments(posonlyargs=[], args=[arg(arg='example_t'), arg(arg='naive_ense_mble', annotation=Name(id='StackingEnsemble', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ƇTesƭtǤ the fȈorecζȸa\x7fstĺ Ŏinte\x80rface wεith pr`ed͗iĜctio½n intervaǋlĪƒsŪ.rÓǸ')), Expr(value=Call(func=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='example_t', ctx=Load())], keywords=[])), Assign(targets=[Name(id='forecast', ctx=Store())], value=Call(func=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='forecast', ctx=Load()), args=[], keywords=[keyword(arg='prediction_interval', value=Constant(value=True)), keyword(arg='quantiles', value=List(elts=[Constant(value=0.025), Constant(value=0.975)], ctx=Load()))])), For(target=Name(id='segment', ctx=Store()), iter=Attribute(value=Name(id='forecast', ctx=Load()), attr='segments', ctx=Load()), body=[Assign(targets=[Name(id='segment_slice', ctx=Store())], value=Subscript(value=Subscript(value=Name(id='forecast', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segment', ctx=Load()), Slice()], ctx=Load()), ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load())), Assert(test=Call(func=Attribute(value=Set(elts=[Constant(value='target_0.025'), Constant(value='target_0.975'), Constant(value='target')]), attr='issubset', ctx=Load()), args=[Attribute(value=Name(id='segment_slice', ctx=Load()), attr='columns', ctx=Load())], keywords=[])), Assert(test=Call(func=Attribute(value=Compare(left=BinOp(left=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target_0.975'), ctx=Load()), op=Sub(), right=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target_0.025'), ctx=Load())), ops=[GtE()], comparators=[Constant(value=0)]), attr='all', ctx=Load()), args=[], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='test_multiprocessing_ensembles', args=arguments(posonlyargs=[], args=[arg(arg='simple_df', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='_catboost_pipeline', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='pr', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='naive_pipeline_1', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='na', annotation=Name(id='Pipeline', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='pipelines', ctx=Store())], value=List(elts=[Name(id='_catboost_pipeline', ctx=Load()), Name(id='pr', ctx=Load()), Name(id='naive_pipeline_1', ctx=Load()), Name(id='na', ctx=Load())], ctx=Load())), Assign(targets=[Name(id='SINGLE_JOBS_ENSEMBLE', ctx=Store())], value=Call(func=Name(id='StackingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='pipelines', ctx=Load())], keywords=[])), keyword(arg='n_jobs', value=Constant(value=1))])), Assign(targets=[Name(id='multi_jobs_ensemble', ctx=Store())], value=Call(func=Name(id='StackingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='pipelines', ctx=Load())], keywords=[])), keyword(arg='n_jobs', value=Constant(value=3))])), Expr(value=Call(func=Attribute(value=Name(id='SINGLE_JOBS_ENSEMBLE', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='simple_df', ctx=Load())], keywords=[]))])), Expr(value=Call(func=Attribute(value=Name(id='multi_jobs_ensemble', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='simple_df', ctx=Load())], keywords=[]))])), Assign(targets=[Name(id='single_jobs_forecastRm', ctx=Store())], value=Call(func=Attribute(value=Name(id='SINGLE_JOBS_ENSEMBLE', ctx=Load()), attr='forecast', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='multi_jobs_forecast', ctx=Store())], value=Call(func=Attribute(value=Name(id='multi_jobs_ensemble', ctx=Load()), attr='forecast', ctx=Load()), args=[], keywords=[])), Assert(test=Call(func=Attribute(value=Call(func=Attribute(value=Compare(left=Attribute(value=Name(id='single_jobs_forecastRm', ctx=Load()), attr='df', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Name(id='multi_jobs_forecast', ctx=Load()), attr='df', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[]), attr='all', ctx=Load()), args=[], keywords=[]))], decorator_list=[Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='long_1', ctx=Load())]), FunctionDef(name='test_predict_interface', args=arguments(posonlyargs=[], args=[arg(arg='example_t'), arg(arg='naive_featured_pipeline_1', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='naive_featured_pipeline_2nfNIM', annotation=Name(id='Pipeline', ctx=Load())), arg(arg='features_to_use', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Constant(value=None), Subscript(value=Name(id='Literal', ctx=Load()), slice=Name(id='all', ctx=Load()), ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='expected_features', annotation=Subscript(value=Name(id='Set', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='C˵he.ckˑĸ ȗt˄ɑƯťhaΦ¹t ϟStac˒kin̞zgEȘŹʿnsʌeømbl}e˳ύ\xad.prÏedȄict rˌeȕtΩuƻrnɳs TǪSDatasÝet ΕİΟofŻ correcǫȠt́Ȟʔ l̝enΕ̊gth̨,` cϼoϔΘntaiȑĬning ΜalΙȈl theɖˤ ˗expeˆϏcɈÃt̐eˑǰͼd\u0379¯ coŞʡlǛĥumʹ\x93ǏnsǈɁ')), Assign(targets=[Name(id='ensemble', ctx=Store())], value=Call(func=Attribute(value=Call(func=Name(id='StackingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=List(elts=[Name(id='naive_featured_pipeline_1', ctx=Load()), Name(id='naive_featured_pipeline_2nfNIM', ctx=Load())], ctx=Load())), keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load()))]), attr='fit', ctx=Load()), args=[Name(id='example_t', ctx=Load())], keywords=[])), Assign(targets=[Name(id='start_idx', ctx=Store())], value=Constant(value=20)), Assign(targets=[Name(id='end_idx', ctx=Store())], value=Constant(value=30)), Assign(targets=[Name(id='prediction', ctx=Store())], value=Call(func=Attribute(value=Name(id='ensemble', ctx=Load()), attr='predict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='example_t', ctx=Load())), keyword(arg='start_timestamp', value=Subscript(value=Attribute(value=Name(id='example_t', ctx=Load()), attr='index', ctx=Load()), slice=Name(id='start_idx', ctx=Load()), ctx=Load())), keyword(arg='end_timestamp', value=Subscript(value=Attribute(value=Name(id='example_t', ctx=Load()), attr='index', ctx=Load()), slice=Name(id='end_idx', ctx=Load()), ctx=Load()))])), Assign(targets=[Name(id='features', ctx=Store())], value=BinOp(left=Call(func=Name(id='set', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='prediction', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])], keywords=[]), op=Sub(), right=Set(elts=[Constant(value='target')]))), Assert(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='prediction', ctx=Load()), Name(id='TSDataset', ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='lenNYvv', ctx=Load()), args=[Attribute(value=Name(id='prediction', ctx=Load()), attr='df', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[BinOp(left=BinOp(left=Name(id='end_idx', ctx=Load()), op=Sub(), right=Name(id='start_idx', ctx=Load())), op=Add(), right=Constant(value=1))])), Assert(test=Compare(left=Name(id='features', ctx=Load()), ops=[Eq()], comparators=[Name(id='expected_features', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='features_to_use,expected_features'), Tuple(elts=[Tuple(elts=[Constant(value=None), Set(elts=[Constant(value='regressor_target_0'), Constant(value='regressor_target_1')])], ctx=Load()), Tuple(elts=[Constant(value='all'), Set(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_month'), Constant(value='regressor_dateflag_day_number_in_week'), Constant(value='regressor_dateflag_is_weekend'), Constant(value='regressor_target_0'), Constant(value='regressor_target_1')])], ctx=Load()), Tuple(elts=[List(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_week'), Constant(value='unknown')], ctx=Load()), Set(elts=[Constant(value='regressor_lag_feature_10'), Constant(value='regressor_dateflag_day_number_in_week'), Constant(value='regressor_target_0'), Constant(value='regressor_target_1')])], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_forecast_sanity', args=arguments(posonlyargs=[], args=[arg(arg='weekly_period_t', annotation=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Constant(value='TSDataset'), Constant(value='TSDataset')], ctx=Load()), ctx=Load())), arg(arg='naive_ense_mble', annotation=Name(id='StackingEnsemble', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='train', ctx=Store()), Name(id='test', ctx=Store())], ctx=Store())], value=Name(id='weekly_period_t', ctx=Load())), Assign(targets=[Name(id='ensemble', ctx=Store())], value=Call(func=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='train', ctx=Load())], keywords=[])), Assign(targets=[Name(id='forecast', ctx=Store())], value=Call(func=Attribute(value=Name(id='ensemble', ctx=Load()), attr='forecast', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='mae', ctx=Store())], value=Call(func=Name(id='MAE', ctx=Load()), args=[Constant(value='macro')], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Call(func=Name(id='mae', ctx=Load()), args=[Name(id='test', ctx=Load()), Name(id='forecast', ctx=Load())], keywords=[]), Constant(value=0)], keywords=[]))], decorator_list=[]), FunctionDef(name='test_features_to_use_wrong_format', args=arguments(posonlyargs=[], args=[arg(arg='forecasts_ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='naive_featured_pipeline_1'), arg(arg='naive_featured_pipeline_2nfNIM'), arg(arg='features_to_use', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Constant(value=None), Subscript(value=Name(id='Literal', ctx=Load()), slice=Name(id='all', ctx=Load()), ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='ensemble', ctx=Store())], value=Call(func=Name(id='StackingEnsemble', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=List(elts=[Name(id='naive_featured_pipeline_1', ctx=Load()), Name(id='naive_featured_pipeline_2nfNIM', ctx=Load())], ctx=Load())), keyword(arg='features_to_use', value=Name(id='features_to_use', ctx=Load()))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='warns', ctx=Load()), args=[Name(id='UserWarning', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Feature list is passed in the wrong format.'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='ensemble', ctx=Load()), attr='_filter_features_to_use', ctx=Load()), args=[Name(id='forecasts_ts', ctx=Load())], keywords=[]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='features_to_use'), List(elts=[Constant(value='regressor_lag_feature_10')], ctx=Load())], keywords=[])]), FunctionDef(name='test_backtest', args=arguments(posonlyargs=[], args=[arg(arg='stacking_ensemble_pipeline', annotation=Name(id='StackingEnsemble', ctx=Load())), arg(arg='example_t', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='n_jobs', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Cϗh\x8ee\xadcȱlϷkƱ tha\x94ʘt baicÙhÒkteϺĶsÉϏt ͼ!wɱȽ4or͊Τ͏Ùkʺs wýit˿h StȉacǮˋukingÜEnʸ)s\x96\x86eȥăơmb\x80le.ͬɀRϯP')), Assign(targets=[Name(id='results', ctx=Store())], value=Call(func=Attribute(value=Name(id='stacking_ensemble_pipeline', ctx=Load()), attr='backtest', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='example_t', ctx=Load())), keyword(arg='metrics', value=List(elts=[Call(func=Name(id='MAE', ctx=Load()), args=[], keywords=[])], ctx=Load())), keyword(arg='n_jobs', value=Name(id='n_jobs', ctx=Load())), keyword(arg='n_folds', value=Constant(value=3))])), For(target=Name(id='df', ctx=Store()), iter=Name(id='results', ctx=Load()), body=[Assert(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='df', ctx=Load()), Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='long_1', ctx=Load()), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='n_jobs'), Tuple(elts=[Constant(value=1), Constant(value=5)], ctx=Load())], keywords=[])]), FunctionDef(name='test_forecast_calls_process_forecasts', args=arguments(posonlyargs=[], args=[arg(arg='example_t', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='naive_ense_mble')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  1    Ƃ    ŋ\x84 ')), Expr(value=Call(func=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='example_t', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='_process_forecasts', ctx=Store())], value=Call(func=Name(id='MagicMock', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='_forecast', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='_process_forecasts', ctx=Load()), attr='assert_called_once', ctx=Load()), args=[], keywords=[])), Assert(test=Compare(left=Name(id='result', ctx=Load()), ops=[Eq()], comparators=[Attribute(value=Attribute(value=Name(id='naive_ense_mble', ctx=Load()), attr='_process_forecasts', ctx=Load()), attr='return_value', ctx=Load())]))], decorator_list=[])], type_ignores=[])