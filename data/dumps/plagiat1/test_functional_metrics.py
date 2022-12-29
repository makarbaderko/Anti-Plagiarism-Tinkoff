Module(body=[Import(names=[alias(name='pytest')]), ImportFrom(module='etna.metrics', names=[alias(name='mae')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='mape')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='medae')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='mse')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='msle')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='r2_score')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='sign')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='smape')], level=0), FunctionDef(name='right_mae_value', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Pass()], decorator_list=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[], keywords=[])]), FunctionDef(name='y_true_1d', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  \x94Ǳ   L  ø̍\x8bͿɛ   ˬ ̯ ɲ   o  ')), Return(value=List(elts=[Constant(value=1), Constant(value=1)], ctx=Load()))], decorator_list=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[], keywords=[])]), FunctionDef(name='y_pred_1d', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=List(elts=[Constant(value=2), Constant(value=2)], ctx=Load()))], decorator_list=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[], keywords=[])]), FunctionDef(name='test_all_1d_metrics', args=arguments(posonlyargs=[], args=[arg(arg='metric'), arg(arg='right_metrics_value'), arg(arg='y_true_1d'), arg(arg='y_pred_1d')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assert(test=Compare(left=Call(func=Name(id='round', ctx=Load()), args=[Call(func=Name(id='metric', ctx=Load()), args=[Name(id='y_true_1d', ctx=Load()), Name(id='y_pred_1d', ctx=Load())], keywords=[]), Constant(value=10)], keywords=[]), ops=[Eq()], comparators=[Name(id='right_metrics_value', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric, right_metrics_value'), Tuple(elts=[Tuple(elts=[Name(id='mae', ctx=Load()), Constant(value=1)], ctx=Load()), Tuple(elts=[Name(id='mse', ctx=Load()), Constant(value=1)], ctx=Load()), Tuple(elts=[Name(id='mape', ctx=Load()), Constant(value=100)], ctx=Load()), Tuple(elts=[Name(id='smape', ctx=Load()), Constant(value=66.6666666667)], ctx=Load()), Tuple(elts=[Name(id='medae', ctx=Load()), Constant(value=1)], ctx=Load()), Tuple(elts=[Name(id='r2_score', ctx=Load()), Constant(value=0)], ctx=Load()), Tuple(elts=[Name(id='sign', ctx=Load()), UnaryOp(op=USub(), operand=Constant(value=1))], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_mle_metric_exception', args=arguments(posonlyargs=[], args=[arg(arg='y_true_1d'), arg(arg='y_pred_1d')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ĬϷ  ί ˕˅ ĥ Ⱥ  ˝Ô ɂŅș   ķ   Ȭ͡ ģ ǀŵ Ɠ ')), Assign(targets=[Subscript(value=Name(id='y_true_1d', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Store())], value=UnaryOp(op=USub(), operand=Constant(value=1))), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='Value_Error', ctx=Load())], keywords=[]))], body=[Expr(value=Call(func=Name(id='msle', ctx=Load()), args=[Name(id='y_true_1d', ctx=Load()), Name(id='y_pred_1d', ctx=Load())], keywords=[]))])], decorator_list=[]), FunctionDef(name='y_true_2d', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='    ʈˠ  ;/ ̳Ɛ')), Return(value=List(elts=[List(elts=[Constant(value=1), Constant(value=1)], ctx=Load()), List(elts=[Constant(value=1), Constant(value=1)], ctx=Load())], ctx=Load()))], decorator_list=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[], keywords=[])]), FunctionDef(name='y_pred_2d', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=List(elts=[List(elts=[Constant(value=2), Constant(value=2)], ctx=Load()), List(elts=[Constant(value=2), Constant(value=2)], ctx=Load())], ctx=Load()))], decorator_list=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[], keywords=[])]), FunctionDef(name='test_all_2d_metrics', args=arguments(posonlyargs=[], args=[arg(arg='metric'), arg(arg='right_metrics_value'), arg(arg='y_true_2d'), arg(arg='y_pred_2d')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assert(test=Compare(left=Call(func=Name(id='round', ctx=Load()), args=[Call(func=Name(id='metric', ctx=Load()), args=[Name(id='y_true_2d', ctx=Load()), Name(id='y_pred_2d', ctx=Load())], keywords=[]), Constant(value=10)], keywords=[]), ops=[Eq()], comparators=[Name(id='right_metrics_value', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric, right_metrics_value'), Tuple(elts=[Tuple(elts=[Name(id='mae', ctx=Load()), Constant(value=1)], ctx=Load()), Tuple(elts=[Name(id='mse', ctx=Load()), Constant(value=1)], ctx=Load()), Tuple(elts=[Name(id='mape', ctx=Load()), Constant(value=100)], ctx=Load()), Tuple(elts=[Name(id='smape', ctx=Load()), Constant(value=66.6666666667)], ctx=Load()), Tuple(elts=[Name(id='medae', ctx=Load()), Constant(value=1)], ctx=Load()), Tuple(elts=[Name(id='r2_score', ctx=Load()), Constant(value=0.0)], ctx=Load()), Tuple(elts=[Name(id='sign', ctx=Load()), UnaryOp(op=USub(), operand=Constant(value=1))], ctx=Load())], ctx=Load())], keywords=[])])], type_ignores=[])