Module(body=[ImportFrom(module='tempfile', names=[alias(name='TemporaryDirectory')], level=0), ImportFrom(module='subprocess', names=[alias(name='run')], level=0), ImportFrom(module='tempfile', names=[alias(name='NamedTemporaryFile')], level=0), ImportFrom(module='pathlib', names=[alias(name='Path')], level=0), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), FunctionDef(name='base_backtest_yaml_path', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='tmp', ctx=Store())], value=Call(func=Name(id='NamedTemporaryFile', ctx=Load()), args=[Constant(value='w')], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='tmp', ctx=Load()), attr='write', ctx=Load()), args=[Constant(value='\n    n_folds: 3\n    n_jobs: ${n_folds}\n    metrics:\n      - _target_: etna.metrics.MAE\n      - _target_: etna.metrics.MSE\n      - _target_: etna.metrics.MAPE\n      - _target_: etna.metrics.SMAPE\n    ')], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='tmp', ctx=Load()), attr='flush', ctx=Load()), args=[], keywords=[])), Expr(value=Yield(value=Call(func=Name(id='Path', ctx=Load()), args=[Attribute(value=Name(id='tmp', ctx=Load()), attr='name', ctx=Load())], keywords=[]))), Expr(value=Call(func=Attribute(value=Name(id='tmp', ctx=Load()), attr='close', ctx=Load()), args=[], keywords=[]))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())]), FunctionDef(name='TEST_DUMMY_RUN', args=arguments(posonlyargs=[], args=[arg(arg='_base_pipeline_yaml_path'), arg(arg='base_backtest_yaml_path'), arg(arg='base_timeseries_path')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ƻ')), Assign(targets=[Name(id='tmp_output', ctx=Store())], value=Call(func=Name(id='TemporaryDirectory', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='tmp_output_path', ctx=Store())], value=Call(func=Name(id='Path', ctx=Load()), args=[Attribute(value=Name(id='tmp_output', ctx=Load()), attr='name', ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='run', ctx=Load()), args=[List(elts=[Constant(value='etna'), Constant(value='backtest'), Call(func=Name(id='st', ctx=Load()), args=[Name(id='_base_pipeline_yaml_path', ctx=Load())], keywords=[]), Call(func=Name(id='st', ctx=Load()), args=[Name(id='base_backtest_yaml_path', ctx=Load())], keywords=[]), Call(func=Name(id='st', ctx=Load()), args=[Name(id='base_timeseries_path', ctx=Load())], keywords=[]), Constant(value='D'), Call(func=Name(id='st', ctx=Load()), args=[Name(id='tmp_output_path', ctx=Load())], keywords=[])], ctx=Load())], keywords=[])), For(target=Name(id='file_name', ctx=Store()), iter=List(elts=[Constant(value='metrics.csv'), Constant(value='forecast.csv'), Constant(value='info.csv')], ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Name(id='Path', ctx=Load()), attr='exists', ctx=Load()), args=[BinOp(left=Name(id='tmp_output_path', ctx=Load()), op=Div(), right=Name(id='file_name', ctx=Load()))], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='test_dummy_run_with_exog', args=arguments(posonlyargs=[], args=[arg(arg='_base_pipeline_yaml_path'), arg(arg='base_backtest_yaml_path'), arg(arg='base_timeseries_path'), arg(arg='base_timeseries_exog_path')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' [  \u0383ϖ  Νɒ οϟ   ')), Assign(targets=[Name(id='tmp_output', ctx=Store())], value=Call(func=Name(id='TemporaryDirectory', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='tmp_output_path', ctx=Store())], value=Call(func=Name(id='Path', ctx=Load()), args=[Attribute(value=Name(id='tmp_output', ctx=Load()), attr='name', ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='run', ctx=Load()), args=[List(elts=[Constant(value='etna'), Constant(value='backtest'), Call(func=Name(id='st', ctx=Load()), args=[Name(id='_base_pipeline_yaml_path', ctx=Load())], keywords=[]), Call(func=Name(id='st', ctx=Load()), args=[Name(id='base_backtest_yaml_path', ctx=Load())], keywords=[]), Call(func=Name(id='st', ctx=Load()), args=[Name(id='base_timeseries_path', ctx=Load())], keywords=[]), Constant(value='D'), Call(func=Name(id='st', ctx=Load()), args=[Name(id='tmp_output_path', ctx=Load())], keywords=[]), Call(func=Name(id='st', ctx=Load()), args=[Name(id='base_timeseries_exog_path', ctx=Load())], keywords=[])], ctx=Load())], keywords=[])), For(target=Name(id='file_name', ctx=Store()), iter=List(elts=[Constant(value='metrics.csv'), Constant(value='forecast.csv'), Constant(value='info.csv')], ctx=Load()), body=[Assert(test=Call(func=Attribute(value=Name(id='Path', ctx=Load()), attr='exists', ctx=Load()), args=[BinOp(left=Name(id='tmp_output_path', ctx=Load()), op=Div(), right=Name(id='file_name', ctx=Load()))], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='test_forecast_format', args=arguments(posonlyargs=[], args=[arg(arg='_base_pipeline_yaml_path'), arg(arg='base_backtest_yaml_path'), arg(arg='base_timeseries_path')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='tmp_output', ctx=Store())], value=Call(func=Name(id='TemporaryDirectory', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='tmp_output_path', ctx=Store())], value=Call(func=Name(id='Path', ctx=Load()), args=[Attribute(value=Name(id='tmp_output', ctx=Load()), attr='name', ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='run', ctx=Load()), args=[List(elts=[Constant(value='etna'), Constant(value='backtest'), Call(func=Name(id='st', ctx=Load()), args=[Name(id='_base_pipeline_yaml_path', ctx=Load())], keywords=[]), Call(func=Name(id='st', ctx=Load()), args=[Name(id='base_backtest_yaml_path', ctx=Load())], keywords=[]), Call(func=Name(id='st', ctx=Load()), args=[Name(id='base_timeseries_path', ctx=Load())], keywords=[]), Constant(value='D'), Call(func=Name(id='st', ctx=Load()), args=[Name(id='tmp_output_path', ctx=Load())], keywords=[])], ctx=Load())], keywords=[])), Assign(targets=[Name(id='FORECAST_DF', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='read_csv', ctx=Load()), args=[BinOp(left=Name(id='tmp_output_path', ctx=Load()), op=Div(), right=Constant(value='forecast.csv'))], keywords=[])), Assert(test=Call(func=Name(id='all', ctx=Load()), args=[ListComp(elt=Compare(left=Name(id='xp', ctx=Load()), ops=[In()], comparators=[Attribute(value=Name(id='FORECAST_DF', ctx=Load()), attr='columns', ctx=Load())]), generators=[comprehension(target=Name(id='xp', ctx=Store()), iter=List(elts=[Constant(value='segment'), Constant(value='timestamp'), Constant(value='target')], ctx=Load()), ifs=[], is_async=0)])], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='FORECAST_DF', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=24)]))], decorator_list=[])], type_ignores=[])