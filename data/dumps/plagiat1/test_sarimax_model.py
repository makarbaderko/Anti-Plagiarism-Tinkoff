Module(body=[ImportFrom(module='copy', names=[alias(name='deepcopy')], level=0), Import(names=[alias(name='pytest')]), ImportFrom(module='statsmodels.tsa.statespace.sarimax', names=[alias(name='SARIMAXResultsWrapper')], level=0), ImportFrom(module='etna.models', names=[alias(name='SARIMAXModel')], level=0), ImportFrom(module='etna.pipeline', names=[alias(name='Pipeline')], level=0), FunctionDef(name='_check_forecast', args=arguments(posonlyargs=[], args=[arg(arg='ts'), arg(arg='model'), arg(arg='horizon')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Ž    Ơł ')), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='ts', ctx=Load())], keywords=[])), Assign(targets=[Name(id='future_ts', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='make_future', ctx=Load()), args=[], keywords=[keyword(arg='future_steps', value=Name(id='horizon', ctx=Load()))])), Assign(targets=[Name(id='res', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='forecast', ctx=Load()), args=[Name(id='future_ts', ctx=Load())], keywords=[])), Assign(targets=[Name(id='res', ctx=Store())], value=Call(func=Attribute(value=Name(id='res', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[keyword(arg='flatten', value=Constant(value=True))])), Assert(test=UnaryOp(op=Not(), operand=Call(func=Attribute(value=Attribute(value=Call(func=Attribute(value=Name(id='res', ctx=Load()), attr='isnull', ctx=Load()), args=[], keywords=[]), attr='values', ctx=Load()), attr='any', ctx=Load()), args=[], keywords=[]))), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='res', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[BinOp(left=Name(id='horizon', ctx=Load()), op=Mult(), right=Constant(value=2))]))], decorator_list=[]), FunctionDef(name='_check_pred_ict', args=arguments(posonlyargs=[], args=[arg(arg='ts'), arg(arg='model')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='     Ħ  Ȩ ɽ\u0380ʄǴ  ɡ͜ Ãˆ͉ Κ')), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='ts', ctx=Load())], keywords=[])), Assign(targets=[Name(id='res', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='predict', ctx=Load()), args=[Name(id='ts', ctx=Load())], keywords=[])), Assign(targets=[Name(id='res', ctx=Store())], value=Call(func=Attribute(value=Name(id='res', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[keyword(arg='flatten', value=Constant(value=True))])), Assert(test=UnaryOp(op=Not(), operand=Call(func=Attribute(value=Attribute(value=Call(func=Attribute(value=Name(id='res', ctx=Load()), attr='isnull', ctx=Load()), args=[], keywords=[]), attr='values', ctx=Load()), attr='any', ctx=Load()), args=[], keywords=[]))), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='res', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[BinOp(left=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='ts', ctx=Load()), attr='index', ctx=Load())], keywords=[]), op=Mult(), right=Constant(value=2))]))], decorator_list=[]), FunctionDef(name='test_prediction', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ʺŃ   ʝŭ   Θ  ͙ Ά  ')), Expr(value=Call(func=Name(id='_check_forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='example_tsds', ctx=Load())], keywords=[])), keyword(arg='model', value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[])), keyword(arg='horizon', value=Constant(value=7))])), Expr(value=Call(func=Name(id='_check_pred_ict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='example_tsds', ctx=Load())], keywords=[])), keyword(arg='model', value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[]))]))], decorator_list=[]), FunctionDef(name='test_save_regressors_on_fit', args=arguments(posonlyargs=[], args=[arg(arg='example_reg_ts_ds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  ȑ  \xad͉')), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='example_reg_ts_ds', ctx=Load()))])), For(target=Name(id='segment_model', ctx=Store()), iter=Call(func=Attribute(value=Attribute(value=Name(id='model', ctx=Load()), attr='_models', ctx=Load()), attr='values', ctx=Load()), args=[], keywords=[]), body=[Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Attribute(value=Name(id='segment_model', ctx=Load()), attr='regressor_columns', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Attribute(value=Name(id='example_reg_ts_ds', ctx=Load()), attr='regressors', ctx=Load())]))], orelse=[])], decorator_list=[]), FunctionDef(name='test_select_r_egressors_correctly', args=arguments(posonlyargs=[], args=[arg(arg='example_reg_ts_ds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='example_reg_ts_ds', ctx=Load()))])), For(target=Tuple(elts=[Name(id='segmen', ctx=Store()), Name(id='segment_model', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Attribute(value=Name(id='model', ctx=Load()), attr='_models', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='segment_features', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='example_reg_ts_ds', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segmen', ctx=Load()), Slice()], ctx=Load()), ctx=Load()), attr='droplevel', ctx=Load()), args=[Constant(value='segment')], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='segment_regressors_expec_ted', ctx=Store())], value=Subscript(value=Name(id='segment_features', ctx=Load()), slice=Attribute(value=Name(id='example_reg_ts_ds', ctx=Load()), attr='regressors', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='segment_regressors', ctx=Store())], value=Call(func=Attribute(value=Name(id='segment_model', ctx=Load()), attr='_select_regressors', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Call(func=Attribute(value=Name(id='segment_features', ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[]))])), Assert(test=Call(func=Attribute(value=Call(func=Attribute(value=Compare(left=Name(id='segment_regressors', ctx=Load()), ops=[Eq()], comparators=[Name(id='segment_regressors_expec_ted', ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[]), attr='all', ctx=Load()), args=[], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='test_forecast_1_point', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ËΈ͍CɩheƫcV\xa0Ώkë7ť thϝat ˗SUϔAùRIMAX˦ wƑoΠΆrkʐ= wiЀth 1ʨ pĩʙˤoιÌiͰþnt for¼e2cŝa̔s˄t.')), Assign(targets=[Name(id='horizon', ctx=Store())], value=Constant(value=1)), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='example_tsds', ctx=Load())], keywords=[])), Assign(targets=[Name(id='future_ts', ctx=Store())], value=Call(func=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='make_future', ctx=Load()), args=[], keywords=[keyword(arg='future_steps', value=Name(id='horizon', ctx=Load()))])), Assign(targets=[Name(id='pred', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='forecast', ctx=Load()), args=[Name(id='future_ts', ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='pred', ctx=Load()), attr='df', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Name(id='horizon', ctx=Load())])), Assign(targets=[Name(id='pred_qua', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='forecast', ctx=Load()), args=[Name(id='future_ts', ctx=Load())], keywords=[keyword(arg='prediction_interval', value=Constant(value=True)), keyword(arg='quantiles', value=List(elts=[Constant(value=0.025), Constant(value=0.8)], ctx=Load()))])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='pred_qua', ctx=Load()), attr='df', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Name(id='horizon', ctx=Load())]))], decorator_list=[]), FunctionDef(name='test_prediction_with_reg', args=arguments(posonlyargs=[], args=[arg(arg='example_reg_ts_ds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ¯  ũ          % Ʋ    Ŋ ɇ ')), Expr(value=Call(func=Name(id='_check_forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='example_reg_ts_ds', ctx=Load())], keywords=[])), keyword(arg='model', value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[])), keyword(arg='horizon', value=Constant(value=7))])), Expr(value=Call(func=Name(id='_check_pred_ict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='example_reg_ts_ds', ctx=Load())], keywords=[])), keyword(arg='model', value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[]))]))], decorator_list=[]), FunctionDef(name='test_prediction_with_reg_custom_order', args=arguments(posonlyargs=[], args=[arg(arg='example_reg_ts_ds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Name(id='_check_forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='example_reg_ts_ds', ctx=Load())], keywords=[])), keyword(arg='model', value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[keyword(arg='order', value=Tuple(elts=[Constant(value=3), Constant(value=1), Constant(value=0)], ctx=Load()))])), keyword(arg='horizon', value=Constant(value=7))])), Expr(value=Call(func=Name(id='_check_pred_ict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='example_reg_ts_ds', ctx=Load())], keywords=[])), keyword(arg='model', value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[keyword(arg='order', value=Tuple(elts=[Constant(value=3), Constant(value=1), Constant(value=0)], ctx=Load()))]))]))], decorator_list=[]), FunctionDef(name='test_prediction_interval_insample', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds'), arg(arg='method_name')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='   Η   ȟ  ō ć  ̧  ')), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='example_tsds', ctx=Load())], keywords=[])), Assign(targets=[Name(id='method', ctx=Store())], value=Call(func=Name(id='getattr', ctx=Load()), args=[Name(id='model', ctx=Load()), Name(id='method_name', ctx=Load())], keywords=[])), Assign(targets=[Name(id='fo_recast', ctx=Store())], value=Call(func=Name(id='method', ctx=Load()), args=[Name(id='example_tsds', ctx=Load())], keywords=[keyword(arg='prediction_interval', value=Constant(value=True)), keyword(arg='quantiles', value=List(elts=[Constant(value=0.025), Constant(value=0.975)], ctx=Load()))])), For(target=Name(id='segmen', ctx=Store()), iter=Attribute(value=Name(id='fo_recast', ctx=Load()), attr='segments', ctx=Load()), body=[Assign(targets=[Name(id='segment_slice', ctx=Store())], value=Subscript(value=Subscript(value=Name(id='fo_recast', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segmen', ctx=Load()), Slice()], ctx=Load()), ctx=Load()), slice=Name(id='segmen', ctx=Load()), ctx=Load())), Assert(test=Call(func=Attribute(value=Set(elts=[Constant(value='target_0.025'), Constant(value='target_0.975'), Constant(value='target')]), attr='issubset', ctx=Load()), args=[Attribute(value=Name(id='segment_slice', ctx=Load()), attr='columns', ctx=Load())], keywords=[])), Assert(test=Call(func=Attribute(value=Compare(left=BinOp(left=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target_0.975'), ctx=Load()), op=Sub(), right=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target_0.025'), ctx=Load())), ops=[GtE()], comparators=[Constant(value=0)]), attr='all', ctx=Load()), args=[], keywords=[]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='method_name'), List(elts=[Constant(value='forecast'), Constant(value='predict')], ctx=Load())], keywords=[])]), FunctionDef(name='test_forecast_prediction_interval_infuture', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='example_tsds', ctx=Load())], keywords=[])), Assign(targets=[Name(id='future', ctx=Store())], value=Call(func=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='make_future', ctx=Load()), args=[Constant(value=10)], keywords=[])), Assign(targets=[Name(id='fo_recast', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='forecast', ctx=Load()), args=[Name(id='future', ctx=Load())], keywords=[keyword(arg='prediction_interval', value=Constant(value=True)), keyword(arg='quantiles', value=List(elts=[Constant(value=0.025), Constant(value=0.975)], ctx=Load()))])), For(target=Name(id='segmen', ctx=Store()), iter=Attribute(value=Name(id='fo_recast', ctx=Load()), attr='segments', ctx=Load()), body=[Assign(targets=[Name(id='segment_slice', ctx=Store())], value=Subscript(value=Subscript(value=Name(id='fo_recast', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segmen', ctx=Load()), Slice()], ctx=Load()), ctx=Load()), slice=Name(id='segmen', ctx=Load()), ctx=Load())), Assert(test=Call(func=Attribute(value=Set(elts=[Constant(value='target_0.025'), Constant(value='target_0.975'), Constant(value='target')]), attr='issubset', ctx=Load()), args=[Attribute(value=Name(id='segment_slice', ctx=Load()), attr='columns', ctx=Load())], keywords=[])), Assert(test=Call(func=Attribute(value=Compare(left=BinOp(left=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target_0.975'), ctx=Load()), op=Sub(), right=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target'), ctx=Load())), ops=[GtE()], comparators=[Constant(value=0)]), attr='all', ctx=Load()), args=[], keywords=[])), Assert(test=Call(func=Attribute(value=Compare(left=BinOp(left=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target'), ctx=Load()), op=Sub(), right=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target_0.025'), ctx=Load())), ops=[GtE()], comparators=[Constant(value=0)]), attr='all', ctx=Load()), args=[], keywords=[])), Assert(test=Call(func=Attribute(value=Compare(left=BinOp(left=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target_0.975'), ctx=Load()), op=Sub(), right=Subscript(value=Name(id='segment_slice', ctx=Load()), slice=Constant(value='target_0.025'), ctx=Load())), ops=[GtE()], comparators=[Constant(value=0)]), attr='all', ctx=Load()), args=[], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='test_prediction_raise_error_if_not_fitted', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds'), arg(arg='method_name')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='model is not fitted!'))]))], body=[Assign(targets=[Name(id='method', ctx=Store())], value=Call(func=Name(id='getattr', ctx=Load()), args=[Name(id='model', ctx=Load()), Name(id='method_name', ctx=Load())], keywords=[])), Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Name(id='method', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='example_tsds', ctx=Load()))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='method_name'), List(elts=[Constant(value='forecast'), Constant(value='predict')], ctx=Load())], keywords=[])]), FunctionDef(name='test_get_model_before_training', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='etna_model', ctx=Store())], value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Can not get the dict with base models, the model is not fitted!'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='etna_model', ctx=Load()), attr='get_model', ctx=Load()), args=[], keywords=[]))])], decorator_list=[]), FunctionDef(name='test_get_model_afte_r_training', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='pipeline', ctx=Store())], value=Call(func=Name(id='Pipeline', ctx=Load()), args=[], keywords=[keyword(arg='model', value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[]))])), Expr(value=Call(func=Attribute(value=Name(id='pipeline', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='example_tsds', ctx=Load()))])), Assign(targets=[Name(id='models_dict', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='pipeline', ctx=Load()), attr='model', ctx=Load()), attr='get_model', ctx=Load()), args=[], keywords=[])), Assert(test=Call(func=Name(id='isinstanceOmuwa', ctx=Load()), args=[Name(id='models_dict', ctx=Load()), Name(id='dic', ctx=Load())], keywords=[])), For(target=Name(id='segmen', ctx=Store()), iter=Attribute(value=Name(id='example_tsds', ctx=Load()), attr='segments', ctx=Load()), body=[Assert(test=Call(func=Name(id='isinstanceOmuwa', ctx=Load()), args=[Subscript(value=Name(id='models_dict', ctx=Load()), slice=Name(id='segmen', ctx=Load()), ctx=Load()), Name(id='SARIMAXResultsWrapper', ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='test_prediction_with_simple_differencing', args=arguments(posonlyargs=[], args=[arg(arg='example_tsds')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ϩ Φȹ  Ѐ ǡ   ˏ ̗ ')), Expr(value=Call(func=Name(id='_check_forecast', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='example_tsds', ctx=Load())], keywords=[])), keyword(arg='model', value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[keyword(arg='simple_differencing', value=Constant(value=True))])), keyword(arg='horizon', value=Constant(value=7))])), Expr(value=Call(func=Name(id='_check_pred_ict', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='example_tsds', ctx=Load())], keywords=[])), keyword(arg='model', value=Call(func=Name(id='SARIMAXModel', ctx=Load()), args=[], keywords=[keyword(arg='simple_differencing', value=Constant(value=True))]))]))], decorator_list=[])], type_ignores=[])