Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), Import(names=[alias(name='pytest')]), ImportFrom(module='etna.datasets.tsdataset', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.models', names=[alias(name='NaiveModel')], level=0), ImportFrom(module='etna.transforms.decomposition', names=[alias(name='STLTransform')], level=0), ImportFrom(module='etna.transforms.decomposition.stl', names=[alias(name='_OneSegmentSTLTransform')], level=0), FunctionDef(name='add_trend', args=arguments(posonlyargs=[], args=[arg(arg='series', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())), arg(arg='coef', annotation=Name(id='float', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1)]), body=[Expr(value=Constant(value='Add trend to given series.')), Assign(targets=[Name(id='new_series', ctx=Store())], value=Call(func=Attribute(value=Name(id='series', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='size', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='series', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load())), Assign(targets=[Name(id='indices', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Name(id='size', ctx=Load())], keywords=[])), AugAssign(target=Name(id='new_series', ctx=Store()), op=Add(), value=BinOp(left=Name(id='indices', ctx=Load()), op=Mult(), right=Name(id='coef', ctx=Load()))), Return(value=Name(id='new_series', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())), FunctionDef(name='add_seasonality', args=arguments(posonlyargs=[], args=[arg(arg='series', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())), arg(arg='period', annotation=Name(id='int', ctx=Load())), arg(arg='magnitude', annotation=Name(id='float', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Add seasonality to given series.')), Assign(targets=[Name(id='new_series', ctx=Store())], value=Call(func=Attribute(value=Name(id='series', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='size', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='series', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load())), Assign(targets=[Name(id='indices', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Name(id='size', ctx=Load())], keywords=[])), AugAssign(target=Name(id='new_series', ctx=Store()), op=Add(), value=BinOp(left=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='sin', ctx=Load()), args=[BinOp(left=BinOp(left=BinOp(left=Constant(value=2), op=Mult(), right=Attribute(value=Name(id='np', ctx=Load()), attr='pi', ctx=Load())), op=Mult(), right=Name(id='indices', ctx=Load())), op=Div(), right=Name(id='period', ctx=Load()))], keywords=[]), op=Mult(), right=Name(id='magnitude', ctx=Load()))), Return(value=Name(id='new_series', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())), FunctionDef(name='get_one_df', args=arguments(posonlyargs=[], args=[arg(arg='coef', annotation=Name(id='float', ctx=Load())), arg(arg='period', annotation=Name(id='int', ctx=Load())), arg(arg='magnitude', annotation=Name(id='float', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='date_range', ctx=Load()), args=[], keywords=[keyword(arg='start', value=Constant(value='2020-01-01')), keyword(arg='end', value=Constant(value='2020-03-01')), keyword(arg='freq', value=Constant(value='D'))])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=Constant(value=0)), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=Call(func=Name(id='add_seasonality', ctx=Load()), args=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Load())], keywords=[keyword(arg='period', value=Name(id='period', ctx=Load())), keyword(arg='magnitude', value=Name(id='magnitude', ctx=Load()))])), Assign(targets=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Store())], value=Call(func=Name(id='add_trend', ctx=Load()), args=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Load())], keywords=[keyword(arg='coef', value=Name(id='coef', ctx=Load()))])), Return(value=Name(id='df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='df_trend_seasonal_one_segment', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Name(id='get_one_df', ctx=Load()), args=[], keywords=[keyword(arg='coef', value=Constant(value=0.1)), keyword(arg='period', value=Constant(value=7)), keyword(arg='magnitude', value=Constant(value=1))])), Expr(value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='set_index', ctx=Load()), args=[Constant(value='timestamp')], keywords=[keyword(arg='inplace', value=Constant(value=True))])), Return(value=Name(id='df', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='df_trend_seasonal_starting_with_nans_one_segment', args=arguments(posonlyargs=[], args=[arg(arg='df_trend_seasonal_one_segment')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='result', ctx=Store())], value=Name(id='df_trend_seasonal_one_segment', ctx=Load())), Assign(targets=[Subscript(value=Attribute(value=Name(id='result', ctx=Load()), attr='iloc', ctx=Load()), slice=Slice(upper=Constant(value=2)), ctx=Store())], value=Attribute(value=Name(id='np', ctx=Load()), attr='NaN', ctx=Load())), Return(value=Name(id='result', ctx=Load()))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='ts_trend_seasonal', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df_1', ctx=Store())], value=Call(func=Name(id='get_one_df', ctx=Load()), args=[], keywords=[keyword(arg='coef', value=Constant(value=0.1)), keyword(arg='period', value=Constant(value=7)), keyword(arg='magnitude', value=Constant(value=1))])), Assign(targets=[Subscript(value=Name(id='df_1', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='segment_1')), Assign(targets=[Name(id='df_2', ctx=Store())], value=Call(func=Name(id='get_one_df', ctx=Load()), args=[], keywords=[keyword(arg='coef', value=Constant(value=0.05)), keyword(arg='period', value=Constant(value=7)), keyword(arg='magnitude', value=Constant(value=2))])), Assign(targets=[Subscript(value=Name(id='df_2', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='segment_2')), Assign(targets=[Name(id='classic_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='df_1', ctx=Load()), Name(id='df_2', ctx=Load())], ctx=Load())], keywords=[keyword(arg='ignore_index', value=Constant(value=True))])), Return(value=Call(func=Name(id='TSDataset', ctx=Load()), args=[Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='classic_df', ctx=Load())], keywords=[])], keywords=[keyword(arg='freq', value=Constant(value='D'))]))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='ts_trend_seasonal_starting_with_nans', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df_1', ctx=Store())], value=Call(func=Name(id='get_one_df', ctx=Load()), args=[], keywords=[keyword(arg='coef', value=Constant(value=0.1)), keyword(arg='period', value=Constant(value=7)), keyword(arg='magnitude', value=Constant(value=1))])), Assign(targets=[Subscript(value=Name(id='df_1', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='segment_1')), Assign(targets=[Name(id='df_2', ctx=Store())], value=Call(func=Name(id='get_one_df', ctx=Load()), args=[], keywords=[keyword(arg='coef', value=Constant(value=0.05)), keyword(arg='period', value=Constant(value=7)), keyword(arg='magnitude', value=Constant(value=2))])), Assign(targets=[Subscript(value=Name(id='df_2', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='segment_2')), Assign(targets=[Name(id='classic_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='df_1', ctx=Load()), Name(id='df_2', ctx=Load())], ctx=Load())], keywords=[keyword(arg='ignore_index', value=Constant(value=True))])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='classic_df', ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[List(elts=[Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=0), ctx=Load()), Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=1), ctx=Load())], ctx=Load()), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Constant(value='segment_1'), Constant(value='target')], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Store())], value=Constant(value=None)), Return(value=Call(func=Name(id='TSDataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[keyword(arg='freq', value=Constant(value='D'))]))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='ts_trend_seasonal_nan_tails', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='df_1', ctx=Store())], value=Call(func=Name(id='get_one_df', ctx=Load()), args=[], keywords=[keyword(arg='coef', value=Constant(value=0.1)), keyword(arg='period', value=Constant(value=7)), keyword(arg='magnitude', value=Constant(value=1))])), Assign(targets=[Subscript(value=Name(id='df_1', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='segment_1')), Assign(targets=[Name(id='df_2', ctx=Store())], value=Call(func=Name(id='get_one_df', ctx=Load()), args=[], keywords=[keyword(arg='coef', value=Constant(value=0.05)), keyword(arg='period', value=Constant(value=7)), keyword(arg='magnitude', value=Constant(value=2))])), Assign(targets=[Subscript(value=Name(id='df_2', ctx=Load()), slice=Constant(value='segment'), ctx=Store())], value=Constant(value='segment_2')), Assign(targets=[Name(id='classic_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='df_1', ctx=Load()), Name(id='df_2', ctx=Load())], ctx=Load())], keywords=[keyword(arg='ignore_index', value=Constant(value=True))])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_dataset', ctx=Load()), args=[Name(id='classic_df', ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[List(elts=[Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=0), ctx=Load()), Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=1), ctx=Load()), Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=2)), ctx=Load()), Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load())], ctx=Load()), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Constant(value='segment_1'), Constant(value='target')], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Store())], value=Constant(value=None)), Return(value=Call(func=Name(id='TSDataset', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[keyword(arg='freq', value=Constant(value='D'))]))], decorator_list=[Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load())], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='test_transform_one_segment', args=arguments(posonlyargs=[], args=[arg(arg='df_name'), arg(arg='model'), arg(arg='request')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test that transform for one segment removes trend and seasonality.')), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='request', ctx=Load()), attr='getfixturevalue', ctx=Load()), args=[Name(id='df_name', ctx=Load())], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='_OneSegmentSTLTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='period', value=Constant(value=7)), keyword(arg='model', value=Name(id='model', ctx=Load()))])), Assign(targets=[Name(id='df_transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_expected', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Subscript(value=Attribute(value=Name(id='df_expected', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[UnaryOp(op=Invert(), operand=Call(func=Attribute(value=Subscript(value=Name(id='df_expected', ctx=Load()), slice=Constant(value='target'), ctx=Load()), attr='isna', ctx=Load()), args=[], keywords=[])), Constant(value='target')], ctx=Load()), ctx=Store())], value=Constant(value=0)), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_allclose', ctx=Load()), args=[Subscript(value=Name(id='df_transformed', ctx=Load()), slice=Constant(value='target'), ctx=Load()), Subscript(value=Name(id='df_expected', ctx=Load()), slice=Constant(value='target'), ctx=Load())], keywords=[keyword(arg='atol', value=Constant(value=0.3))]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='model'), List(elts=[Constant(value='arima'), Constant(value='holt')], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='df_name'), List(elts=[Constant(value='df_trend_seasonal_one_segment'), Constant(value='df_trend_seasonal_starting_with_nans_one_segment')], ctx=Load())], keywords=[])]), FunctionDef(name='test_transform_multi_segments', args=arguments(posonlyargs=[], args=[arg(arg='ts_name'), arg(arg='model'), arg(arg='request')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test that transform for all segments removes trend and seasonality.')), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Attribute(value=Name(id='request', ctx=Load()), attr='getfixturevalue', ctx=Load()), args=[Name(id='ts_name', ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_expected', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[keyword(arg='flatten', value=Constant(value=True))])), Assign(targets=[Subscript(value=Attribute(value=Name(id='df_expected', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[UnaryOp(op=Invert(), operand=Call(func=Attribute(value=Subscript(value=Name(id='df_expected', ctx=Load()), slice=Constant(value='target'), ctx=Load()), attr='isna', ctx=Load()), args=[], keywords=[])), Constant(value='target')], ctx=Load()), ctx=Store())], value=Constant(value=0)), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='STLTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='period', value=Constant(value=7)), keyword(arg='model', value=Name(id='model', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='transforms', value=List(elts=[Name(id='transform', ctx=Load())], ctx=Load()))])), Assign(targets=[Name(id='df_transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[keyword(arg='flatten', value=Constant(value=True))])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_allclose', ctx=Load()), args=[Subscript(value=Name(id='df_transformed', ctx=Load()), slice=Constant(value='target'), ctx=Load()), Subscript(value=Name(id='df_expected', ctx=Load()), slice=Constant(value='target'), ctx=Load())], keywords=[keyword(arg='atol', value=Constant(value=0.3))]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='model'), List(elts=[Constant(value='arima'), Constant(value='holt')], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='ts_name'), List(elts=[Constant(value='ts_trend_seasonal'), Constant(value='ts_trend_seasonal_starting_with_nans')], ctx=Load())], keywords=[])]), FunctionDef(name='test_inverse_transform_one_segment', args=arguments(posonlyargs=[], args=[arg(arg='df_name'), arg(arg='model'), arg(arg='request')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="Test that transform + inverse_transform don't change dataframe.")), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='request', ctx=Load()), attr='getfixturevalue', ctx=Load()), args=[Name(id='df_name', ctx=Load())], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='_OneSegmentSTLTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='period', value=Constant(value=7)), keyword(arg='model', value=Name(id='model', ctx=Load()))])), Assign(targets=[Name(id='df_transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='df_inverse_transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[Name(id='df_transformed', ctx=Load())], keywords=[])), Assert(test=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Load()), attr='equals', ctx=Load()), args=[Subscript(value=Name(id='df_inverse_transformed', ctx=Load()), slice=Constant(value='target'), ctx=Load())], keywords=[]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='model'), List(elts=[Constant(value='arima'), Constant(value='holt')], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='df_name'), List(elts=[Constant(value='df_trend_seasonal_one_segment'), Constant(value='df_trend_seasonal_starting_with_nans_one_segment')], ctx=Load())], keywords=[])]), FunctionDef(name='test_inverse_transform_multi_segments', args=arguments(posonlyargs=[], args=[arg(arg='ts_name'), arg(arg='model'), arg(arg='request')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="Test that transform + inverse_transform don't change tsdataset.")), Assign(targets=[Name(id='ts', ctx=Store())], value=Call(func=Attribute(value=Name(id='request', ctx=Load()), attr='getfixturevalue', ctx=Load()), args=[Name(id='ts_name', ctx=Load())], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='STLTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='period', value=Constant(value=7)), keyword(arg='model', value=Name(id='model', ctx=Load()))])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[keyword(arg='flatten', value=Constant(value=True))])), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='transforms', value=List(elts=[Name(id='transform', ctx=Load())], ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='df_inverse_transformed', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[keyword(arg='flatten', value=Constant(value=True))])), Assert(test=Call(func=Attribute(value=Subscript(value=Name(id='df_inverse_transformed', ctx=Load()), slice=Constant(value='target'), ctx=Load()), attr='equals', ctx=Load()), args=[Subscript(value=Name(id='df', ctx=Load()), slice=Constant(value='target'), ctx=Load())], keywords=[]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='model'), List(elts=[Constant(value='arima'), Constant(value='holt')], ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='ts_name'), List(elts=[Constant(value='ts_trend_seasonal'), Constant(value='ts_trend_seasonal_starting_with_nans')], ctx=Load())], keywords=[])]), FunctionDef(name='test_forecast', args=arguments(posonlyargs=[], args=[arg(arg='ts_trend_seasonal'), arg(arg='model_stl')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test that transform works correctly in forecast.')), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='STLTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='period', value=Constant(value=7)), keyword(arg='model', value=Name(id='model_stl', ctx=Load()))])), Assign(targets=[Tuple(elts=[Name(id='ts_train', ctx=Store()), Name(id='ts_test', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_trend_seasonal', ctx=Load()), attr='train_test_split', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='ts_trend_seasonal', ctx=Load()), attr='index', ctx=Load()), slice=Constant(value=0), ctx=Load()), Subscript(value=Attribute(value=Name(id='ts_trend_seasonal', ctx=Load()), attr='index', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=4)), ctx=Load()), Subscript(value=Attribute(value=Name(id='ts_trend_seasonal', ctx=Load()), attr='index', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=3)), ctx=Load()), Subscript(value=Attribute(value=Name(id='ts_trend_seasonal', ctx=Load()), attr='index', ctx=Load()), slice=UnaryOp(op=USub(), operand=Constant(value=1)), ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='ts_train', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='transforms', value=List(elts=[Name(id='transform', ctx=Load())], ctx=Load()))])), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='NaiveModel', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='ts_train', ctx=Load())], keywords=[])), Assign(targets=[Name(id='ts_future', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts_train', ctx=Load()), attr='make_future', ctx=Load()), args=[], keywords=[keyword(arg='future_steps', value=Constant(value=3)), keyword(arg='tail_steps', value=Attribute(value=Name(id='model', ctx=Load()), attr='context_size', ctx=Load()))])), Assign(targets=[Name(id='ts_forecast', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='forecast', ctx=Load()), args=[Name(id='ts_future', ctx=Load())], keywords=[keyword(arg='prediction_size', value=Constant(value=3))])), For(target=Name(id='segment', ctx=Store()), iter=Attribute(value=Name(id='ts_forecast', ctx=Load()), attr='segments', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_allclose', ctx=Load()), args=[Subscript(value=Name(id='ts_forecast', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segment', ctx=Load()), Constant(value='target')], ctx=Load()), ctx=Load()), Subscript(value=Name(id='ts_test', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segment', ctx=Load()), Constant(value='target')], ctx=Load()), ctx=Load())], keywords=[keyword(arg='atol', value=Constant(value=0.1))]))], orelse=[])], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='model_stl'), List(elts=[Constant(value='arima'), Constant(value='holt')], ctx=Load())], keywords=[])]), FunctionDef(name='test_transform_raise_error_if_not_fitted', args=arguments(posonlyargs=[], args=[arg(arg='df_trend_seasonal_one_segment')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test that transform for one segment raise error when calling transform without being fit.')), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='_OneSegmentSTLTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='period', value=Constant(value=7)), keyword(arg='model', value=Constant(value='arima'))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Transform is not fitted!'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df_trend_seasonal_one_segment', ctx=Load()))]))])], decorator_list=[]), FunctionDef(name='test_inverse_transform_raise_error_if_not_fitted', args=arguments(posonlyargs=[], args=[arg(arg='df_trend_seasonal_one_segment')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Test that transform for one segment raise error when calling inverse_transform without being fit.')), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='_OneSegmentSTLTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='period', value=Constant(value=7)), keyword(arg='model', value=Constant(value='arima'))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='Transform is not fitted!'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='df_trend_seasonal_one_segment', ctx=Load()))]))])], decorator_list=[]), FunctionDef(name='test_fit_transform_with_nans_in_tails', args=arguments(posonlyargs=[], args=[arg(arg='ts_trend_seasonal_nan_tails'), arg(arg='model_stl')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='STLTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='period', value=Constant(value=7)), keyword(arg='model', value=Name(id='model_stl', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='ts_trend_seasonal_nan_tails', ctx=Load()), attr='fit_transform', ctx=Load()), args=[], keywords=[keyword(arg='transforms', value=List(elts=[Name(id='transform', ctx=Load())], ctx=Load()))])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='testing', ctx=Load()), attr='assert_allclose', ctx=Load()), args=[Call(func=Attribute(value=Subscript(value=Name(id='ts_trend_seasonal_nan_tails', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Constant(value='target')], ctx=Load()), ctx=Load()), attr='dropna', ctx=Load()), args=[], keywords=[]), Constant(value=0)], keywords=[keyword(arg='atol', value=Constant(value=0.25))]))], decorator_list=[Call(func=Attribute(value=Attribute(value=Name(id='pytest', ctx=Load()), attr='mark', ctx=Load()), attr='parametrize', ctx=Load()), args=[Constant(value='model_stl'), List(elts=[Constant(value='arima'), Constant(value='holt')], ctx=Load())], keywords=[])]), FunctionDef(name='test_fit_transform_with_nans_in_middle_raise_error', args=arguments(posonlyargs=[], args=[arg(arg='df_with_nans')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Name(id='STLTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Constant(value='target')), keyword(arg='period', value=Constant(value=7))])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='raises', ctx=Load()), args=[Name(id='ValueError', ctx=Load())], keywords=[keyword(arg='match', value=Constant(value='The input column contains NaNs in the middle of the series!'))]))], body=[Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Name(id='transform', ctx=Load()), attr='fit_transform', ctx=Load()), args=[Name(id='df_with_nans', ctx=Load())], keywords=[]))])], decorator_list=[])], type_ignores=[])