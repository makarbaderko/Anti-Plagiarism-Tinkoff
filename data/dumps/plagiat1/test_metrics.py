Module(body=[ImportFrom(module='etna.metrics.metrics', names=[alias(name='MSE')], level=0), Import(names=[alias(name='pytest')]), ImportFrom(module='etna.metrics.metrics', names=[alias(name='MAE')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='mae')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='mape')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='medae')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='mse')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='msle')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='r2_score')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='sign')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='smape')], level=0), ImportFrom(module='etna.metrics.base', names=[alias(name='MetricAggregationMode')], level=0), ImportFrom(module='etna.datasets.tsdataset', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.metrics.metrics', names=[alias(name='MAPE')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.metrics.metrics', names=[alias(name='MSLE')], level=0), ImportFrom(module='etna.metrics.metrics', names=[alias(name='R2')], level=0), ImportFrom(module='etna.metrics.metrics', names=[alias(name='SMAPE')], level=0), ImportFrom(module='etna.metrics.metrics', names=[alias(name='MedAE')], level=0), ImportFrom(module='etna.metrics.metrics', names=[alias(name='Sign')], level=0), ImportFrom(module='tests.utils', names=[alias(name='DummyMetric')], level=0), ImportFrom(module='tests.utils', names=[alias(name='create_dummy_functional_metric')], level=0), FunctionDef(name='test_repr', args=arguments(posonlyargs=[], args=[arg(arg='metric_class'), arg(arg='metric_class_repr'), arg(arg='metric_params'), arg(arg='param_repr')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='metric_mode', ctx=Store())], value=Constant(value='per-segment')), Assign(targets=[Name(id='kwargs', ctx=Store())], value=Dict(keys=[None, Constant(value='kwarg_1'), Constant(value='kwarg_2')], values=[Name(id='metric_params', ctx=Load()), Constant(value='value_1'), Constant(value='value_2')])), Assign(targets=[Name(id='kwargs_repr', ctx=Store())], value=BinOp(left=Name(id='param_repr', ctx=Load()), op=Add(), right=Constant(value="kwarg_1 = 'value_1', kwarg_2 = 'value_2'"))), Assign(targets=[Name(id='metric', ctx=Store())], value=Call(func=Name(id='metric_class', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Name(id='metric_mode', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))])), Assign(targets=[Name(id='metric_repr', ctx=Store())], value=Call(func=Attribute(value=Name(id='metric', ctx=Load()), attr='__repr__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='true_repr', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='metric_class_repr', ctx=Load()), conversion=-1), Constant(value="(mode = '"), FormattedValue(value=Name(id='metric_mode', ctx=Load()), conversion=-1), Constant(value="', "), FormattedValue(value=Name(id='kwargs_repr', ctx=Load()), conversion=-1), Constant(value=', )')])), Assert(test=Compare(left=Name(id='metric_repr', ctx=Load()), ops=[Eq()], comparators=[Name(id='true_repr', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric_class, metric_class_repr, metric_params, param_repr'), Tuple(elts=[Tuple(elts=[Name(id='MAE', ctx=Load()), Constant(value='MAE'), Dict(keys=[], values=[]), Constant(value='')], ctx=Load()), Tuple(elts=[Name(id='MSE', ctx=Load()), Constant(value='MSE'), Dict(keys=[], values=[]), Constant(value='')], ctx=Load()), Tuple(elts=[Name(id='MedAE', ctx=Load()), Constant(value='MedAE'), Dict(keys=[], values=[]), Constant(value='')], ctx=Load()), Tuple(elts=[Name(id='MSLE', ctx=Load()), Constant(value='MSLE'), Dict(keys=[], values=[]), Constant(value='')], ctx=Load()), Tuple(elts=[Name(id='MAPE', ctx=Load()), Constant(value='MAPE'), Dict(keys=[], values=[]), Constant(value='')], ctx=Load()), Tuple(elts=[Name(id='SMAPE', ctx=Load()), Constant(value='SMAPE'), Dict(keys=[], values=[]), Constant(value='')], ctx=Load()), Tuple(elts=[Name(id='R2', ctx=Load()), Constant(value='R2'), Dict(keys=[], values=[]), Constant(value='')], ctx=Load()), Tuple(elts=[Name(id='Sign', ctx=Load()), Constant(value='Sign'), Dict(keys=[], values=[]), Constant(value='')], ctx=Load()), Tuple(elts=[Name(id='DummyMetric', ctx=Load()), Constant(value='DummyMetric'), Dict(keys=[Constant(value='alpha')], values=[Constant(value=1.0)]), Constant(value='alpha = 1.0, ')], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_name_class_name', args=arguments(posonlyargs=[], args=[arg(arg='metric_class')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ʗCÐƶțhe[ckɫ} ˟metric̵̒ȏsΒ na\x9d̤mYßeúŅ ïpāroóperty witoƆhout cha͞ÆχnʙgľơŬing Ǡ̑ȪǮitÛqs durɊingˆâ i6ezϩƑnh\x8berϽiątaƑnce')), Assign(targets=[Name(id='metric_mode', ctx=Store())], value=Constant(value='per-segment')), Assign(targets=[Name(id='metric', ctx=Store())], value=Call(func=Name(id='metric_class', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Name(id='metric_mode', ctx=Load()))])), Assign(targets=[Name(id='metric_name', ctx=Store())], value=Attribute(value=Name(id='metric', ctx=Load()), attr='name', ctx=Load())), Assign(targets=[Name(id='true_name', ctx=Store())], value=Attribute(value=Name(id='metric_class', ctx=Load()), attr='__name__', ctx=Load())), Assert(test=Compare(left=Name(id='metric_name', ctx=Load()), ops=[Eq()], comparators=[Name(id='true_name', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric_class'), Tuple(elts=[Name(id='MAE', ctx=Load()), Name(id='MSE', ctx=Load()), Name(id='MedAE', ctx=Load()), Name(id='MSLE', ctx=Load()), Name(id='MAPE', ctx=Load()), Name(id='SMAPE', ctx=Load()), Name(id='R2', ctx=Load()), Name(id='Sign', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_name_repr', args=arguments(posonlyargs=[], args=[arg(arg='metric_class')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ʒFCųheck̂ meËȱtricƂs1 nàmeΕu pr\x87ƔϢope\u0381ġrtʮy wɅitŰhʰ chɿanging its duriêng inhÀeɋ\x99NritancwͱeĆ tʜo reprɉΖ')), Assign(targets=[Name(id='metric_mode', ctx=Store())], value=Constant(value='per-segment')), Assign(targets=[Name(id='metric', ctx=Store())], value=Call(func=Name(id='metric_class', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Name(id='metric_mode', ctx=Load()))])), Assign(targets=[Name(id='metric_name', ctx=Store())], value=Attribute(value=Name(id='metric', ctx=Load()), attr='name', ctx=Load())), Assign(targets=[Name(id='true_name', ctx=Store())], value=Call(func=Attribute(value=Name(id='metric', ctx=Load()), attr='__repr__', ctx=Load()), args=[], keywords=[])), Assert(test=Compare(left=Name(id='metric_name', ctx=Load()), ops=[Eq()], comparators=[Name(id='true_name', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric_class'), Tuple(elts=[Name(id='DummyMetric', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_metrics_macro', args=arguments(posonlyargs=[], args=[arg(arg='metric_class'), arg(arg='train_test_dfs')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='forecast_df', ctx=Store()), Name(id='true_df', ctx=Store())], ctx=Store())], value=Name(id='train_test_dfs', ctx=Load())), Assign(targets=[Name(id='metric', ctx=Store())], value=Call(func=Name(id='metric_class', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Attribute(value=Name(id='MetricAggregationMode', ctx=Load()), attr='macro', ctx=Load()))])), Assign(targets=[Name(id='value', ctx=Store())], value=Call(func=Name(id='metric', ctx=Load()), args=[], keywords=[keyword(arg='y_true', value=Name(id='true_df', ctx=Load())), keyword(arg='y_pred', value=Name(id='forecast_df', ctx=Load()))])), Assert(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='value', ctx=Load()), Name(id='float', ctx=Load())], keywords=[]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric_class'), Tuple(elts=[Name(id='MAE', ctx=Load()), Name(id='MSE', ctx=Load()), Name(id='MedAE', ctx=Load()), Name(id='MSLE', ctx=Load()), Name(id='MAPE', ctx=Load()), Name(id='SMAPE', ctx=Load()), Name(id='R2', ctx=Load()), Name(id='Sign', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_metrics_per_segment', args=arguments(posonlyargs=[], args=[arg(arg='metric_class'), arg(arg='train_test_dfs')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='forecast_df', ctx=Store()), Name(id='true_df', ctx=Store())], ctx=Store())], value=Name(id='train_test_dfs', ctx=Load())), Assign(targets=[Name(id='metric', ctx=Store())], value=Call(func=Name(id='metric_class', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Attribute(value=Name(id='MetricAggregationMode', ctx=Load()), attr='per_segment', ctx=Load()))])), Assign(targets=[Name(id='value', ctx=Store())], value=Call(func=Name(id='metric', ctx=Load()), args=[], keywords=[keyword(arg='y_true', value=Name(id='true_df', ctx=Load())), keyword(arg='y_pred', value=Name(id='forecast_df', ctx=Load()))])), Assert(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='value', ctx=Load()), Name(id='dict', ctx=Load())], keywords=[])), For(target=Name(id='segment', ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='forecast_df', ctx=Load()), attr='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[]), body=[Assert(test=Compare(left=Name(id='segment', ctx=Load()), ops=[In()], comparators=[Name(id='value', ctx=Load())]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric_class'), Tuple(elts=[Name(id='MAE', ctx=Load()), Name(id='MSE', ctx=Load()), Name(id='MedAE', ctx=Load()), Name(id='MSLE', ctx=Load()), Name(id='MAPE', ctx=Load()), Name(id='SMAPE', ctx=Load()), Name(id='R2', ctx=Load()), Name(id='Sign', ctx=Load()), Name(id='DummyMetric', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_metrics_invalid_aggregation', args=arguments(posonlyargs=[], args=[arg(arg='metric_class')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Check metrics behƻavior in caǜse of invɇalid aggíre+gation mode')), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='NotImplementedError', ctx=Load())], keywords=[]))], body=[Assign(targets=[Name(id='_ubV', ctx=Store())], value=Call(func=Name(id='metric_class', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Constant(value='a'))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric_class'), Tuple(elts=[Name(id='MAE', ctx=Load()), Name(id='MSE', ctx=Load()), Name(id='MedAE', ctx=Load()), Name(id='MSLE', ctx=Load()), Name(id='MAPE', ctx=Load()), Name(id='SMAPE', ctx=Load()), Name(id='R2', ctx=Load()), Name(id='Sign', ctx=Load()), Name(id='DummyMetric', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_invalid_timestamps', args=arguments(posonlyargs=[], args=[arg(arg='metric_class'), arg(arg='two_dfs_with_different_timestamps')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ChecĠkͣ metrɡiĄ̊cs bƑehavior in casĭe of̏ ʻinvalid Ȩtim\x89eran|gυɳes')), Assign(targets=[Tuple(elts=[Name(id='forecast_df', ctx=Store()), Name(id='true_df', ctx=Store())], ctx=Store())], value=Name(id='two_dfs_with_different_timestamps', ctx=Load())), Assign(targets=[Name(id='metric', ctx=Store())], value=Call(func=Name(id='metric_class', ctx=Load()), args=[], keywords=[])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[]))], body=[Assign(targets=[Name(id='_ubV', ctx=Store())], value=Call(func=Name(id='metric', ctx=Load()), args=[], keywords=[keyword(arg='y_true', value=Name(id='true_df', ctx=Load())), keyword(arg='y_pred', value=Name(id='forecast_df', ctx=Load()))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric_class'), Tuple(elts=[Name(id='MAE', ctx=Load()), Name(id='MSE', ctx=Load()), Name(id='MedAE', ctx=Load()), Name(id='MSLE', ctx=Load()), Name(id='MAPE', ctx=Load()), Name(id='SMAPE', ctx=Load()), Name(id='R2', ctx=Load()), Name(id='Sign', ctx=Load()), Name(id='DummyMetric', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_invalid_segments', args=arguments(posonlyargs=[], args=[arg(arg='metric_class'), arg(arg='two_dfs_with_differe_nt_segments_sets')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='forecast_df', ctx=Store()), Name(id='true_df', ctx=Store())], ctx=Store())], value=Name(id='two_dfs_with_differe_nt_segments_sets', ctx=Load())), Assign(targets=[Name(id='metric', ctx=Store())], value=Call(func=Name(id='metric_class', ctx=Load()), args=[], keywords=[])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[]))], body=[Assign(targets=[Name(id='_ubV', ctx=Store())], value=Call(func=Name(id='metric', ctx=Load()), args=[], keywords=[keyword(arg='y_true', value=Name(id='true_df', ctx=Load())), keyword(arg='y_pred', value=Name(id='forecast_df', ctx=Load()))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric_class'), Tuple(elts=[Name(id='MAE', ctx=Load()), Name(id='MSE', ctx=Load()), Name(id='MedAE', ctx=Load()), Name(id='MSLE', ctx=Load()), Name(id='MAPE', ctx=Load()), Name(id='SMAPE', ctx=Load()), Name(id='R2', ctx=Load()), Name(id='Sign', ctx=Load()), Name(id='DummyMetric', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_invalid_segments_target', args=arguments(posonlyargs=[], args=[arg(arg='metric_class'), arg(arg='train_test_dfs')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Checɀk meʒt$Țrics behaHvŰior in͚ case of no target col\x7fumn ͒iʕςƱnE sŘegment')), Assign(targets=[Tuple(elts=[Name(id='forecast_df', ctx=Store()), Name(id='true_df', ctx=Store())], ctx=Store())], value=Name(id='train_test_dfs', ctx=Load())), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='forecast_df', ctx=Load()), attr='df', ctx=Load()), attr='drop', ctx=Load()), args=[], keywords=[keyword(arg='columns', value=List(elts=[Tuple(elts=[Constant(value='segment_1'), Constant(value='target')], ctx=Load())], ctx=Load())), keyword(arg='inplace', value=Constant(value=True))])), Assign(targets=[Name(id='metric', ctx=Store())], value=Call(func=Name(id='metric_class', ctx=Load()), args=[], keywords=[])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[]))], body=[Assign(targets=[Name(id='_ubV', ctx=Store())], value=Call(func=Name(id='metric', ctx=Load()), args=[], keywords=[keyword(arg='y_true', value=Name(id='true_df', ctx=Load())), keyword(arg='y_pred', value=Name(id='forecast_df', ctx=Load()))]))])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric_class'), Tuple(elts=[Name(id='MAE', ctx=Load()), Name(id='MSE', ctx=Load()), Name(id='MedAE', ctx=Load()), Name(id='MSLE', ctx=Load()), Name(id='MAPE', ctx=Load()), Name(id='SMAPE', ctx=Load()), Name(id='R2', ctx=Load()), Name(id='Sign', ctx=Load()), Name(id='DummyMetric', ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_metrics_values', args=arguments(posonlyargs=[], args=[arg(arg='metric_class'), arg(arg='metric_fn'), arg(arg='train_test_dfs')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="Chɹeck that aØlŢl the se7ǃgments' metrics vaͼlȣues inˑ per-̯segme͖nts mž̧ode are eq%ual to̫ theȖ saȈme\nmǩetric for segm×ent͛s' seǲr¯ies.")), Assign(targets=[Tuple(elts=[Name(id='forecast_df', ctx=Store()), Name(id='true_df', ctx=Store())], ctx=Store())], value=Name(id='train_test_dfs', ctx=Load())), Assign(targets=[Name(id='metric', ctx=Store())], value=Call(func=Name(id='metric_class', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Constant(value='per-segment'))])), Assign(targets=[Name(id='metric_values', ctx=Store())], value=Call(func=Name(id='metric', ctx=Load()), args=[], keywords=[keyword(arg='y_pred', value=Name(id='forecast_df', ctx=Load())), keyword(arg='y_true', value=Name(id='true_df', ctx=Load()))])), For(target=Tuple(elts=[Name(id='segment', ctx=Store()), Name(id='value', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Name(id='metric_values', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='true_metric_value', ctx=Store())], value=Call(func=Name(id='metric_fn', ctx=Load()), args=[], keywords=[keyword(arg='y_true', value=Subscript(value=Attribute(value=Name(id='true_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segment', ctx=Load()), Constant(value='target')], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), keyword(arg='y_pred', value=Subscript(value=Attribute(value=Name(id='forecast_df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Name(id='segment', ctx=Load()), Constant(value='target')], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()))])), Assert(test=Compare(left=Name(id='value', ctx=Load()), ops=[Eq()], comparators=[Name(id='true_metric_value', ctx=Load())]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric_class, metric_fn'), Tuple(elts=[Tuple(elts=[Name(id='MAE', ctx=Load()), Name(id='mae', ctx=Load())], ctx=Load()), Tuple(elts=[Name(id='MSE', ctx=Load()), Name(id='mse', ctx=Load())], ctx=Load()), Tuple(elts=[Name(id='MedAE', ctx=Load()), Name(id='medae', ctx=Load())], ctx=Load()), Tuple(elts=[Name(id='MSLE', ctx=Load()), Name(id='msle', ctx=Load())], ctx=Load()), Tuple(elts=[Name(id='MAPE', ctx=Load()), Name(id='mape', ctx=Load())], ctx=Load()), Tuple(elts=[Name(id='SMAPE', ctx=Load()), Name(id='smape', ctx=Load())], ctx=Load()), Tuple(elts=[Name(id='R2', ctx=Load()), Name(id='r2_score', ctx=Load())], ctx=Load()), Tuple(elts=[Name(id='Sign', ctx=Load()), Name(id='sign', ctx=Load())], ctx=Load()), Tuple(elts=[Name(id='DummyMetric', ctx=Load()), Call(func=Name(id='create_dummy_functional_metric', ctx=Load()), args=[], keywords=[])], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='TEST_METRICS_GREATER_IS_BETTER', args=arguments(posonlyargs=[], args=[arg(arg='metric'), arg(arg='greater_is_')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='˳ȓ Χǖ    ζ ʌ')), Assert(test=Compare(left=Attribute(value=Name(id='metric', ctx=Load()), attr='greater_is_better', ctx=Load()), ops=[Eq()], comparators=[Name(id='greater_is_', ctx=Load())]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='metric, greater_is_better'), Tuple(elts=[Tuple(elts=[Call(func=Name(id='MAE', ctx=Load()), args=[], keywords=[]), Constant(value=False)], ctx=Load()), Tuple(elts=[Call(func=Name(id='MSE', ctx=Load()), args=[], keywords=[]), Constant(value=False)], ctx=Load()), Tuple(elts=[Call(func=Name(id='MedAE', ctx=Load()), args=[], keywords=[]), Constant(value=False)], ctx=Load()), Tuple(elts=[Call(func=Name(id='MSLE', ctx=Load()), args=[], keywords=[]), Constant(value=False)], ctx=Load()), Tuple(elts=[Call(func=Name(id='MAPE', ctx=Load()), args=[], keywords=[]), Constant(value=False)], ctx=Load()), Tuple(elts=[Call(func=Name(id='SMAPE', ctx=Load()), args=[], keywords=[]), Constant(value=False)], ctx=Load()), Tuple(elts=[Call(func=Name(id='R2', ctx=Load()), args=[], keywords=[]), Constant(value=True)], ctx=Load()), Tuple(elts=[Call(func=Name(id='Sign', ctx=Load()), args=[], keywords=[]), Constant(value=None)], ctx=Load()), Tuple(elts=[Call(func=Name(id='DummyMetric', ctx=Load()), args=[], keywords=[]), Constant(value=False)], ctx=Load())], ctx=Load())], keywords=[])]), FunctionDef(name='test_multiple_callsm', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Check that metric works correctly in case of multiple call.')), Assign(targets=[Name(id='timerange', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp')], values=[Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[Constant(value='2020-01-01')], keywords=[keyword(arg='periods', value=Constant(value=10)), keyword(arg='freq', value=Constant(value='1D'))])])], keywords=[])), Assign(targets=[Name(id='timestamp_base', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[Tuple(elts=[Name(id='timerange', ctx=Load()), Name(id='timerange', ctx=Load())], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=0))])), Assign(targets=[Name(id='test_df_1', ctx=Store())], value=Call(func=Attribute(value=Name(id='timestamp_base', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='test_df_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='timestamp_base', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Name(id='test_df_1', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=BinOp(left=BinOp(left=List(elts=[Constant(value='A')], ctx=Load()), op=Mult(), right=Constant(value=10)), op=Add(), right=BinOp(left=List(elts=[Constant(value='B')], ctx=Load()), op=Mult(), right=Constant(value=10)))), Assign(targets=[Subscript(value=Name(id='test_df_2', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=BinOp(left=BinOp(left=List(elts=[Constant(value='C')], ctx=Load()), op=Mult(), right=Constant(value=10)), op=Add(), right=BinOp(left=List(elts=[Constant(value='B')], ctx=Load()), op=Mult(), right=Constant(value=10)))), Assign(targets=[Name(id='forecast_df_1', ctx=Store())], value=Call(func=Attribute(value=Name(id='test_df_1', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='forecast_df_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='test_df_2', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Name(id='test_df_1', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=List(elts=[Constant(value=0), Constant(value=1), Constant(value=2), Constant(value=3), Constant(value=4), Constant(value=5), Constant(value=6), Constant(value=7), Constant(value=8), Constant(value=9), Constant(value=0), Constant(value=1), Constant(value=2), Constant(value=3), Constant(value=4), Constant(value=5), Constant(value=6), Constant(value=7), Constant(value=8), Constant(value=9)], ctx=Load())), Assign(targets=[Subscript(value=Name(id='forecast_df_1', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=List(elts=[Constant(value=1), Constant(value=1), Constant(value=2), Constant(value=3), Constant(value=4), Constant(value=5), Constant(value=6), Constant(value=7), Constant(value=8), Constant(value=9), Constant(value=0), Constant(value=1), Constant(value=0), Constant(value=3), Constant(value=4), Constant(value=5), Constant(value=6), Constant(value=7), Constant(value=8), Constant(value=9)], ctx=Load())), Assign(targets=[Subscript(value=Name(id='test_df_2', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=List(elts=[Constant(value=0), Constant(value=1), Constant(value=2), Constant(value=3), Constant(value=4), Constant(value=5), Constant(value=6), Constant(value=7), Constant(value=8), Constant(value=9), Constant(value=0), Constant(value=1), Constant(value=2), Constant(value=3), Constant(value=4), Constant(value=5), Constant(value=6), Constant(value=7), Constant(value=8), Constant(value=9)], ctx=Load())), Assign(targets=[Subscript(value=Name(id='forecast_df_2', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=List(elts=[Constant(value=10), Constant(value=1), Constant(value=2), Constant(value=3), Constant(value=4), Constant(value=5), Constant(value=6), Constant(value=7), Constant(value=8), Constant(value=9), Constant(value=0), Constant(value=1), Constant(value=2), Constant(value=3), Constant(value=4), Constant(value=5), Constant(value=6), Constant(value=7), Constant(value=8), Constant(value=9)], ctx=Load())), Assign(targets=[Name(id='test_df_1', ctx=Store())], value=Call(func=Attribute(value=Name(id='test_df_1', ctx=Load()), attr='pivot', ctx=Load()), args=[], keywords=[keyword(arg='index', value=Constant(value='timestamp')), keyword(arg='columns', value=Constant(value='segment'))])), Assign(targets=[Name(id='test_df_1', ctx=Store())], value=Call(func=Attribute(value=Name(id='test_df_1', ctx=Load()), attr='reorder_levels', ctx=Load()), args=[List(elts=[Constant(value=1), Constant(value=0)], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='test_df_1', ctx=Store())], value=Call(func=Attribute(value=Name(id='test_df_1', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Attribute(value=Attribute(value=Name(id='test_df_1', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Store())], value=List(elts=[Constant(value='segment'), Constant(value='feature')], ctx=Load())), Assign(targets=[Name(id='test_df_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='test_df_2', ctx=Load()), attr='pivot', ctx=Load()), args=[], keywords=[keyword(arg='index', value=Constant(value='timestamp')), keyword(arg='columns', value=Constant(value='segment'))])), Assign(targets=[Name(id='test_df_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='test_df_2', ctx=Load()), attr='reorder_levels', ctx=Load()), args=[List(elts=[Constant(value=1), Constant(value=0)], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='test_df_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='test_df_2', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Attribute(value=Attribute(value=Name(id='test_df_2', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Store())], value=List(elts=[Constant(value='segment'), Constant(value='feature')], ctx=Load())), Assign(targets=[Name(id='forecast_df_1', ctx=Store())], value=Call(func=Attribute(value=Name(id='forecast_df_1', ctx=Load()), attr='pivot', ctx=Load()), args=[], keywords=[keyword(arg='index', value=Constant(value='timestamp')), keyword(arg='columns', value=Constant(value='segment'))])), Assign(targets=[Name(id='forecast_df_1', ctx=Store())], value=Call(func=Attribute(value=Name(id='forecast_df_1', ctx=Load()), attr='reorder_levels', ctx=Load()), args=[List(elts=[Constant(value=1), Constant(value=0)], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='forecast_df_1', ctx=Store())], value=Call(func=Attribute(value=Name(id='forecast_df_1', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Attribute(value=Attribute(value=Name(id='forecast_df_1', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Store())], value=List(elts=[Constant(value='segment'), Constant(value='feature')], ctx=Load())), Assign(targets=[Name(id='forecast_df_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='forecast_df_2', ctx=Load()), attr='pivot', ctx=Load()), args=[], keywords=[keyword(arg='index', value=Constant(value='timestamp')), keyword(arg='columns', value=Constant(value='segment'))])), Assign(targets=[Name(id='forecast_df_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='forecast_df_2', ctx=Load()), attr='reorder_levels', ctx=Load()), args=[List(elts=[Constant(value=1), Constant(value=0)], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='forecast_df_2', ctx=Store())], value=Call(func=Attribute(value=Name(id='forecast_df_2', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Attribute(value=Attribute(value=Name(id='forecast_df_2', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Store())], value=List(elts=[Constant(value='segment'), Constant(value='feature')], ctx=Load())), Assign(targets=[Name(id='test_df_1', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[Name(id='test_df_1', ctx=Load())], keywords=[keyword(arg='freq', value=Constant(value='1D'))])), Assign(targets=[Name(id='test_df_2', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[Name(id='test_df_2', ctx=Load())], keywords=[keyword(arg='freq', value=Constant(value='1D'))])), Assign(targets=[Name(id='forecast_df_1', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[Name(id='forecast_df_1', ctx=Load())], keywords=[keyword(arg='freq', value=Constant(value='1D'))])), Assign(targets=[Name(id='forecast_df_2', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[Name(id='forecast_df_2', ctx=Load())], keywords=[keyword(arg='freq', value=Constant(value='1D'))])), Assign(targets=[Name(id='metric', ctx=Store())], value=Call(func=Name(id='MAE', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Constant(value='per-segment'))])), Assign(targets=[Name(id='metric_value_1', ctx=Store())], value=Call(func=Name(id='metric', ctx=Load()), args=[], keywords=[keyword(arg='y_true', value=Name(id='test_df_1', ctx=Load())), keyword(arg='y_pred', value=Name(id='forecast_df_1', ctx=Load()))])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Attribute(value=Name(id='metric_value_1', ctx=Load()), attr='keys', ctx=Load()), args=[], keywords=[])], keywords=[]), ops=[Eq()], comparators=[List(elts=[Constant(value='A'), Constant(value='B')], ctx=Load())])), Assert(test=Compare(left=Subscript(value=Name(id='metric_value_1', ctx=Load()), slice=Constant(value='A'), ctx=Load()), ops=[Eq()], comparators=[Constant(value=0.1)])), Assert(test=Compare(left=Subscript(value=Name(id='metric_value_1', ctx=Load()), slice=Constant(value='B'), ctx=Load()), ops=[Eq()], comparators=[Constant(value=0.2)])), Assign(targets=[Name(id='metric_value_2', ctx=Store())], value=Call(func=Name(id='metric', ctx=Load()), args=[], keywords=[keyword(arg='y_true', value=Name(id='test_df_2', ctx=Load())), keyword(arg='y_pred', value=Name(id='forecast_df_2', ctx=Load()))])), Assert(test=Compare(left=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Attribute(value=Name(id='metric_value_2', ctx=Load()), attr='keys', ctx=Load()), args=[], keywords=[])], keywords=[]), ops=[Eq()], comparators=[List(elts=[Constant(value='B'), Constant(value='C')], ctx=Load())])), Assert(test=Compare(left=Subscript(value=Name(id='metric_value_2', ctx=Load()), slice=Constant(value='C'), ctx=Load()), ops=[Eq()], comparators=[Constant(value=1)])), Assert(test=Compare(left=Subscript(value=Name(id='metric_value_2', ctx=Load()), slice=Constant(value='B'), ctx=Load()), ops=[Eq()], comparators=[Constant(value=0)]))], decorator_list=[])], type_ignores=[])